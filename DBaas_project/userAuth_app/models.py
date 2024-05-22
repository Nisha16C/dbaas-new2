# models.py
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    # role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
class LDAPGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class LDAPGroupMember(models.Model):
    group = models.ForeignKey(LDAPGroup, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)

    class Meta:
        unique_together = ('group', 'username')

    def __str__(self):
        return f"{self.group} - {self.username}"


 
class GroupRoleAssignment(models.Model):
    group = models.CharField(max_length=100, null=True)  # Storing group name (LDAP group name)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)  # Role assigned to the group
 
    def __str__(self):
        return f"{self.group} - {self.role.name}"        
     
      