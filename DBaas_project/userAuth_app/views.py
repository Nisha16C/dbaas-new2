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

from .models import Role, UserRole

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
 
            project_name = self.generate_random_project_name()          

            project= Project(user= user, project_name = project_name) 

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

    queryset = UserRole.objects.all()
 
    def create(self, request, *args, **kwargs):

        # Get user_id and role_names from the request POST data

        user_id = request.data.get('user_id')
        role_names = request.data.get('roles')
 
        try:
            # Retrieve the user
            user = User.objects.get(pk=user_id)
 
            # Start a transaction to ensure atomicity
            with transaction.atomic():
                # Delete existing roles for the user
                UserRole.objects.filter(user=user).delete()

                # Retrieve or create roles
                for role_name in role_names:
                    role, created = Role.objects.get_or_create(name=role_name, defaults={'description': f'Default description for {role_name}'})
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
    



@api_view(['GET'])

def get_user_role(request, user_id):

    try:

            # Retrieve the user

        user = get_object_or_404(User, pk=user_id)
 
            # Retrieve user roles

        user_roles = UserRole.objects.filter(user=user)
 
            # Create a list of user role strings

        user_role_strings = [f"{user.username} - {user_role.role}" for user_role in user_roles]
 
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

    def post(self, request):

        username = request.data.get('username')

        print(username)

        password = request.data.get('password')

        print(password)
 
        user = authenticate(request, username=username, password=password)
 
        if user is not None:

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')  # Specify the authentication backend

            serializer = userAuthSerializers(user)

            return Response({'user_data': serializer.data,})

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
