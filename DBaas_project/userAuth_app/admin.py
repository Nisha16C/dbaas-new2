from django.contrib import admin
from .models import Role,UserRole, LDAPGroup, LDAPGroupMember
# Register your models here.
admin.site.register(Role)
admin.site.register(UserRole)

admin.site.register(LDAPGroup)
admin.site.register(LDAPGroupMember)
