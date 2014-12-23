from fabric.api import *
from fabric.contrib.files import sed

@task
def wget_install():
    sudo('yum -y install wget')

@task
def epel():
    run('wget https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm')
    sudo('/bin/rpm -Uvh epel-release-6-8.noarch.rpm')

@task
def remi():
    run('wget http://rpms.famillecollet.com/enterprise/remi-release-6.rpm')
    sudo('rpm -Uvh remi-release-6.rpm')

@task
def set_timezone():
    sudo('cp -p /etc/localtime /etc/localtime.org')
    sudo('cp -p /usr/share/zoneinfo/Asia/Tokyo /etc/localtime')

@task
def set_locale():
    sed(
        '/etc/sysconfig/i18n',
        'LANG=.*',
        'LANG="ja_JP.UTF-8"',
        use_sudo = True
    )

@task
def jq_install():
    run('wget http://stedolan.github.io/jq/download/source/jq-1.4.tar.gz')
    run('tar xzf jq-1.4.tar.gz')
    with cd('jq-1.4'):
        run('autoreconf -i || true')
        run('./configure')
        run('make')
        sudo('make install')
