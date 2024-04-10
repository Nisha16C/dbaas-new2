import os

from django.http import JsonResponse

from rest_framework import viewsets

from rest_framework.views import APIView

from rest_framework.decorators import action

from django.conf import settings

from rest_framework import status

from django.contrib.auth.models import User

from .serializers import UserSerializer

from rest_framework.response import Response
 
class FormViewSet(viewsets.ViewSet):

    def create(self, request):

        print('api call')

        ldap_server_uri = request.data.get('ldapServerURI')

        ldap_server_bind_on = request.data.get('ldapServerBIND_DN')

        ldap_server_bind_password = request.data.get('ldapServerBIND_PASSWORD')

        ldap_group_search = request.data.get('ldapGroupSearch')

        print('ldap_group_search', ldap_group_search)
 
        print('ldapServerBIND_PASSWORD :', ldap_server_bind_password)
 
        try:

            # Read the contents of the settings.py file

            with open(settings.BASE_DIR / 'DBaas_project' / 'settings.py', 'r') as settings_file:

                lines = settings_file.readlines()

            # Write the lines back to the settings.py file, updating only the AUTH_LDAP_SERVER_URI variable

            with open(settings.BASE_DIR / 'DBaas_project' / 'settings.py', 'w') as settings_file:

                for line in lines:

                    if line.startswith('AUTH_LDAP_SERVER_URI'):

                        settings_file.write(f"AUTH_LDAP_SERVER_URI = '{ldap_server_uri}'\n")

                    elif line.startswith('AUTH_LDAP_BIND_DN'):

                        settings_file.write(f"AUTH_LDAP_BIND_DN = '{ldap_server_bind_on}'\n")

                    elif line.startswith('AUTH_LDAP_BIND_PASSWORD'):

                        settings_file.write(f"AUTH_LDAP_BIND_PASSWORD = '{ldap_server_bind_password}'\n")

                    # elif line.startswith('AUTH_LDAP_GROUP_SEARCH'):

                    #     settings_file.write(f"AUTH_LDAP_GROUP_SEARCH = ' LDAPSearch("{ldap_group_search}"),ldap.SCOPE_SUBTREE(sAMAccountName=%(user)s) '\n")
 
                    else:

                        settings_file.write(line)

                     # AUTH_LDAP_GROUP_SEARCH = LDAPSearch("CN=Users,DC=os3,DC=com", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
 
            

            return JsonResponse({'message': 'LDAP settings updated successfully'}, status=200)

        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)
 
    def reset_ldap_settings(request):

        try:

            # Update settings.py dynamically

            with open(os.path.join(settings.BASE_DIR, 'DBaas_project', 'settings.py'), 'a') as settings_file:

                settings_file.write("AUTH_LDAP_SERVER_URI = ''\n")

                settings_file.write("AUTH_LDAP_BIND_DN = ''\n")

                settings_file.write("AUTH_LDAP_BIND_PASSWORD = ''\n")

            return JsonResponse({'message': 'LDAP settings disabled successfully'}, status=200)

        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)
 
 
class LDAPAuthenticatedUserListView(APIView):

    def get(self, request):

        # Query users who have logged in using LDAP authentication

        ldap_authenticated_users = User.objects.filter(last_login__isnull=False)

        # Serialize user data

        serializer = UserSerializer(ldap_authenticated_users, many=True)

        # Return serialized data as response

        return Response(serializer.data)
 