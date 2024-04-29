from django.contrib import admin
# from .models import ActiveDirectorySettings
from .models import ADGroup , ADGroupMember

# Register your models here.


# admin.site.register(ActiveDirectorySettings)

admin.site.register(ADGroup)
admin.site.register(ADGroupMember)