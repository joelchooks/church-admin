from django.core.management import call_command

def my_scheduled_backup():
    try:
        call_command('dbbackup')
    except:
        pass