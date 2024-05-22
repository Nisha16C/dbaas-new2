from rest_framework import generics

from django.contrib.auth.models import User

from rest_framework import viewsets, status

from rest_framework.response import Response

from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate, login

import random

import string

from project_api .models import Project 

from project_api.serializers import projectSerializers 

from rest_framework.views import APIView

from .models import Role, UserRole, GroupRoleAssignment

from .serializers import userAuthSerializers

from django.http import JsonResponse

from django.views.decorators.http import require_POST

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view

import logging

import ldap

from django.conf import settings

from django_auth_ldap.backend import LDAPBackend

from django_auth_ldap.config import GroupOfNamesType, LDAPSearch
from django.db import transaction
from django.contrib.auth.models import Group
 
 
# Create a logger instance

user_creation_logger = logging.getLogger('user_creation_logger')

class UserAuthViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()

    serializer_class = userAuthSerializers
 
    def generate_random_project_name(self):

        static_prefix = "default-"

        adjectives = ['happy', 'colorful', 'creative', 'vibrant', 'sparkling']

        nouns = ['unicorn', 'rainbow', 'garden', 'ocean', 'harmony']
 
        random_adjective = random.choice(adjectives)

        random_noun = random.choice(nouns)
 
        generated_name = f"{static_prefix}{random_adjective}-{random_noun}"
 
        while Project.objects.filter(project_name=generated_name).exists():

            random_adjective = random.choice(adjectives)

            random_noun = random.choice(nouns)

            generated_name = f"{static_prefix}{random_adjective}-{random_noun}"
 
        return generated_name
 
    def create(self, request, *args, **kwargs):

        first_name = request.data.get('first_name')

        username = request.data.get('username')

        email = request.data.get('email')

        password = request.data.get('password')

        cpassword = request.data.get('cpassword')
 
        # if password != cpassword:

        #     return Response({"error": "password mismatch"})
 
        existing_email = User.objects.filter(email=email).exists()

        existing_username = User.objects.filter(username=username).exists()
 
        if existing_username:

            return Response({"username_error": "User with this username already exists"})

        if existing_email:

            return Response({"email_error": "User with this email already exists"})

        try:

            # Create the user

            user = User.objects.create_user(username=username, email=email, first_name=first_name, password=password)
            
            my_group = Group.objects.get(name='Local-users')
            my_group.user_set.add(user)
 
            project_name = self.generate_random_project_name() 
            print("new project_name : ", project_name)         

            project= Project(user= user, project_name = project_name) 
            print("new project assign name : ", project)

            user.save()
            project.save()
            
 
            # Log the user creation event

            log_entry = f"user={user.username} project={project_name} msg={user.username} created"

            user_creation_logger.info(log_entry)
 
            serializer= projectSerializers(project)
 
            

            return Response({"message": "user created a default project"})
 
        except Exception as e:

            return Response({"error": f"Failed to create user: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
 
 
# Create a logger instance
role_assignment_logger = logging.getLogger('role_assignment_logger')

class AddRoleViewset(viewsets.ModelViewSet):
    
    def create(self, request, *args, **kwargs):
        # Get user_id and role_names from the request POST data
        user_id = request.data.get('user_id')
        role_names = request.data.get('roles')
        print("role_names: ", role_names)

        try:
            # Retrieve the user
            user = get_object_or_404(User, pk=user_id)
            print("user : ", user)

            # Start a transaction to ensure atomicity
            with transaction.atomic():
                # Delete existing roles for the user
                UserRole.objects.filter(user=user).delete()

                # Retrieve or create roles
                for role_name in role_names:
                    # Assuming roles are stored in a Role model
                    role, created = Role.objects.get_or_create(name=role_name)
                    # Associate roles with user
                    UserRole.objects.create(user=user, role=role)

                # Log the role assignment event
                log_entry = f"user={user.username} msg=Roles assigned: {', '.join(role_names)}"
                role_assignment_logger.info(log_entry)

            return JsonResponse({'success': True, 'message': 'Roles added successfully'})

        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User does not exist'}, status=404)

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)  

    # def post(self, request, *args, **kwargs):
    #     # Get user_id and role_names from the request POST data
    #     user_id = request.data.get('user_id')
    #     role_names = request.data.get('roles')
    #     print("role_names: ", role_names)

    #     try:
    #         # Retrieve the user
    #         user = get_object_or_404(User, pk=user_id)
    #         print("user : ", user)

    #         # Start a transaction to ensure atomicity
    #         with transaction.atomic():
    #             # Delete existing roles for the user
    #             UserRole.objects.filter(user=user).delete()

    #             # Retrieve or create roles
    #             for role_name in role_names:
    #                 # Assuming roles are stored in a Role model
    #                 role, created = Role.objects.get_or_create(name=role_name)
    #                 # Associate roles with user
    #                 UserRole.objects.create(user=user, role=role)

    #             # Log the role assignment event
    #             log_entry = f"user={user.username} msg=Roles assigned: {', '.join(role_names)}"
    #             role_assignment_logger.info(log_entry)

    #         return JsonResponse({'success': True, 'message': 'Roles added successfully'})

    #     except User.DoesNotExist:
    #         return JsonResponse({'success': False, 'message': 'User does not exist'}, status=404)

    #     except Exception as e:
    #         return JsonResponse({'success': False, 'message': str(e)}, status=500)


@api_view(['GET'])

def get_user_role(request, user_id):

    try:

            # Retrieve the user

        user = get_object_or_404(User, pk=user_id)
        print("user:", user)
            # Retrieve user roles

        user_roles = UserRole.objects.filter(user=user)
        print("user_roles:", user_roles)
 
            # Create a list of user role strings

        user_role_strings = [f"{user.username} - {user_role.role}" for user_role in user_roles]
        print("user_role_strings:",user_role_strings)
 
        return Response({'user_roles': user_role_strings})

    except User.DoesNotExist:

        return Response({'success': False, 'message': 'User does not exist'}, status=404)

    except Exception as e:

        return Response({'success': False, 'message': str(e)}, status=500)
 
# Create a logger instance

login_logger = logging.getLogger('login_logger')

class LoginViewSet(viewsets.ViewSet):

    def create(self, request):

        username_or_email = request.data.get('username_or_email')

        password = request.data.get('password')

        print(username_or_email)

        print(password)

 
        if '@' in username_or_email:

            user = User.objects.filter(email=username_or_email).first()

        else:

            user = User.objects.filter(username=username_or_email).first()

        if user is not None and user.check_password(password):

            # Log the user in

            login(request, user)

            # Log the login event

            log_entry = f"user={user.username} msg=logged in"

            login_logger.info(log_entry)
 


            serializer = userAuthSerializers(user)

            return Response({

                # 'token': token.key,

                'user_data': serializer.data,

            })

        else:

            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
 
    

class LDAPLoginView(APIView):

    def generate_random_project_name(self):
        static_prefix = "default-"
        adjectives = ['happy', 'colorful', 'creative', 'vibrant', 'sparkling']
        nouns = ['unicorn', 'rainbow', 'garden', 'ocean', 'harmony']
        random_adjective = random.choice(adjectives)
        random_noun = random.choice(nouns)
        generated_name = f"{static_prefix}{random_adjective}-{random_noun}"
        while Project.objects.filter(project_name=generated_name).exists():
            random_adjective = random.choice(adjectives)
            random_noun = random.choice(nouns)
            generated_name = f"{static_prefix}{random_adjective}-{random_noun}"
        return generated_name

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            # Check if the user already has a project assigned
            existing_project = Project.objects.filter(user=user).first()

            if existing_project:
                # User already has a project assigned
                project_name = existing_project.project_name
            else:
                # Generate a random project name and assign it to the user
                project_name = self.generate_random_project_name()

                # Create a default role or retrieve an existing one
                # default_role, _ = Role.objects.get_or_create(name='default_role')

                # Assign the default role to the user
                UserRole.objects.get_or_create(user=user)

                # Create a new project and associate it with the user
                Project.objects.create(user=user, project_name=project_name)

            # Log the login event
            log_entry = f"user={user.username} msg=logged in"
            login_logger.info(log_entry)

            # Serialize user data and return response
            serializer = userAuthSerializers(user)
            return Response({'user_data': serializer.data, 'project_name': project_name})

        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



def user_roles_api(request):
    """
    API endpoint to fetch a list of usernames along with their assigned roles.
    """
    try:
        # Query all UserRole objects
        user_roles = UserRole.objects.all()

        # Create a dictionary to store usernames and their assigned roles
        user_role_data = {}

        # Iterate over UserRole objects to populate the dictionary
        for user_role in user_roles:
            # Get the username
            username = user_role.user.username
            print("username", username)
            # Check if the username is already in the dictionary
            if username in user_role_data:
                # If yes, append the role to the existing list of roles
                user_role_data[username].append(user_role.role)
            else:
                # If no, create a new list with the role
                user_role_data[username] = [user_role.role]

        # Return the data as JSON response
        return JsonResponse({'user_roles': user_role_data})

    except Exception as e:
        # If an error occurs, return an error response
        return JsonResponse({'error': str(e)}, status=500)





from .models import LDAPGroup, LDAPGroupMember

import ldap
from django.http import JsonResponse
from .models import LDAPGroup, LDAPGroupMember

def get_ADgroup_users(request):
    try:
        # Establish LDAP connection
        ldap_server_uri = 'ldap://10.0.0.2:389'
        bind_dn = 'CN=Administrator,CN=Users,DC=os3,DC=com'
        bind_password = 'P@33w0rd'
        ldap_connection = ldap.initialize(ldap_server_uri)
        ldap_connection.simple_bind_s(bind_dn, bind_password)

        # Search for all groups
        search_base_groups = 'CN=Users,DC=os3,DC=com'
        search_filter_groups = "(objectClass=group)"
        ldap_groups = ldap_connection.search_s(
            search_base_groups,
            ldap.SCOPE_SUBTREE,
            search_filter_groups,
            ['sAMAccountName', 'member']
        )

        # Iterate over LDAP groups
        for dn, entry in ldap_groups:
            group_name = entry.get('sAMAccountName', [])[0].decode('utf-8')
            print("group_name", group_name)

            # Check if the group already exists in the database
            ldap_group, created = LDAPGroup.objects.get_or_create(name=group_name)

            # Retrieve and save member sAMAccountName
            members = entry.get('member', [])
            for member in members:
                member_dn = member.decode('utf-8')
                # Fetch the member's sAMAccountName
                member_info = ldap_connection.search_s(
                    member_dn,
                    ldap.SCOPE_BASE,
                    '(objectClass=*)',
                    ['sAMAccountName']
                )
                if member_info:
                    member_name = member_info[0][1].get('sAMAccountName', [])[0].decode('utf-8')
                    print("member_name", member_name)
                    # Save group member if not already exists
                    LDAPGroupMember.objects.get_or_create(group=ldap_group, username=member_name)

        return JsonResponse({'message': 'LDAP groups and members saved successfully'})

    except ldap.LDAPError as e:
        return JsonResponse({'error': str(e)}, status=500)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

from django.http import JsonResponse
from .models import LDAPGroup, LDAPGroupMember

# Fetch the Group name and members from django Database  and display in UI

# def list_ad_groups_with_members(request):
#     ad_groups = LDAPGroup.objects.all()
#     groups_data = []

#     for group in ad_groups:
#         members = LDAPGroupMember.objects.filter(group=group).values_list('username', flat=True)
#         groups_data.append({
#             'name': group.name,
#             'members': list(members)
#         })

#     return JsonResponse({'ad_groups': groups_data})

def list_ad_groups_with_members(request):

    try:
        # Establish LDAP connection
        ldap_server_uri = 'ldap://10.0.0.2:389'
        bind_dn = 'CN=Administrator,CN=Users,DC=os3,DC=com'
        bind_password = 'P@33w0rd'
        ldap_connection = ldap.initialize(ldap_server_uri)
        ldap_connection.simple_bind_s(bind_dn, bind_password)

        # Search for all groups
        search_base_groups = 'CN=Users,DC=os3,DC=com'
        search_filter_groups = "(objectClass=group)"
        ldap_groups = ldap_connection.search_s(
            search_base_groups,
            ldap.SCOPE_SUBTREE,
            search_filter_groups,
            ['sAMAccountName', 'member']
        )

        group_info = []

        for dn, entry in ldap_groups:
            group_name = entry.get('sAMAccountName', [])[0].decode('utf-8')
            members = entry.get('member', [])
            member_names = []

            for member in members:
                member_dn = member.decode('utf-8')
                # Fetch the member's sAMAccountName
                member_info = ldap_connection.search_s(
                    member_dn,
                    ldap.SCOPE_BASE,
                    '(objectClass=*)',
                    ['sAMAccountName']
                )
                if member_info:
                    member_name = member_info[0][1].get('sAMAccountName', [])[0].decode('utf-8')
                    member_names.append(member_name)

            group_info.append({
                'group_name': group_name,
                'members': member_names
            })

        return JsonResponse({'groups': group_info}, safe=False)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


from django.contrib.auth.models import User
from .models import Role, UserRole

from django.contrib.auth.models import User

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Role, UserRole, GroupRoleAssignment, LDAPGroup, LDAPGroupMember
from django.contrib.auth.models import User

@api_view(['GET', 'POST'])
def assign_roles_to_group_members(request):
    if request.method == 'POST':
        group_name = request.data.get('group_name')
        role_name = request.data.get('role_name')
        sAMAccountNames = request.data.get('sAMAccountNames')

        if not group_name or not role_name or not sAMAccountNames:
            return Response({'success': False, 'message': 'group_name, role_name, and sAMAccountNames are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Get or create the role object
            role, _ = Role.objects.get_or_create(name=role_name)

            # Find the group object
            group = LDAPGroup.objects.get(name=group_name)

            # Find the group members
            group_members = LDAPGroupMember.objects.filter(group=group)

            # Remove any existing roles associated with the members of the specified group
            for member in group_members:
                user = User.objects.filter(username=member.username).first()
                if user:
                    UserRole.objects.filter(user=user).delete()

            # Assign the new role to each user
            for sAMAccountName in sAMAccountNames:
                user, _ = User.objects.get_or_create(username=sAMAccountName)
                UserRole.objects.create(user=user, role=role)

            # Remove existing GroupRoleAssignment records for the group
            GroupRoleAssignment.objects.filter(group=group.name).delete()

            # Create new GroupRoleAssignment for the group and role
            GroupRoleAssignment.objects.create(group=group.name, role=role)

            return Response({'success': True, 'message': f'Roles assigned to members of {group_name}'})
        except LDAPGroup.DoesNotExist:
            return Response({'success': False, 'message': f'Group {group_name} does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'GET':
        try:
            # Fetch all GroupRoleAssignment objects
            group_assignments = GroupRoleAssignment.objects.all()

            # Prepare the response data
            group_roles_data = {}
            for assignment in group_assignments:
                group_name = assignment.group  # Access group name directly
                role_name = assignment.role.name
                if group_name in group_roles_data:
                    group_roles_data[group_name].append(role_name)
                else:
                    group_roles_data[group_name] = [role_name]

            return JsonResponse({'group_roles': group_roles_data})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




from django.http import JsonResponse
from rest_framework.decorators import api_view
import urllib.parse

@api_view(['GET'])
def get_group_role(request, group_name):
    try:
        # Decode the group name
        decoded_group_name = urllib.parse.unquote(group_name)
        
        # Fetch the GroupRoleAssignment objects for the specified group
        group_assignments = GroupRoleAssignment.objects.filter(group=decoded_group_name)
        
        # If no assignments found, return an appropriate response
        if not group_assignments.exists():
            return JsonResponse({'success': False, 'message': f'No roles found for group {decoded_group_name}'}, status=404)
        
        # Prepare the response data
        role_names = [assignment.role.name for assignment in group_assignments]
        
        return JsonResponse({'success': True, 'group': decoded_group_name, 'roles': role_names})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)




from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

class IsConnectedAPIView(APIView):
    def get(self, request):

        is_connected = settings.IS_CONNNECTED.strip()  # Corrected attribute name and stripping whitespace
        print("is_connected", is_connected)
        return Response({'is_connected': is_connected})