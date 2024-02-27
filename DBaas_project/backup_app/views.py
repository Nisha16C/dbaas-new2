from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django_cron import CronJobBase, Schedule
# from django_cron import CronJobManager
# from crontab import CronTab
import subprocess
import json
import os

CONFIG_DIR = '/etc/barman.d'
PGPASS_FILE = os.path.join(os.path.expanduser("~barman"), ".pgpass")
AUTH_KEYS_FILE = os.path.join(os.path.expanduser("~barman"), ".ssh/authorized_keys")

def execute_command(command, storage_method):
    try:
        if storage_method not in ['nfs', 's3']:
            return {'status': 'error', 'message': 'Invalid storage method specified.'}

        config_file = f'/etc/barman-{storage_method}.conf'
        command_with_json_format = command[:1] + ['-c', config_file, '--format', 'json'] + command[1:]
        result = subprocess.run(command_with_json_format, capture_output=True, text=True, check=True)
        return {'status': 'success', 'message': json.loads(result.stdout)}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@api_view(['GET'])
def check_server_status(request):
    server_name = request.query_params.get('server_name')
    storage_method = request.query_params.get('storage_method')

    if not server_name:
        return Response({'status': 'error', 'message': 'Server name is required.'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(execute_command(['barman', 'check', server_name], storage_method))

@api_view(['GET'])
def list_servers(request):
    storage_method = request.query_params.get('storage_method')

    if not storage_method:
        return Response({'status': 'error', 'message': 'Storage method is required.'}, status=status.HTTP_400_BAD_REQUEST)

    result = execute_command(['barman', 'list-servers'], storage_method)
    return Response(result)

@api_view(['GET'])
def list_backups(request):
    server_name = request.query_params.get('server_name')
    storage_method = request.query_params.get('storage_method')

    if not server_name:
        return Response({'status': 'error', 'message': 'Server name is required.'}, status=status.HTTP_400_BAD_REQUEST)

    result = execute_command(['barman', 'list-backups', server_name], storage_method)
    return Response(result)