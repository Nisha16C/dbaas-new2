import os

from django.http import JsonResponse

from rest_framework import viewsets

from rest_framework.views import APIView

from rest_framework.decorators import action

from django.conf import settings

from rest_framework import status

from .serializers import UserSerializer

from rest_framework.response import Response

from django.contrib.auth.models import User

from django_auth_ldap.backend import LDAPBackend

from rest_framework.decorators import api_view

from django_auth_ldap.backend import LDAPBackend
from django_auth_ldap.config import GroupOfNamesType, LDAPSearch
import ldap
from django.http import JsonResponse
from django.conf import settings
 
class FormViewSet(viewsets.ViewSet):
    

    def create(self, request):
        print("hello world!!!!")
        try:
            # Extract data from request
            ldap_server_uri = request.data.get('ldapServerURI')
            ldap_server_bind_on = request.data.get('ldapServerBIND_DN')
            ldap_server_bind_password = request.data.get('ldapServerBIND_PASSWORD')
            ldap_group_search = request.data.get('ldapGroupSearch')
            connection_timeout = request.data.get('serverConnectionTimeout')
            ldap_server_Connection_Timeout = int(connection_timeout)
            ldap_server_account_distinguished_name = request.data.get('ServiceAccountDistinguishedName')
            ldap_default_login_domain = request.data.get('DefaultLoginDomain')
            ldap_user_Object_class = request.data.get('userObjectClass')
            ldap_user_username_attribute = request.data.get('usernameAttribute')
            ldap_user_login_attribute = request.data.get('userLoginAttribute')
            ldap_user_member_attribute = request.data.get('userMemberAttribute')
            ldap_user_search_attribute = request.data.get('userSearchAttribute')
            ldap_user_search_filter = request.data.get('userSearchFilter')
            ldap_user_enable_attribute = request.data.get('userEnableAttribute')
            ldap_disabled_Status_Bitmask = request.data.get('disabledStatusBitmask')
            ldap_group_object_class =  request.data.get('groupObjectClass') 
            ldap_group_name_attribute =  request.data.get('groupNameAttribute') 
            ldap_group_member_user_attribute =  request.data.get('groupMemberUserAttribute') 
            ldap_group_search_attribute =  request.data.get('groupSearchAttribute') 
            ldap_group_search_filter =  request.data.get('groupSearchFilter') 
            ldap_group_member_mapping_attribute =  request.data.get('groupMamberMappingAttribute') 
            ldap_group_DN_attribute =  request.data.get('groupDNattribute') 
            ldap_test_username = request.data.get('testUsername')
            ldap_test_password = request.data.get('testPassword')


            

            # Update settings.py dynamically
            with open(os.path.join(settings.BASE_DIR, 'DBaas_project', 'settings.py'), 'r+') as settings_file:
                lines = settings_file.readlines()
                settings_file.seek(0)
                for line in lines:
                    if line.startswith('AUTH_LDAP_SERVER_URI'):
                        line = f"AUTH_LDAP_SERVER_URI = '{ldap_server_uri}'\n"
                    elif line.startswith('AUTH_LDAP_BIND_DN'):
                        line = f"AUTH_LDAP_BIND_DN = '{ldap_server_bind_on}'\n"
                    elif line.startswith('AUTH_LDAP_BIND_PASSWORD'):
                        line = f"AUTH_LDAP_BIND_PASSWORD = '{ldap_server_bind_password}'\n"
                    elif line.startswith('ldapGroupSearch'):
                        line = f"ldapGroupSearch = '{ldap_group_search}  '\n"
                    elif line.startswith('serverConnectionTimeout'):
                        line = f"serverConnectionTimeout = {ldap_server_Connection_Timeout}  \n"
                    elif line.startswith('ServiceAccountDistinguishedName'):
                        line = f"ServiceAccountDistinguishedName = '{ldap_server_account_distinguished_name}  '\n"
                    elif line.startswith('AUTH_LDAP_DEFAULT_DOMAIN'):
                        line = f"AUTH_LDAP_DEFAULT_DOMAIN = '{ldap_default_login_domain}  '\n"
                    elif line.startswith('AUTH_LDAP_DEFAULT_DOMAIN'):
                        line = f"AUTH_LDAP_DEFAULT_DOMAIN = {ldap_disabled_Status_Bitmask}  \n"
                    elif line.startswith('AUTH_LDAP_USER_OBJECT_CLASS'):
                        line = f"AUTH_LDAP_USER_OBJECT_CLASS = '{ldap_user_Object_class}  '\n"
                    elif line.startswith('AUTH_LDAP_USER_USERNAME_ATTR'):
                        line = f"AUTH_LDAP_USER_USERNAME_ATTR = '{ldap_user_username_attribute}  '\n"
                    elif line.startswith('AUTH_LDAP_USER_LOGIN_ATTR'):
                        line = f"AUTH_LDAP_USER_LOGIN_ATTR = '{ldap_user_login_attribute}  '\n"
                    elif line.startswith('AUTH_LDAP_USER_LOGIN_ATTR'):
                        line = f"AUTH_LDAP_USER_LOGIN_ATTR = '{ldap_user_login_attribute}  '\n"
                    elif line.startswith('AUTH_LDAP_USER_MEMBER_ATTR'):
                        line = f"AUTH_LDAP_USER_MEMBER_ATTR = '{ldap_user_member_attribute}  '\n"
                    elif line.startswith('AUTH_LDAP_USER_SEARCH_ATTR'):
                        line = f"AUTH_LDAP_USER_SEARCH_ATTR = '{ldap_user_search_attribute}  '\n"
                    elif line.startswith('AUTH_LDAP_USER_SEARCH_FILTER'):
                        line = f"AUTH_LDAP_USER_SEARCH_FILTER = '{ldap_user_search_filter}  '\n"
                    elif line.startswith('AUTH_LDAP_USER_ENABLE_ATTR'):
                        line = f"AUTH_LDAP_USER_ENABLE_ATTR = '{ldap_user_enable_attribute}  '\n"
                    elif line.startswith('AUTH_LDAP_GROUP_OBJECT_CLASS'):
                        line = f"AUTH_LDAP_GROUP_OBJECT_CLASS = '{ldap_group_object_class}  '\n"
                    elif line.startswith('AUTH_LDAP_GROUP_NAME_ATTR'):
                        line = f"AUTH_LDAP_GROUP_NAME_ATTR = '{ldap_group_name_attribute}  '\n"
                    elif line.startswith('AUTH_LDAP_GROUP_MEMBER_ATTR'):
                        line = f"AUTH_LDAP_GROUP_MEMBER_ATTR = '{ldap_group_member_user_attribute}  '\n"
                    elif line.startswith('AUTH_LDAP_GROUP_SEARCH_ATTR'):
                        line = f"AUTH_LDAP_GROUP_SEARCH_ATTR = '{ldap_group_search_attribute}  '\n"
                    elif line.startswith('AUTH_LDAP_GROUP_SEARCH_FILTER'):
                        line = f"AUTH_LDAP_GROUP_SEARCH_FILTER = '{ldap_group_search_filter}  '\n"
                    elif line.startswith('AUTH_LDAP_GROUP_MEMBER_MAPPING_ATTR'):
                        line = f"AUTH_LDAP_GROUP_MEMBER_MAPPING_ATTR = '{ldap_group_member_mapping_attribute}  '\n"
                    elif line.startswith('AUTH_LDAP_GROUP_DN_ATTR'):
                        line = f"AUTH_LDAP_GROUP_DN_ATTR = '{ldap_group_DN_attribute}  '\n"
                    elif line.startswith('AD_TEST_USERNAME'):
                        line = f"AD_TEST_USERNAME = '{ldap_test_username}  '\n"
                    elif line.startswith('AD_TEST_PASSWORD'):
                        line = f"AD_TEST_PASSWORD = '{ldap_test_password}  '\n"
                    settings_file.write(line)

            # Create an instance of ActiveDirectorySettings model
            # ad_settings = ActiveDirectorySettings(
            #     ldap_server_uri=ldap_server_uri,
            #     ldap_server_bind_on=ldap_server_bind_on,
            #     service_account_password=ldap_server_bind_password,
            #     ldap_group_search=ldap_group_search,
            #     server_connection_timeout=ldap_server_Connection_Timeout,
            #     service_account_dn=ldap_server_account_distinguished_name,
            #     default_login_domain=ldap_default_login_domain,
            #     users_object_class=ldap_user_Object_class,
            #     users_username_attribute=ldap_user_username_attribute,
            #     users_login_attribute=ldap_user_login_attribute,
            #     users_member_attribute=ldap_user_member_attribute,
            #     users_search_attribute=ldap_user_search_attribute,
            #     users_search_filter=ldap_user_search_filter,
            #     users_enable_attribute=ldap_user_enable_attribute,
            #     users_disabled_status_bitmask=ldap_disabled_Status_Bitmask,
            #     groups_object_class=ldap_group_object_class,
            #     groups_name_attribute=ldap_group_name_attribute,
            #     groups_member_user_attribute=ldap_group_member_user_attribute,
            #     groups_search_attribute=ldap_group_search_attribute,
            #     groups_search_filter=ldap_group_search_filter,
            #     groups_member_mapping_attribute=ldap_group_member_mapping_attribute,
            #     groups_dn_attribute=ldap_group_DN_attribute,
            #     username=ldap_test_username,
            #     password=ldap_test_password,
            # )
            # print("ldap_server_uri", ldap_server_uri)
            
            
            # Save the instance
            # ad_settings.save()            
           

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

                settings_file.write("ldapGroupSearch = ''\n")
                settings_file.write("serverConnectionTimeout = ''\n")
                settings_file.write("ServiceAccountDistinguishedName = ''\n")
                settings_file.write("AUTH_LDAP_DEFAULT_DOMAIN = ''\n")
                settings_file.write("AUTH_LDAP_USER_DISABLED_BITMASK = ''\n")

