from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .models import UserProfile
from .serializers import UserProfileSerializer
import random
import string
from project_api .models import Project 
from project_api.serializers import projectSerializers 

from .serializers import userAuthSerializers

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
            serializer= projectSerializers(project)
            return Response({"message": "user created a default project"})

        except Exception as e:
            return Response({"error": f"Failed to create user: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def create(self, request, *args, **kwargs):
        user_data = request.data.get('user') 
        user_serializer = userAuthSerializers(data=user_data)
        
        if user_serializer.is_valid():
            user = user_serializer.save()
            request.data['user'] = user.id
            return super(UserProfileViewSet, self).create(request, *args, **kwargs)
        
        return Response({'error': 'Invalid user data'}, status=400)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class LoginViewSet(viewsets.ViewSet):
    def create(self, request):
       
        username_or_email = request.data.get('username_or_email')
        password = request.data.get('password')
        

        if '@' in username_or_email:
            
            user = User.objects.filter(email=username_or_email).first()
        else:
            user = User.objects.filter(username=username_or_email).first()
 
        if user is not None and user.check_password(password):
            # Log the user in
            login(request, user)
 
            serializer = userAuthSerializers(user)
 
            return Response({
                # 'token': token.key,
                'user_data': serializer.data,
            })
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)