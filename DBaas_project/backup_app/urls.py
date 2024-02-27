from django.urls import path
from .views import check_server_status, list_backups, list_servers

urlpatterns = [
    path('barman/check/', check_server_status),
    path('barman/list-servers/', list_servers),
    path('barman/list-backups/', list_backups),
    # Define other URLs similarly...
]