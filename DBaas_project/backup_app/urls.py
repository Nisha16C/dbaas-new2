from django.urls import path
from .views import check_server_status, list_backups, list_servers, create_backup, switch_wal, recover_backup, schedule_backup, get_scheduled_servers, update_scheduled_backup, add_server_config, add_nfs_mount, mount_s3_bucket, list_mount_points, unmount, delete_server
 
urlpatterns = [
    path('barman/check', check_server_status),
    path('barman/list-servers', list_servers),
    path('barman/list-backups', list_backups),
    path('barman/backup', create_backup, name='create_backup'),
    path('barman/add-server', add_server_config, name='add_server'),
    path('barman/recover', recover_backup, name='recover_backup'),
    path('barman/switch-wal', switch_wal, name='switch_wal'),
    path('barman/schedule-backup', schedule_backup, name='schedule_backup'),
    path('barman/update-scheduled-backups', update_scheduled_backup, name='update_scheduled_backups'),
    path('barman/get-scheduled-servers', get_scheduled_servers),
    path('barman/mount-nfs', add_nfs_mount),
    path('barman/mount-s3', mount_s3_bucket),
    path('barman/list-mount-points', list_mount_points),
    path('barman/unmount', unmount),
    path('barman/delete-server', unmount),
    # Define other URLs similarly...
]