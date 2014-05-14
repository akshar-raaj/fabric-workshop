from fabric.api import run, env, cd
from fabric.colors import green
from fabric.context_managers import prefix

import time

env.hosts = ['54.187.97.9']
env.user = 'akshar'

def pull_code():
    print(green('Pulling code'))
    run('git pull')
    print(green('Pulled code'))

def install_requirements():
    print(green('Installing requirements'))
    run('pip install -r requirements.txt')
    print(green('Installed requirements'))

def kill_gunicorn_process():
    print(green('Killing gunicorn'))
    run('kill -9 `cat gunicorn.pid`')
    print(green('Killed gunicorn'))

def start_gunicorn_process():
    print(green('Starting gunicorn'))
    run('gunicorn web_application:application -c gunicorn_cfg.py', pty=False)
    print(green('Started gunicorn'))

def restart_nginx():
    print(green('Starting nginx'))
    run('sudo service nginx restart')
    print(green('Started nginx'))

def deploy():
    code_dir = '~/fabric_bak/fabric-workshop/'
    with(cd(code_dir)):
        with(prefix('source ~/fabric_bak/bin/activate')):
            pull_code()
            install_requirements()
            kill_gunicorn_process()
            time.sleep(10)
            start_gunicorn_process()
            restart_nginx()
