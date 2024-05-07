from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Project, Cluster, Db_credentials, Db_credentials
from .serializers import projectSerializers, ClusterSerializers
from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
import requests
import zipfile
import io
from django.http import JsonResponse
import time
import logging
from datetime import datetime
import os
from dotenv import load_dotenv
 

load_dotenv() 
 
project_logger = logging.getLogger('project_logger')
rename_project_logger = logging.getLogger('rename_project_logger')
 
 
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = projectSerializers
 
    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        project_name = request.data.get('project_name')
       
        if not user_id:
            return Response({
                "error":"user_id is required "
 
            },status = status.HTTP_400_BAD_REQUEST)
        if not project_name:            
            return Response({
                "error":"project name is required "
 
            },status = status.HTTP_400_BAD_REQUEST)   
 
        existing_project = Project.objects.filter(project_name= project_name).exists()
        
 
        if existing_project == True:
            return Response({
                "error":"project Already exists"
            },status = status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk= user_id)
            
            project = Project.objects.create(user=user, project_name=project_name)
 
        except User.DoestNotExist:
            return Response({"error": "User with the provided ID does not exist."},
                            status=status.HTTP_404_NOT_FOUND)
 
        project.save()
 
        log_entry = f"user={user.username} projectName={project.project_name} msg={project.project_name} created "
        project_logger.info(log_entry)
 
        serializer= projectSerializers(project)
 
        return Response(
            serializer.data,status = status.HTTP_201_CREATED)   
    
 
 
 
    @action(detail=True, methods=['PUT'])
    def rename_project(self, request, pk=None):
        """
        Rename a project by its ID.
 
        Expected JSON payload:
        {
            "new_project_name": "new_name"
        }
        """
        project = self.get_object()
        new_project_name = request.data.get('new_project_name')
 
        if not new_project_name:
            return Response({
                "error": "new_project_name is required"
            }, status=status.HTTP_400_BAD_REQUEST)
 
        existing_project = Project.objects.exclude(pk=project.id).filter(project_name=new_project_name).exists()
 
        if existing_project:
            return Response({
                "error": "Project with the new name already exists"
            }, status=status.HTTP_400_BAD_REQUEST)
      
 
        project.project_name = new_project_name
        project.save()
 
        log_entry_after_rename = f"user={project.user.username} projectname={project.project_name} msg={ project.project_name } renamed"
        rename_project_logger.info(log_entry_after_rename)
 
        serializer = projectSerializers(project)
        return Response(serializer.data, status=status.HTTP_200_OK)         
 
from rest_framework.views import APIView
import urllib
import base64
import urllib.parse
import urllib.request
import json
import hashlib
import hmac
import re
import yaml
    
class ComputeOfferingsAPIView(APIView):
    def get(self, request):
        
        baseurl = os.getenv('BASEURL')

        request_data = {
                'command': 'listServiceOfferings',
                'response': 'json',
                'apikey': os.getenv('API_KEY')
        }
        secret_key = os.getenv('SECRET_KEY_ENCODED').encode('utf-8')

            
            
 
        request_str = '&'.join(['='.join([k, urllib.parse.quote_plus(request_data[k])]) for k in request_data.keys()])
 
        sig_str = '&'.join(['='.join([k.lower(), urllib.parse.quote_plus(request_data[k]).lower().replace('+', '%20')])
                            for k in sorted(request_data.keys())])
 
        sig = urllib.parse.quote_plus(
            base64.b64encode(hmac.new(secret_key, sig_str.encode('utf-8'), hashlib.sha1).digest()).
            strip())
 
        req = baseurl + request_str + '&signature=' + sig
 
        try:
            res = urllib.request.urlopen(req)
            response_data = json.loads(res.read().decode('utf-8'))
 
            if 'listserviceofferingsresponse' in response_data:
                service_offerings = response_data['listserviceofferingsresponse'].get('serviceoffering', [])
 
                # Create a list to store compute offerings
                compute_offerings = []
 
                # Add data to the list
                for offering in service_offerings:
                    compute_offerings.append({
                        'name': offering['name'],
                        'cpunumber': offering['cpunumber'],
                        'cpuspeed': offering['cpuspeed'],
                        'memory': offering['memory']
                    })
 
                return Response({'compute_offerings': compute_offerings})
            else:
                error_message = "Error: Unable to fetch compute offerings."
        except Exception as e:
            error_message = f"Error: {str(e)}"
 
        return Response({'error': error_message}, status=500)   