# --------------------------------------------------------- user --------------------------------------------------------------
                settings_file.write("AUTH_LDAP_USER_OBJECT_CLASS = ''\n")
                settings_file.write("AUTH_LDAP_USER_USERNAME_ATTR = ''\n")
                settings_file.write("AUTH_LDAP_USER_SEARCH_ATTR = ''\n")
                settings_file.write("AUTH_LDAP_USER_SEARCH_FILTER = ''\n")
                settings_file.write("AUTH_LDAP_USER_ENABLE_ATTR = ''\n")
                settings_file.write("AUTH_LDAP_USER_LOGIN_ATTR = ''\n")
                settings_file.write("AUTH_LDAP_USER_MEMBER_ATTR = ''\n")

#  ------------------------------------------------------------------------------group ------------------------------------------
                settings_file.write("AUTH_LDAP_GROUP_OBJECT_CLASS = ''\n")
                settings_file.write("AUTH_LDAP_GROUP_NAME_ATTR = ''\n")
                settings_file.write("AUTH_LDAP_GROUP_MEMBER_ATTR = ''\n")
                settings_file.write("AUTH_LDAP_GROUP_SEARCH_ATTR = ''\n")
                settings_file.write("AUTH_LDAP_GROUP_SEARCH_FILTER = ''\n")
                settings_file.write("AUTH_LDAP_GROUP_MEMBER_MAPPING_ATTR = ''\n")
                settings_file.write("AUTH_LDAP_GROUP_DN_ATTR = ''\n")
                settings_file.write("AD_TEST_USERNAME = ''\n")
                settings_file.write("AD_TEST_PASSWORD = ''\n")

                


            return JsonResponse({'message': 'LDAP settings disabled successfully'}, status=200)

        except Exception as e:

            return JsonResponse({'error': str(e)}, status=500)


# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from .models import ActiveDirectorySettings
# from .serializers import LDAPSettingsSerializer
 
# class LDAPSettingsViewSet(viewsets.ViewSet):
#     def create(self, request):
#         serializer = LDAPSettingsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from django.http import JsonResponse

from django_auth_ldap.backend import LDAPBackend

import ldap
 
# def get_ADgroup_users(request):

#     try:

#         # Establish LDAP connection

#         ldap_server_uri = 'ldap://10.0.0.2:389'

#         bind_dn = 'CN=Administrator,CN=Users,DC=os3,DC=com'

#         bind_password = 'P@33w0rd'

#         ldap_connection = ldap.initialize(ldap_server_uri)

#         ldap_connection.simple_bind_s(bind_dn, bind_password)
 
#         search_base = 'CN=Users,DC=os3,DC=com'

#         search_filter = "(sAMAccountName=*)"  # Filter to retrieve all users

#         ldap_users = ldap_connection.search_s(

#             search_base,

#             ldap.SCOPE_SUBTREE,

#             search_filter,

#             ['sAMAccountName']

#         )

#         print("ldap_users:" ,ldap_users)
 
#         # Extract usernames

#         user_names = [entry.get('sAMAccountName', [])[0].decode('utf-8') for dn, entry in ldap_users]
 
