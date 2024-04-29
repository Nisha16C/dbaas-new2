from django.db import models

class ADGroup(models.Model):
    name = models.CharField(max_length=100)

class ADGroupMember(models.Model):
    group = models.ForeignKey(ADGroup, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)




 
# class ActiveDirectorySettings(models.Model):
#     # Authentication Provider Info
#     ldap_server_uri = models.CharField(max_length=255)
#     ldap_server_bind_on = models.CharField(max_length=255)
#     server_connection_timeout = models.IntegerField(max_length=255)
    
#     # Service Account Info
#     service_account_dn = models.CharField(max_length=255)
#     service_account_password = models.CharField(max_length=255)
#     default_login_domain = models.CharField(max_length=100)
    
#     # User Search Settings
#     # user_search_base = models.CharField(max_length=255)
#     group_search_base = models.CharField(max_length=255)
    
#     # Customize Schema for Users
#     users_object_class = models.CharField(max_length=100)
#     users_username_attribute = models.CharField(max_length=100)
#     users_login_attribute = models.CharField(max_length=100)
#     users_member_attribute = models.CharField(max_length=100)
#     users_search_attribute = models.CharField(max_length=255)
#     users_search_filter = models.CharField(max_length=255)
#     users_enable_attribute = models.CharField(max_length=100)
#     users_disabled_status_bitmask = models.IntegerField(max_length=255)
    
#     # Customize Schema for Groups
#     groups_object_class = models.CharField(max_length=100)
#     groups_name_attribute = models.CharField(max_length=100)
#     groups_member_user_attribute = models.CharField(max_length=100)
#     groups_search_attribute = models.CharField(max_length=100)
#     groups_search_filter = models.CharField(max_length=255)
#     groups_member_mapping_attribute = models.CharField(max_length=100)
#     groups_dn_attribute = models.CharField(max_length=100)
#     # search_direct_nested = models.BooleanField(default=True)
    
#     username = models.CharField(max_length=100)  # Corresponds to `userData.first_name`
#     password = models.CharField(max_length=255)     # Add more fields as needed
    
#     def __str__(self):
#         return f"Active Directory Settings - {self.id}"
 
 
 
# class LDAPSettings(models.Model):
#     ldap_server_uri = models.CharField(max_length=255)
#     bind_dn = models.CharField(max_length=255)
#     bind_password = models.CharField(max_length=255)
#     group_search = models.CharField(max_length=255)
#     # Add more fields as needed
 
#     def __str__(self):
#         return f"LDAP Settings - {self.id}"
 
