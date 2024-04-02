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
 
# from rest_framework.decorators import action

# Load environment variables from .env file
load_dotenv() 
 
# Define a logger for project-related actions
project_logger = logging.getLogger('project_logger')
rename_project_logger = logging.getLogger('rename_project_logger')
 
 
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = projectSerializers
 
    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        project_name = request.data.get('project_name')
        print (user_id)
        if not user_id:
            return Response({
                "error":"user_id is required "
 
            },status = status.HTTP_400_BAD_REQUEST)
        if not project_name:            
            return Response({
                "error":"project name is required "
 
            },status = status.HTTP_400_BAD_REQUEST)   
 
        existing_project = Project.objects.filter(project_name= project_name).exists()
        print (existing_project)
 
        if existing_project == True:
            return Response({
                "error":"project Already exists"
            },status = status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk= user_id)
            print (user)
            project = Project.objects.create(user=user, project_name=project_name)
 
        except User.DoestNotExist:
            return Response({"error": "User with the provided ID does not exist."},
                            status=status.HTTP_404_NOT_FOUND)
 
        # project= Project(user= user, project_name = project_name)
        project.save()
 
          # Log project creation information with username, project_name, date, and time
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
        # Log information before the project is renamed
        # log_entry_before_rename = f"BeforeProjectRename - User={project.user.username}, ProjectId={project.id}, ProjectName={project.project_name}, msg={ project.project_name } is a old name"
        # rename_project_logger.info(log_entry_before_rename)
 
        project.project_name = new_project_name
        project.save()
 
        # Log information after the project is renamed
        log_entry_after_rename = f"user={project.user.username} projectname={project.project_name} msg={ project.project_name } renamed"
        rename_project_logger.info(log_entry_after_rename)
 
        serializer = projectSerializers(project)
        return Response(serializer.data, status=status.HTTP_200_OK)         
 
# Compute offering
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
        # Define the endpoint of the Cloud, the command that you want to execute, and the keys of the user
        # baseurl = 'http://10.0.0.102:8080/client/api?'
        # request_data = {
        #     'command': 'listServiceOfferings',
        #     'response': 'json',
        #     'apikey': 'i6g5Skzgme-1TdBCWE-ViOiQYSSsZfMahUkJXc-nhJZDHWFE_xQz98-jOqD7elGo7_TGOPvLx0MpalfSuZpidA'
        # }
        # secret_key = 'POJLZ1-QnNVmnkxSwTUHmOqlXTnQY7PXWDYnXEXfEsxXUMzyDGFBaKcV8Bshe9Vg-SMIY0ELE84wU7plndf4fQ'.encode('utf-8')
        baseurl = os.getenv('BASEURL')
        # api_key = os.getenv('API_KEY')

        # Define the request data
        request_data = {
                'command': 'listServiceOfferings',
                'response': 'json',
                'apikey': os.getenv('API_KEY')
        }
        secret_key = os.getenv('SECRET_KEY_ENCODED').encode('utf-8')

            
            
 
        # Build the request string
        request_str = '&'.join(['='.join([k, urllib.parse.quote_plus(request_data[k])]) for k in request_data.keys()])
 
        # Compute the signature with hmac, do a 64-bit encoding, and URL encoding
        sig_str = '&'.join(['='.join([k.lower(), urllib.parse.quote_plus(request_data[k]).lower().replace('+', '%20')])
                            for k in sorted(request_data.keys())])
 
        sig = urllib.parse.quote_plus(
            base64.b64encode(hmac.new(secret_key, sig_str.encode('utf-8'), hashlib.sha1).digest()).
            strip())
 
        req = baseurl + request_str + '&signature=' + sig
 
        # Make the API request
        try:
            res = urllib.request.urlopen(req)
            response_data = json.loads(res.read().decode('utf-8'))
 
            # Extract and return relevant information in JSON format
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
                # 'flavor_id': flavor.id,
                # 'name': flavor.name,
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

# project_id = os.getenv('PROJECT_ID')
# private_token = os.getenv('PRIVATE_TOKEN')
# base_url = os.getenv('BASE_URL')

