from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django_cron import CronJobBase, Schedule
# from django_cron import CronJobManager
# from crontab import CronTab
import subprocess
import json
import os
from django.views.decorators.csrf import csrf_exempt
from crontab import CronTab

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

@api_view(['POST'])
def create_backup(request):
    server_name = request.query_params.get('server_name')
    backup_name = request.query_params.get('backup_name')
    storage_method = request.query_params.get('storage_method')

    if not server_name:
        return Response({'status': 'error', 'message': 'Server name is required.'}, status=status.HTTP_400_BAD_REQUEST)

    command = ['barman', 'backup', server_name]
    if backup_name:
        command.extend(['--name', backup_name])

    return Response(execute_command(command, storage_method))

@api_view(['POST'])
def switch_wal(request):
    server_name = request.query_params.get('server_name')
    storage_method = request.query_params.get('storage_method')

    if not server_name:
        return Response({'status': 'error', 'message': 'Server name is required.'}, status=status.HTTP_400_BAD_REQUEST)

    command = ['barman', 'switch-wal', '--force', '--archive', server_name]

    return Response(execute_command(command, storage_method))

@api_view(['POST'])
def recover_backup(request):
    server_name = request.query_params.get('server_name')
    backup_id = request.query_params.get('backup_id')
    destination_directory = request.query_params.get('destination_directory')
    target_server_name = request.query_params.get('target_server_name')
    storage_method = request.query_params.get('storage_method')

    if not (server_name, backup_id, destination_directory, target_server_name):
        return Response({'status': 'error', 'message': 'All parameters are required.'}, status=status.HTTP_400_BAD_REQUEST)

    command = ['barman', 'recover', '--remote-ssh-command', f'ssh postgres@{target_server_name}',
               server_name, backup_id, destination_directory]

    return Response(execute_command(command, storage_method))

@csrf_exempt
@api_view(['POST'])
def schedule_backup(request):
    server_name = request.query_params.get('server_name')
    storage_method = request.query_params.get('storage_method')
    retention_str = request.query_params.get('retention')  

    if not (server_name, storage_method, retention_str):
        return JsonResponse({'status': 'error', 'message': 'All parameters are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        cron = CronTab(user=True)

        # Check if a cron job already exists for the specified server
        for job in cron:
            command = job.command
            if command.startswith('barman') and server_name in command:
                return Response({'status': 'error', 'message': f'A cron job already exists for server "{server_name}".'}, status=400)

        # Proceed with scheduling the backup if no existing cron job found
        config_file_path = os.path.join(CONFIG_DIR, f'{server_name}.conf')
        with open(config_file_path, 'a') as config_file:
            for retention in retention_str.split('\n'):
                print(retention)
                if retention and retention != '-1':  # Skip if retention is -1
                    value, unit = int(retention[:-1]), retention[-1]
                    print(value, unit)
                    if unit == 'd':
                        server_config = f"retention_policy = RECOVERY WINDOW OF {value} DAYS\n"
                    elif unit == 'm':
                        server_config = f"retention_policy = RECOVERY WINDOW OF {value} MONTHS\n"
                    elif unit == 'y':
                        server_config = f"retention_policy = RECOVERY WINDOW OF {value} YEARS\n"
                    config_file.write(server_config)

        config_file = f'/etc/barman-{storage_method}.conf'
        command = f'barman -c {config_file} backup {server_name}'

        job = cron.new(command=command)
        job.minute.on(0)  # Run at minute 0
        job.hour.on(0)    # Run at hour 0 (midnight)
        cron.write()

        return Response({'status': 'success', 'message': 'Backup scheduled for midnight.'}, status=200)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=500)

@api_view(['GET'])
def get_scheduled_servers(request):
    try:
        cron = CronTab(user=True)
        scheduled_servers = []

        # Iterate over all cron jobs to find scheduled servers
        for job in cron:
            command = job.command
            if command.startswith('barman') and 'backup' in command:
                parts = command.split()
                server_name_index = parts.index('backup') + 1
                if server_name_index < len(parts):
                    server_name = parts[server_name_index]
                    scheduled_servers.append(server_name)

        # Now, iterate over scheduled servers to find retention period
        servers_with_retention = []
        for server_name in scheduled_servers:
            retention_period = None
            config_file_path = os.path.join(CONFIG_DIR, f'{server_name}.conf')
            if os.path.exists(config_file_path):
                with open(config_file_path, 'r') as config_file:
                    for line in config_file:
                        if line.startswith('retention_policy'):
                            retention_period = line.split('=')[-1].strip()[18:]  # Extract retention days
                            break
            servers_with_retention.append({'server_name': server_name, 'retention_period': retention_period})

        return Response({'status': 'success', 'message': servers_with_retention}, status=200)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=500)

