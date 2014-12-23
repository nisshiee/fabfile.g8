from fabric.api import *
from fabric.contrib.files import *

@task
def repo():
    upload_template(
        'fabfile/common/templates/nginx.repo',
        '/etc/yum.repos.d/nginx.repo',
        use_sudo = True,
        mode = 0644
    )
    sudo('chown root.root /etc/yum.repos.d/nginx.repo')

@task
def install():
    sudo('yum -y install nginx')

@task
def chkconfig():
    sudo('chkconfig nginx on')

@task
def restart():
    _restart()

def _restart():
    sudo('service nginx restart')