#         return JsonResponse({'user_names': user_names}, safe=False)

#     except Exception as e:

#         return JsonResponse({'error': str(e)}, status=500)

def get_ad_users(request):

    try:

        # Establish LDAP connection

        ldap_server_uri = 'ldap://10.0.0.2:389'

        bind_dn = 'CN=Administrator,CN=Users,DC=os3,DC=com'

        bind_password = 'P@33w0rd'

        ldap_connection = ldap.initialize(ldap_server_uri)

        ldap_connection.simple_bind_s(bind_dn, bind_password)
 
        search_base = 'CN=Users,DC=os3,DC=com'

        search_filter = "(sAMAccountName=*)"  # Filter to retrieve all users

        ldap_users = ldap_connection.search_s(

            search_base,

            ldap.SCOPE_SUBTREE,

            search_filter,

            ['sAMAccountName']

        )

        print("ldap_users:" ,ldap_users)
 
        # Extract usernames

        user_names = [entry.get('sAMAccountName', [])[0].decode('utf-8') for dn, entry in ldap_users]
 
        return JsonResponse({'user_names': user_names}, safe=False)

    except Exception as e:

        return JsonResponse({'error': str(e)}, status=500)
 
    

# def get_ADgroup_users(request):
#     try:
#         # Establish LDAP connection
#         ldap_server_uri = 'ldap://10.0.0.2:389'
#         bind_dn = 'CN=Administrator,CN=Users,DC=os3,DC=com'
#         bind_password = 'P@33w0rd'
#         ldap_connection = ldap.initialize(ldap_server_uri)
#         ldap_connection.simple_bind_s(bind_dn, bind_password)

#         # Search base and filter
#         search_base = 'CN=Users,DC=os3,DC=com'
#         search_filter = "(objectClass=user)"  # Filter to retrieve all users

#         # Specify attributes to retrieve
#         attributes = ['sAMAccountName', 'cn']  # You can add more attributes as needed

#         # Search for users
#         ldap_users = ldap_connection.search_s(
#             search_base,
#             ldap.SCOPE_SUBTREE,
#             search_filter,
#             attributes
#         )

#         # Extract user names and DNs
#         user_data = []
#         for dn, entry in ldap_users:
#             user_data.append({
#                 'sAMAccountName': entry.get('sAMAccountName', [])[0].decode('utf-8'),
#                 'cn': entry.get('cn', [])[0].decode('utf-8')
#             })

#         return JsonResponse({'users': user_data}, safe=False)

#     except ldap.LDAPError as e:
#         return JsonResponse({'error': str(e)}, status=500)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)