@api_view(['POST'])
def update_scheduled_backup(request):
    try:
        server_name = request.query_params.get('server_name')
        storage_method = request.query_params.get('storage_method')
        retention_str = request.query_params.get('retention')
        remove_job = request.query_params.get('remove_job')
        print(retention_str)

        if not (server_name, storage_method):
            return Response({'status': 'error', 'message': 'Server name and storage method are required.'}, status=400)

        config_file_path = os.path.join(CONFIG_DIR, f'{server_name}.conf')
        retention_policy_line = "retention_policy"

        if remove_job == 'true':
            cron = CronTab(user=True)
            # Remove existing cron jobs for the specified server
            for job in cron:
                command = job.command
                if command.startswith('barman') and server_name in command:
                    cron.remove(job)

            with open(config_file_path, 'r') as config_file:
                lines = config_file.readlines()

            with open(config_file_path, 'w') as config_file:
                for line in lines:
                    # Check if the line is not a retention policy line
                    if not line.startswith(retention_policy_line):
                        config_file.write(line)

            cron.write()
            return Response({'status': 'success', 'message': 'Scheduled backup removed successfully.'}, status=200)

        if retention_str == '-1':
            with open(config_file_path, 'r') as config_file:
                lines = config_file.readlines()

            with open(config_file_path, 'w') as config_file:
                for line in lines:
                    # Check if the line is not a retention policy line
                    if not line.startswith(retention_policy_line):
                        config_file.write(line)
            return Response({'status': 'success', 'message': 'Retention period disabled successfully.'}, status=200)

        else:
            with open(config_file_path, 'r') as config_file:
                lines = config_file.readlines()

            # Open the file in write mode to update retention policy
            with open(config_file_path, 'w') as config_file:
                # Flag to check if retention policy is updated
                retention_updated = False
                for line in lines:
                    if line.startswith('retention_policy'):
                        # Update the existing retention policy with new values
                        retention_policy = []
                        for retention in retention_str.split('\n'):
                            if retention:
                                value, unit = int(retention[:-1]), retention[-1]
                                if unit == 'd':
                                    retention_policy.append(f"RECOVERY WINDOW OF {value} DAYS")
                                elif unit == 'm':
                                    retention_policy.append(f"RECOVERY WINDOW OF {value} MONTHS")
                                elif unit == 'y':
                                    retention_policy.append(f"RECOVERY WINDOW OF {value} YEARS")
                        # Write the updated retention policy to the file
                        config_file.write(f"retention_policy = {' AND '.join(retention_policy)}\n")
                        retention_updated = True
                    else:
                        # Write other lines back to the file
                        config_file.write(line)

                # If retention policy is not updated, add a new one
                if not retention_updated:
                    retention_policy = []
                    for retention in retention_str.split('\n'):
                        if retention:
                            value, unit = int(retention[:-1]), retention[-1]
                            if unit == 'd':
                                retention_policy.append(f"RECOVERY WINDOW OF {value} DAYS")
                            elif unit == 'm':
                                retention_policy.append(f"RECOVERY WINDOW OF {value} MONTHS")
                            elif unit == 'y':
                                retention_policy.append(f"RECOVERY WINDOW OF {value} YEARS")
                    # Write the new retention policy to the file
                    config_file.write(f"retention_policy = {' AND '.join(retention_policy)}\n")

            return Response({'status': 'success', 'message': 'Retention period updated successfully.'}, status=200)

    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=500)

@api_view(['POST'])
def add_server_config(request):
    try:
        # Get server details from request parameters
        server_name = request.query_params.get('server_name')
        ssh_host = request.query_params.get('ssh_host')
        db_name = request.query_params.get('db_name')
        db_pass = request.query_params.get('db_pass')
        ssh_key = request.query_params.get('ssh_key')
        storage_method = request.query_params.get('storage_method')

        if not (server_name, ssh_host, db_name, db_pass, ssh_key, storage_method):
            return Response({'status': 'error', 'message': 'All parameters are required.'}, status=400)

        # Construct the configuration file content
        config_content = f"""
[{server_name}]
description = "Configuration for {server_name} server"
ssh_command = ssh postgres@{ssh_host}
conninfo = host={ssh_host} user=barman dbname={db_name}
backup_method = rsync
archiver = on
backup_options = concurrent_backup
"""

        # Write the configuration content to a new file
        config_file_path = os.path.join(CONFIG_DIR, f'{server_name}.conf')
        with open(config_file_path, 'w') as config_file:
            config_file.write(config_content)

        # Append the new entry to the .pgpass file
        with open(PGPASS_FILE, 'a') as pgpass_file:
            pgpass_file.write(f"{ssh_host}:5432:postgres:barman:{db_pass}\n")

        # Append public key
        with open(AUTH_KEYS_FILE, 'a') as f:
            f.write(ssh_key + '\n')

        return Response({'status': 'success', 'message': f'Configuration file created for {server_name}'}, status=200)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=500)