from rest_framework.views import APIView
from rest_framework.response import Response
import openstack
 
class FlavorList(APIView):
    def get(self, request):
        # Retrieve flavors from OpenStack
        conn = openstack.connect(
            auth_url = os.getenv('AUTH_URL'),
            project_name = os.getenv('PROJECT_NAME'),
            username = os.getenv('USERNAME'),
            password = os.getenv('PASSWORD'),
            user_domain_name = os.getenv('USER_DOMAIN_NAME'),
            project_domain_name = os.getenv('PROJECT_DOMAIN_NAME')

        )
        flavors = conn.compute.flavors()
 
        # Transform flavors data into a list of dictionaries
        flavor_data = [

            
            {
                'flavors': {'flavor_id': flavor.id, 'name': flavor.name},
              
                'ram': flavor.ram,
                'vcpus': flavor.vcpus,
                'disk': flavor.disk,
                'is_public': flavor.is_public
            }
            for flavor in flavors
        ]
 
        # Return flavors data as JSON response
        return Response(flavor_data)
 
@api_view(['GET'])
def get_projects_by_user(request, user_id):
    projects = Project.objects.filter(user_id=user_id)
    serializer = projectSerializers(projects, many=True)
    return Response(serializer.data)
 


from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


   
# CLUSTER CREATE API GET CLUSTER BY USER ID AND & PROJECT I
k8s_variables = {}
deleteCluster_name = ''
temp_variables = {}
clusterName = ''
clusterType = ''
databaseVersion = ''
backupMethod=''
providerName = ''
userId = ''
projectID = ''
apiEndpoint = ''
accessKey = ''
secretKey = ''
appUser= ''
computeOffering = ''