# print (project_id)
# print(f"{private_token}, token")
# print(f"{base_url}, url") 
   
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
        # global tenant_name 
        global openstackpassword
        # global auth_url
        # global region 
        # global appUser
        
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

        #openstackusernamename = request.data.get ('openStackuser')   
        openstackusername = request.data.get ('openstackusername')
     
        print(f"{openstackusername}, openaaaaaaaaaaaaaaaaa")

        tenant_name = request.data.get ('tenant_name')
        openstackpassword= request.data.get ('openstackPassword')

        print(f"{openstackpassword}, openaaaaaaaaaaaaaaaaa")
        auth_url = request.data.get ('auth_url')
        region = request.data.get ('region')
 
 
        computeOffering  = request.data.get('computeOffering')
        storageOffering = request.data.get('storageOffering')
       
 
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
        print("Config data")
        print(kubeconfig_data)
 
        user = User.objects.get(pk=user_id)
 
        temp_variables = {
            'user': user.username,
            'username': username,
            'password': password,
            'cluster_name': cluster_name,   
            'postgres_version': database_version,
            'backup_method' : backup_method,
            'provider_endpoint': provider_endpoint,
            'provider_access_token ': provider_access_token,
            'provider_secret_key': provider_secret_key,
            'storageOffering': storageOffering,
            'kubeconfig': kubeconfig_data,

            'openstackusername':openstackusername,
            'tenant_name': tenant_name,
            # 'openstackpassword': openstackpassword,
            'auth_url': auth_url,
            'region': region,
 
        }
       
        # Check if cluster with the same name already exists in the project
        existing_cluster = Cluster.objects.filter(project=project_id, cluster_name=cluster_name).exists()
 
        if existing_cluster:
            return Response({"error": "Cluster with the same name already exists in the project"}, status=status.HTTP_400_BAD_REQUEST)
 
        try:
            user = User.objects.get(pk=user_id)
            project = Project.objects.get(pk=project_id)
            # provider = Provider.objects.get(provider_name=provider_name, user=user)
 
        except User.DoesNotExist:
            return Response({"error": "User with the provided ID does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Project.DoesNotExist:
            return Response({"error": "No Project! has been selected.."}, status=status.HTTP_404_NOT_FOUND)
        # except Provider.DoesNotExist:
        #     return Response({"error": "Provider with the provided name does not exist for this user."},
        #                     status=status.HTTP_404_NOT_FOUND)
   
        

        project_id = os.getenv('PROJECT_ID')
        private_token = os.getenv('PRIVATE_TOKEN')
        base_url = os.getenv('BASE_URL')

        print (project_id)
        print(f"{private_token}, token")
        print(f"{base_url}, url")

 
         
        # project_id = "132"
        # private_token = "GDNoxgBaU_vQ_Q6QzjyQ"
        # base_url = "https://gitlab.os3.com/api/v4/"
 
 
        headers = {"PRIVATE-TOKEN": private_token}
        cluster_type1 = False
     
 
 
        if provider_name == 'Kubernetes' and cluster_type == 'Standalone':
            print ("k8s pipeline")
            response = trigger_single(base_url, project_id, headers, 'deploy-postgres-k8s')
            if response == 200:
                print("Cluster save.....")
                cluster = Cluster(
                    user=user,
                    project=project,
                    cluster_name=cluster_name,
                    cluster_type=cluster_type,
                    database_version=database_version,
                    # backup_method=backup_method,
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
            response = trigger_single(base_url, project_id, headers, 'ha-postgres-cluster')
            print("CloudStack ha branch trigger.....")
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
            response = trigger_single(base_url, project_id, headers, 'dummay')
            print("CloudStack ha branch trigger.....")
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
            response = trigger_single(base_url, project_id, headers, 'infra-and-db')
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
            response = trigger_single(base_url, project_id, headers, 'openstack-provider')
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
            response = trigger_single(base_url, project_id, headers, 'openstack-provider-ha')
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
        global clusterName
        global clusterType
        global databaseVersion
        global backupMethod
        global providerName
        global userId
        global projectID
        # global apiEndpoint
        # global accessKey
        # global secretKey
 
        # Replace these variables with your actual GitLab project ID and private token
        project_id = os.getenv('PROJECT_ID')
        private_token = os.getenv('PRIVATE_TOKEN')
        base_url = os.getenv('BASE_URL')
 
 
        headers = {"PRIVATE-TOKEN": private_token}
        pipeline_count = 1
 
        # Get the statuses of the latest pipelines
        latest_pipeline_statuses = get_latest_pipeline_statuses(base_url, project_id, headers, pipeline_count)
 
        # Get the artifacts for each of the latest pipelines
        all_artifacts = []
        for pipeline_status in latest_pipeline_statuses:
            pipeline_id = pipeline_status["id"]
            artifacts = get_latest_pipeline_artifacts(base_url, project_id, headers, pipeline_id, clusterName,clusterType,databaseVersion,providerName,userId,projectID)
            all_artifacts.append({"status": pipeline_status["status"], "artifacts": artifacts})
 
        return JsonResponse({"pipelines": all_artifacts})
  
# Define a logger for cluster-related actions
deletecluster_logger = logging.getLogger('deletecluster_logger')    
 
class ClusterDeleteViewSet(viewsets.ModelViewSet):
   
    def create(self , request, *args, **kwargs):
        global k8s_variables
        global deleteCluster_name
 
        # global clusterName
        # global providerName
        # global apiEndpoint
        global accessKey
        # global secretKey
        deleteCluster_name   = request.data.get('cluster_name')
        # provider_name = request.data.get('provider_name')
        provider_name = request.data.get('provider_name')
        provider_endpoint = request.data.get('provider_endpoint')
        accessKey = request.data.get('provider_access_token')
        provider_secret_key = request.data.get('provider_secret_key')
        kubeconfig_data = request.data.get('kubeconfig_data')
        print (f"{accessKey} and {deleteCluster_name}")
 
        print (kubeconfig_data)
 
 
        k8s_variables = {
            'provider_endpoint' : provider_endpoint,
            'provider_secret_key' : provider_secret_key,
            'provider_name' : provider_name,
            'kubeconfig_data': kubeconfig_data,
        }
        print (k8s_variables)
 
        
 
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
                branch_name = 'destroy'  # Use a different branch name if provider is not 'Kubernetes'
 
            response = trigger_single(base_url, project_id, headers, branch_name)
 
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
 
 
 
def trigger_single(base_url, project_id, headers, branch_name):
    formData = {
        "ref": branch_name,
    }
    # print(formData)
 
    response = requests.post(base_url + f"projects/{project_id}/pipeline", headers=headers, json=formData,
                             verify=False)
 
    if response.status_code != 201:
        return {"error": f"Failed to create cluster. Status code: {response.status_code}"}
 
    pipeline_id = response.json().get("id")
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
   
 
 
# Status fetch function
# Status fetch function
def get_latest_pipeline_statuses(base_url, project_id, headers, count=1):
    response = requests.get(base_url + f"projects/{project_id}/pipelines", headers=headers, verify=False)
 
    if response.status_code != 200:
        raise ValueError(f"Error fetching pipelines: {response.status_code}, {response.json()}")
 
    pipelines = response.json()
    if not pipelines:
        return []
 
    latest_pipelines = pipelines[:count]
    latest_statuses = []
 
    for pipeline in latest_pipelines:
        latest_status = pipeline['status']
        latest_statuses.append({"id": pipeline['id'], "status": latest_status})
 
    return latest_statuses
 
def get_latest_pipeline_artifacts(base_url, project_id, headers, pipeline_id, clusterName,clusterType,databaseVersion,providerName,userId,projectID):
    user = User.objects.get(pk=userId)
    project = Project.objects.get(pk=projectId)
    response = requests.get(base_url + f"projects/{project_id}/pipelines/{pipeline_id}/jobs", headers=headers, verify=False)
    print(f'cluster name artifatcat wale function se {clusterName} and userId {userId} and {clusterType}')
    if response.status_code != 200:
        raise ValueError(f"Error fetching pipeline jobs: {response.status_code}, {response.json()}")
 
    jobs = response.json()
    artifacts = []
    # customer_name = request.POST.get('customer_name', '')
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
                        
                        # Create a new PipelineArtifact instance and save it to the database
                        # Check if an artifact with the same filename and pipeline ID already exists
                        existing_artifact = Db_credentials.objects.filter(
                            pipeline_id=pipeline_id,
                            filename=artifact_name
                        ).first()
 
                        if existing_artifact:
                            # Update the content of the existing artifact
                            existing_artifact.content = content
                            existing_artifact.save()
                        else:
                            print('artifacts save')
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
 
 
 
def get_variables(request):
    global temp_variables
    global accessKey
    global computeOffering
    global openstackpassword
    # global appUser
    
 
    # Your code here, using the retrieved values
    appUser = temp_variables.get('user', '')
    username = temp_variables.get('username', '')
    password = temp_variables.get('password', '')
    cluster_name = temp_variables.get('cluster_name', '')
    postgres_version = temp_variables.get('postgres_version', '')
    backup_method = temp_variables.get('backup_method', '')
    provider_endpoint = temp_variables.get('provider_endpoint','')
    provider_access_token = accessKey
    provider_secret_key = temp_variables.get('provider_secret_key','')
    storageOffering = temp_variables.get('storageOffering', '')
    kubeconfig_data = temp_variables.get('kubeconfig', '')

    openstackusername = temp_variables.get ('openstackusername', '')    
    tenant_name = temp_variables.get ('tenant_name', '')
    openstackpassword= openstackpassword
    auth_url = temp_variables.get ('auth_url', '')
    region = temp_variables.get ('region', '')
   
 
 
    data = {
        'appUser': appUser,
        'dbUser': username,
        'password': password,
        'database_name': cluster_name,
        'postgres_version': postgres_version,
        'backup_method': backup_method,
        
        'endpoint': provider_endpoint,
        'secret-key': provider_secret_key,
        'access-key': provider_access_token,
        'computeOffering': computeOffering,
        'storageOffering': storageOffering,
        'kubeconfig_data': kubeconfig_data,

        'openstackusername':openstackusername,        
        'tenant_name': tenant_name,
        'openstackpassword': openstackpassword,
        'auth_url': auth_url,
        'region': region,

    }
    print(data)
    return JsonResponse(data)
 
def get_dlt_k8s_variables(request):
    global k8s_variables
    global deleteCluster_name
    global accessKey
 
    # global provider_endpoint
 
    # Your code here, using the retrieved values
 
    provider_name = k8s_variables.get('provider_name')
 
    provider_endpoint = k8s_variables.get('provider_endpoint','')
    provider_access_token = accessKey
    provider_secret_key = k8s_variables.get('provider_secret_key','')
    deleteCluster_name = deleteCluster_name
    kubeconfig_data = k8s_variables.get('kubeconfig_data','')
    print(deleteCluster_name)
 
    data = {
      
        'providerName': provider_name,
        'delete-cluster' : deleteCluster_name ,
        'endpoint': provider_endpoint,
        'secret-key': provider_secret_key,
        'access-key': provider_access_token,
        'kubeconfig_data': kubeconfig_data,

        
    }
    print (data)
 
    return JsonResponse(data)    
 
def extract_host(content):
    import re
    match = re.search(r'HOST:\s*([\d\.]+)', content)
    if match:
        return match.group(1)
    return None
 
def display_clusters(request):
    artifacts = Db_credentials.objects.all()
 
    # Prepare a list to hold artifact data
    artifacts_data = []
 
    for artifact in artifacts:
        host_ip = extract_host(artifact.content)
 
    clusters = Cluster.objects.all()
 
    # Prepare a list to hold cluster data
    clusters_data = []
 
    for cluster in clusters:
        cluster_data = {
            'targets': [f"{host_ip}:9187"],
            'labels':{
            'instance': cluster.cluster_name,
            'cluster_type': cluster.cluster_type,
            'database_version': cluster.database_version,
            'provider': cluster.provider,
            }}
        clusters_data.append(cluster_data)
 
    result_data = clusters_data
 
    # Return the combined data as JSON response
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
 
class ContentByClusterNameView(generics.ListAPIView):
    serializer_class = DbcredentialsSerializer
 
    def get_queryset(self):
        cluster_name = self.kwargs['cluster_name']
        return Db_credentials.objects.filter(cluster_name=cluster_name)
        
 
@api_view(['GET'])
def get_backup_method_by_cluster_name(request, cluster_name):
    try:
        cluster = Cluster.objects.get(cluster_name=cluster_name)
        backup_method = cluster.backup_method
        return Response({'backup_method': backup_method}, status=status.HTTP_200_OK)
    except Cluster.DoesNotExist:
        return Response({'error': 'Cluster not found'}, status=status.HTTP_404_NOT_FOUND) 