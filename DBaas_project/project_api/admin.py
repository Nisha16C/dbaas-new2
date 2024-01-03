from django.contrib import admin
from .models import Project, Cluster

from .models import DBcredentials
# Register your models here.
admin.site.register(DBcredentials)


# Register your models here.
admin.site.register (Project)
admin.site.register (Cluster)