openstackusername = ''
tenant_name = ''
openstackpassword= ''
auth_url = ''
region = ''

 
# Define a logger for cluster-related actions
cluster_logger = logging.getLogger('cluster_logger')
class ClusterViewSet(viewsets.ModelViewSet):
    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializers
 
    def create(self, request, *args, **kwargs):
        global temp_variables
        global clusterName
        global clusterType
        global databaseVersion
        global backupMethod
        global providerName
        global userId
        global projectId
        global apiEndpoint
        global accessKey
        global secretKey
        global computeOffering

        global openstackusername
        global openstackpassword
     
        
        username = request.data.get('db_user')
        password = request.data.get('db_password')
        user_id = request.data.get('user')
        project_id = request.data.get('project')
        cluster_name = request.data.get('cluster_name')
        cluster_type = request.data.get('cluster_type')
        database_version = request.data.get('postgres_version')
        backup_method = request.data.get('backup_method')
 
        provider_name = request.data.get('provider')
        provider_endpoint = request.data.get('provider_endpoint')
        provider_access_token = request.data.get('provider_access_token')
        provider_secret_key = request.data.get('provider_secret_key')
        kubeconfig_data = request.data.get('kubeconfig_data')

        openstackusername = request.data.get ('openstackusername')
     
        tenant_name = request.data.get ('tenant_name')
        openstackpassword= request.data.get ('openstackPassword')

        auth_url = request.data.get ('auth_url')
        region = request.data.get ('region')
  
        computeOffering  = request.data.get('computeOffering')
        storageOffering = request.data.get('storageOffering')
        mount_point = request.data.get('mount_point')
       
 
        # Adding global variable
        clusterName = cluster_name
        clusterType = cluster_type
        databaseVersion = database_version
        backupMethod = backup_method
        providerName = provider_name
        userId = user_id
        projectId = project_id
        apiEndpoint = provider_endpoint
        accessKey = provider_access_token
        secretKey = provider_secret_key
        
        openstackusername=openstackusername,
        tenant_name=tenant_name,
        openstackpassword=openstackpassword,
        auth_url=auth_url,
        region=region,
       
        # Remove newline characters from kubeconfig_data
        kubeconfig_data = kubeconfig_data.replace('\n', ' ')
 
        # Assuming kubeconfig_data is a YAML string, you can load it to ensure proper formatting
        kubeconfig_dict = yaml.safe_load(kubeconfig_data)
       
        user = User.objects.get(pk=user_id)
              
        # Check if cluster with the same name already exists in the project
        existing_cluster = Cluster.objects.filter(project=project_id, cluster_name=cluster_name).exists()
 
        if existing_cluster:
            return Response({"error": "Cluster with the same name already exists in the project"}, status=status.HTTP_400_BAD_REQUEST)
 
        try:
            user = User.objects.get(pk=user_id)
            project = Project.objects.get(pk=project_id)
 
        except User.DoesNotExist:
            return Response({"error": "User with the provided ID does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Project.DoesNotExist:
            return Response({"error": "No Project! has been selected.."}, status=status.HTTP_404_NOT_FOUND)
            

        project_id = os.getenv('PROJECT_ID')
        private_token = os.getenv('PRIVATE_TOKEN')
        base_url = os.getenv('BASE_URL')

        headers = {"PRIVATE-TOKEN": private_token}
        
        if provider_name == 'Kubernetes' and cluster_type == 'Standalone':
            formData = {
                "ref": 'deploy-postgres-k8s',
                "variables": [
                {"key": "DATABASE_NAME", "value": cluster_name},
                {"key": "KUBE_CONFIG", "value": kubeconfig_data},
                {"key": "DATABASE_VERSION", "value": database_version},
                {"key": "BACKUP_METHOD", "value": backup_method},
                {"key": "USERNAME", "value": username}, 
                {"key": "PASSWORD", "value": password},           
             ]
            }
            response = trigger_single(base_url, project_id, headers, user_id, formData)
            if response == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    provider=provider_name,  
                )
                cluster.save()
                
                serializer = ClusterSerializers(cluster)
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
              
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:            
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)   

        elif provider_name == 'Cloudstack' and cluster_type == 'Multiple':
            formData = {
                "ref": 'ha-postgres-cluster',
                "variables": [
                {"key": "DATABASE_NAME", "value": cluster_name},
                {"key": "PROVIDER_ENDPOINT", "value": provider_endpoint},
                {"key": "PROVIDER_SECRET_KEY", "value": provider_secret_key},
                {"key": "PROVIDER_ACCESS_KEY", "value": provider_access_token},
                {"key": "COMPUTE_OFFERING", "value": computeOffering},
                {"key": "BACKUP_METHOD", "value": backup_method},
                {"key": "STORAGE_OFFERING", "value": storageOffering},
                {"key": "DATABASE_VERSION", "value": database_version},
                {"key": "USERNAME", "value": username}, 
                {"key": "PASSWORD", "value": password},           
             ]
            }
            response = trigger_single(base_url, project_id, headers, user_id,formData )
            print("CloudStack HA branch trigger.....")
            if response == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    backup_method=backup_method,

                    provider=provider_name
                )
                cluster.save()
                serializer = ClusterSerializers(cluster)
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                    
            else:            
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
        elif provider_name == 'Harvester' and cluster_type == 'Standalone':
            print("harvesr ha branch trigger.....")

            response = trigger_single(base_url, project_id, headers, user_id, 'Harvester')
            if response == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    backup_method=backup_method,

                    provider=provider_name
                )
                cluster.save()
                serializer = ClusterSerializers(cluster)
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                    
            else:            
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
         
 
         
 
 
        elif provider_name == 'Cloudstack' and cluster_type == 'Standalone':
            barman_ip = "172.16.1.131"
            bitblast_ip = "172.16.1.131"
            formData = {
                "ref": 'infra-and-db',
                "variables": [
                {"key": "BITBLAST_USERNAME", "value": user.username},
                {"key": "DATABASE_NAME", "value": cluster_name},
                {"key": "PROVIDER_ENDPOINT", "value": provider_endpoint},
                {"key": "PROVIDER_SECRET_KEY", "value": provider_secret_key},
                {"key": "PROVIDER_ACCESS_KEY", "value": provider_access_token},
                {"key": "BACKUP_METHOD", "value": backup_method},
                {"key": "MOUNT_POINT", "value": mount_point},
                {"key": "BARMAN_SERVER", "value":barman_ip},
                {"key": "BITBLAST_IP", "value": bitblast_ip},
                {"key": "COMPUTE_OFFERING", "value": computeOffering},
                {"key": "STORAGE_OFFERING", "value": storageOffering},
                {"key": "DATABASE_VERSION", "value": database_version},
                {"key": "USERNAME", "value": username},
                {"key": "PASSWORD", "value": password},           
             ]
            }
            response = trigger_single(base_url, project_id, headers, user_id,formData)
            print("CloudStack branch trigger.....")
            if response == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    backup_method=backup_method,
                    provider=provider_name,
                    
                )
                cluster.save()
                serializer = ClusterSerializers(cluster)
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:            
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      

        elif provider_name == 'Openstack' and cluster_type == 'Standalone':
            formData = {
                "ref": 'openstack-provider-ha-vip',
                "variables": [
                {"key": "DATABASE_NAME", "value": cluster_name},
                {"key": "DATABASE_VERSION", "value": database_version},
                {"key": "BACKUP_METHOD", "value": backup_method},
                {"key": "OPENSTACK_USER", "value": openstackusername},
                {"key": "OPENSTACK_PASSWORD", "value":  openstackpassword},
                {"key": "TENANT_NAME", "value": tenant_name}, 
                {"key": "REGION", "value": region}, 
                {"key": "AUTH_URL", "value": auth_url},           
             ]
            }
            response = trigger_single(base_url, project_id, headers, user_id, formData)
            print("Openstack Standalone branch trigger.....")
            if response == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    backup_method=backup_method,
                    provider=provider_name,
                    
                )
                cluster.save()
                serializer = ClusterSerializers(cluster)
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:            
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        elif provider_name == 'Openstack' and cluster_type == 'Multiple':
            formData = {
                "ref": 'openstack-provider-ha-vip',
                "variables": [
                {"key": "DATABASE_NAME", "value": cluster_name},
                {"key": "DATABASE_VERSION", "value": database_version},
                {"key": "BACKUP_METHOD", "value": backup_method},
                {"key": "OPENSTACK_USER", "value": openstackusername},
                {"key": "OPENSTACK_PASSWORD", "value":  openstackpassword},
                {"key": "TENANT_NAME", "value": tenant_name}, 
                {"key": "REGION", "value": region}, 
                {"key": "AUTH_URL", "value": auth_url},           
             ]
            }
            response = trigger_single(base_url, project_id, headers, user_id, formData)
            print("Openstack HA branch trigger.....")
            if response == 200:
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    backup_method=backup_method,
                    provider=provider_name,
                    
                )
                cluster.save()
                serializer = ClusterSerializers(cluster)
                # Log cluster creation information
                log_entry = f"user={user.username} clustername={cluster.cluster_name} provider={provider_name} project={project} msg={cluster.cluster_name} created"
                cluster_logger.info(log_entry)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:            
                return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response({'message': 'Cluster creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)        
            
 
    
        
    @action(detail=False, methods=['get'])
    def check_cluster_exists(self, request, *args, **kwargs):
 
        cluster_name = request.query_params.get('cluster_name', None)
        project_id = request.query_params.get('project_id', None)
 
        if not cluster_name or not project_id:
            return Response({"error": "Cluster name and project ID are required parameters."}, status=status.HTTP_400_BAD_REQUEST)
 
        existing_cluster = Cluster.objects.filter( cluster_name=cluster_name).exists()
 
        if existing_cluster:
            return Response({"exists": True}, status=status.HTTP_200_OK)
        else:
            return Response({"exists": False}, status=status.HTTP_200_OK)
   
    
    def get_pipeline_status(self, request):
        global pipeline_dict
        
        # users = {}
        user_id = request.data.get('user_id')
        project_ID = request.data.get('project_id')
        cluster_name = request.data.get('cluster_name')
        cluster_type = request.data.get('cluster_type')
        postgres_version = request.data.get('postgres_version')
        provider_name = request.data.get('provider_name')
        
        # user_id = request.query_params.get('user_id')

        user_id = str(user_id) 
        pipeline_id = pipeline_dict.get(user_id)[0]
        
        # Replace these variables with your actual GitLab project ID and private token
        project_id = os.getenv('PROJECT_ID')
        private_token = os.getenv('PRIVATE_TOKEN')
        base_url = os.getenv('BASE_URL')
  
        headers = {"PRIVATE-TOKEN": private_token}
        # pipeline_count = 1
        artifacts = None
        pipeline_status = get_latest_pipeline_statuses(base_url, project_id, headers, pipeline_id)
        if(pipeline_status == 'success' or pipeline_status == 'failed'):
            del pipeline_dict[user_id]
        artifacts = get_latest_pipeline_artifacts(base_url, project_id, headers, pipeline_id, cluster_name, cluster_type, postgres_version, provider_name,user_id,project_ID)
        
        return JsonResponse({"status": pipeline_status, "artifacts": artifacts})
    
        # Get the statuses of the latest pipelines
        # latest_pipeline_statuses = get_latest_pipeline_statuses(base_url, project_id, headers, pipeline_count)
 
        # # Get the artifacts for each of the latest pipelines
        # all_artifacts = []
        # for pipeline_status in latest_pipeline_statuses:
        #     pipeline_id = pipeline_status["id"]
        #     artifacts = get_latest_pipeline_artifacts(base_url, project_id, headers, pipeline_id, clusterName,clusterType,databaseVersion,providerName,userId,projectID)
        #     all_artifacts.append({"status": pipeline_status["status"], "artifacts": artifacts})
 
        # return JsonResponse({"pipelines": all_artifacts})
    
    def get_dele_pipeline_status(self,request):
        global pipeline_dict
                   
        user_id = request.data.get('user_id')
        print(" delete aapi", user_id)
        print(pipeline_dict)
        user_id = str(user_id) 
        pipeline_id = pipeline_dict.get(user_id)[0]
        
        # Replace these variables with your actual GitLab project ID and private token
        project_id = os.getenv('PROJECT_ID')
        private_token = os.getenv('PRIVATE_TOKEN')
        base_url = os.getenv('BASE_URL')
  
        headers = {"PRIVATE-TOKEN": private_token}
        
        pipeline_status = get_latest_pipeline_statuses(base_url, project_id, headers, pipeline_id)
        if(pipeline_status == 'success' or pipeline_status == 'failed'):
            del pipeline_dict[user_id]
        
        return JsonResponse({"status": pipeline_status})
    

# Define a logger for cluster-related actions
deletecluster_logger = logging.getLogger('deletecluster_logger')    
 
class ClusterDeleteViewSet(viewsets.ModelViewSet):
   
    def create(self , request, *args, **kwargs):
        
        deleteCluster_name   = request.data.get('cluster_name')
        provider_name = request.data.get('provider_name')
        provider_endpoint = request.data.get('provider_endpoint')
        accessKey = request.data.get('provider_access_token')
        provider_secret_key = request.data.get('provider_secret_key')
        kubeconfig_data = request.data.get('kubeconfig_data')
        user_id = request.data.get('user_id')
 
        try:
             # Check if the cluster exists in the database
            cluster = Cluster.objects.get(cluster_name=deleteCluster_name )
            
            # Log delete cluster information
            log_entry = f"user={cluster.user.username} clusterName={cluster.cluster_name} msg={cluster.cluster_name} deleted"
            deletecluster_logger.info(log_entry)
            
            # Delete the cluster from the databas
            project_id = os.getenv('PROJECT_ID')
            private_token = os.getenv('PRIVATE_TOKEN')
            base_url = os.getenv('BASE_URL')
 
            headers = {"PRIVATE-TOKEN" : private_token}
            
            if provider_name == 'Kubernetes':
                branch_name = 'destroy-postgres-k8s'
            else:
                branch_name = 'destroy' 

            formData = {
                "ref": branch_name,
                "variables": [
                {"key": "DATABASE_NAME", "value": deleteCluster_name},
                {"key": "PROVIDER_ENDPOINT", "value": provider_endpoint},
                {"key": "PROVIDER_SECRET_KEY", "value": provider_secret_key},
                {"key": "PROVIDER_ACCESS_KEY", "value": accessKey},
                {"key": "KUBE_CONFIG", "value": kubeconfig_data}         
             ]
            }
            
            response = trigger_single(base_url, project_id, headers,user_id, formData)
 
            if response == 200:
                cluster.delete()
                return Response({"message": "Destroy pipeline triggered successfully."},
                                status=status.HTTP_200_OK)
            else:
                return Response({"error": "Failed to trigger Destroy pipeline."},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Cluster.DoesNotExist:
            return Response({"error": "Cluster not found."},
                            status=status.HTTP_404_NOT_FOUND)
 
pipeline_dict = {}

def trigger_single(base_url, project_id, headers, user_id, formData):
    global pipeline_dict
        
    print(pipeline_dict)
    response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=formData,
                             verify=False)
    if response.status_code != 201:
        return {"error": f"Failed to create cluster. Status code: {response.status_code}"}
 
    pipeline_id = response.json().get("id")
    # Update pipeline_dict with user_id and pipeline_id
    if user_id in pipeline_dict:
        pipeline_dict[user_id].append(pipeline_id)
    else:
        pipeline_dict[user_id] = [pipeline_id]

    pipeline_status = "pending"
 
 
    while pipeline_status in ["pending", "running"]:
        time.sleep(1)
 
        pipeline_info_response = requests.get(base_url + f"projects/{project_id}/pipelines/{pipeline_id}",
                                              headers=headers, verify=False)
        pipeline_info = pipeline_info_response.json()
        pipeline_status = pipeline_info.get("status")
 
    if pipeline_status == "success":
        return 200
    else:
        return {"error": f"Pipeline failed with status: {pipeline_status}"}

def get_key_from_value(pipeline_dict, value):
    for key, values in pipeline_dict.items():
        if value in values:
            return key
    return None    
 
 
def get_latest_pipeline_statuses(base_url, project_id, headers, pipeline_id):
    response = requests.get(base_url + f"projects/{project_id}/pipelines/{pipeline_id}", headers=headers, verify=False)
 
    if response.status_code != 200:
        raise ValueError(f"Error fetching pipeline status: {response.status_code}, {response.json()}")
 
    pipeline_data = response.json()
    status = pipeline_data.get('status')
 
    return status


def get_latest_pipeline_artifacts(base_url, project_id, headers, pipeline_id, clusterName,clusterType,databaseVersion,providerName,userId,usr_project_Id):
    
    user = User.objects.get(pk=userId)
    
    project = Project.objects.get(pk=usr_project_Id)
    
    response = requests.get(base_url + f"projects/{project_id}/pipelines/{pipeline_id}/jobs", headers=headers, verify=False)
    if response.status_code != 200:
        raise ValueError(f"Error fetching pipeline jobs: {response.status_code}, {response.json()}")
 
    jobs = response.json()
    artifacts = []
    for job in jobs:
        response = requests.get(base_url + f"projects/{project_id}/jobs/{job['id']}/artifacts", headers=headers, verify=False)
        if response.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_file:
                # Modify the following to fetch the required artifacts
                required_artifacts = ['info.txt']
                for artifact_name in required_artifacts:
                    if artifact_name in zip_file.namelist():
                        content = zip_file.read(artifact_name).decode('utf-8')
                        artifacts.append({"filename": artifact_name, "content": content})
                     
                        existing_artifact = Db_credentials.objects.filter(
                            pipeline_id=pipeline_id,
                            filename=artifact_name
                        ).first()
 
                        if existing_artifact:
                            # Update the content of the existing artifact
                            existing_artifact.content = content
                            existing_artifact.save()
                        else:
                            # Create a new Db_credentials instance and save it to the database
                            artifact = Db_credentials(
                                user = user,
                                project = project,
                                cluster_name = clusterName,
                                cluster_type = clusterType,
                                database_version= databaseVersion,
                                provider_name= providerName,
                                pipeline_id=pipeline_id,
                                filename=artifact_name,
                                content=content,
                            )
                            artifact.save()
 
    return artifacts
 
def display_artifacts(request):
    # Retrieve all saved artifacts from the database
    artifacts = Db_credentials.objects.all()
 
    # Prepare a list to hold artifact data
    artifacts_data = []
 
    for artifact in artifacts:
        artifact_data = {
            'clusterName' : artifact.clusterName,
            'pipeline_id': artifact.pipeline_id,
            'filename': artifact.filename,
            'content': artifact.content,
            
        }
        artifacts_data.append(artifact_data)
 
    return JsonResponse({'artifacts': artifacts_data})
 

def extract_host(content):

    import re

    match = re.search(r'Host:\s*([\d\.]+)', content)

    if match:

        return match.group(1)

    return None

def display_clusters(request):

    clusters = Db_credentials.objects.all()

    # Prepare a list to hold cluster data

    clusters_data = []

    for cluster in clusters:

        cluster_data = {

            'targets': [f"{extract_host(cluster.content)}:9187"],

            'labels':{

            'instance': cluster.cluster_name,

            'cluster_type': cluster.cluster_type,

            'database_version': cluster.database_version,
            'user': cluster.user.username,
            'project': cluster.project.project_name,

            # 'provider': cluster.provider,

            }}

        clusters_data.append(cluster_data)

    result_data = clusters_data

    return JsonResponse(result_data,safe=False)

 
from .serializers import ClusterSerializers
@api_view(['GET'])
def get_clusters_details(request):
    clusters = Cluster.objects.filter(user_id=user_id)
    serializer = ClusterSerializers(clusters, many=True)
    return Response(serializer.data)
 
 
@api_view(['GET'])
def get_clusters_by_user(request, user_id):
    clusters = Cluster.objects.filter(user_id=user_id)
    serializer = ClusterSerializers(clusters, many=True)
    return Response(serializer.data)
 
 
@api_view(['GET'])
def get_clusters_by_project(request, project_id):
    clusters = Cluster.objects.filter(project_id=project_id)
    serializer = ClusterSerializers(clusters, many=True)
    return Response(serializer.data)
 
 
from rest_framework import generics
from rest_framework.response import Response
from .models import Db_credentials
from .serializers import DbcredentialsSerializer
from django.shortcuts import get_object_or_404 
 
class ContentByClusterNameView(generics.ListAPIView):
    serializer_class = DbcredentialsSerializer
 
    def get_queryset(self):
        cluster_name = self.kwargs['cluster_name']
        username = self.kwargs['username']
 
        user = get_object_or_404(User, username=username)
 
        # Get the provider based on the user and provider name
        # provider = get_object_or_404(Provider, user_id=user.id, cluster_name=cluster_name)
        return Db_credentials.objects.filter(cluster_name=cluster_name, user_id = user.id )
    
class ContentByClusterName(generics.ListAPIView):
    serializer_class = DbcredentialsSerializer
 
    def get_queryset(self):
        cluster_name = self.kwargs['cluster_name']
        # username = self.kwargs['username']

        # user = get_object_or_404(User, username=username)

        # Get the provider based on the user and provider name
        # provider = get_object_or_404(Provider, user_id=user.id, cluster_name=cluster_name)
        return Db_credentials.objects.filter(cluster_name=cluster_name )
          
 
@api_view(['GET'])
def get_backup_method_by_cluster_name(request, cluster_name):
    try:
        cluster = Cluster.objects.get(cluster_name=cluster_name)
        backup_method = cluster.backup_method
        return Response({'backup_method': backup_method}, status=status.HTTP_200_OK)
    except Cluster.DoesNotExist:
        return Response({'error': 'Cluster not found'}, status=status.HTTP_404_NOT_FOUND) 