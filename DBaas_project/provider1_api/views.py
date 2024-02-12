from rest_framework import viewsets,status
from .models import Provider
from .serializers import ProviderSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    
    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        provider_name = request.data.get('provider_name')
        Key_name = request.data.get('key_name')
        provider_url = request.data.get('provider_url')
        secret_key = request.data.get('secret_key')
        access_token = request.data.get('access_token')
        kubeconfig_data = request.data.get('kubeconfig_data')
        
        # Check if the provider with the same URL exists for this user
        existing_provider = Provider.objects.filter(provider_name=provider_name, user_id=user_id).first()
 
        if existing_provider:
            # Update the existing provider
            existing_provider.provider_name = provider_name
            existing_provider.Key_name = Key_name
            existing_provider.secret_key = secret_key
            existing_provider.access_token = access_token
            existing_provider.kubeconfig_data = kubeconfig_data
            existing_provider.is_connected = True  # Assuming connection is successful
            existing_provider.save()
 
            serializer = ProviderSerializer(existing_provider)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Create a new provider
            provider = Provider(
                user_id=user_id,
                provider_name=provider_name,
                Key_name=Key_name,
                provider_url=provider_url,
                secret_key=secret_key,
                access_token=access_token,
                kubeconfig_data=kubeconfig_data,
                is_connected=True
            )
            provider.save()
 
            serializer = ProviderSerializer(provider)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    def get_provider_by_name(self, request, provider_name):
        provider = get_object_or_404(Provider, provider_name=provider_name)
        serializer = ProviderSerializer(provider)
        return Response(serializer.data)

    def get_provider_by_user_id(self, request, user_id):
        providers = Provider.objects.filter(user_id=user_id, is_connected=True)
        serializer = ProviderSerializer(providers, many=True)
        return Response(serializer.data)

    def get_provider_by_username_and_name(self, request, username, provider_name):
        
        user = get_object_or_404(User, username=username)

        # Get the provider based on the user and provider name
        provider = get_object_or_404(Provider, user_id=user.id, provider_name=provider_name)

        serializer = ProviderSerializer(provider)
        return Response(serializer.data)


