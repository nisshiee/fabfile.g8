# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.contrib.files import *

@task
def install():
    sudo('yum -y --enablerepo=remi install mysql-server')

@task
def config():
    upload_template(
        'fabfile/common/templates/my.cnf',
        '/etc/my.cnf',
        context = {
            'buffer_pool_size': env.MYSQL_BUFFER_POOL_SIZE
        },
        use_sudo = True,
        use_jinja = True,
        mode = 0644
    )
    sudo('chown root.root /etc/my.cnf')

@task
def chkconfig():
    sudo('chkconfig mysqld on')

@task
def restart():
    sudo('service mysqld restart')

@task
def adduser():
    run('mysql -u root -e "grant all on *.* to \'%s\'@\'localhost\' identified by \'%s\';"' % (env.MYSQL_USER_NAME, env.MYSQL_USER_PASSWORD))
    run('mysql -u root -e "revoke super on *.* from \'%s\'@\'localhost\';"' % env.MYSQL_USER_NAME)
    run('mysql -u root -e "grant all on *.* to \'%s\'@\'%%\' identified by \'%s\';"' % (env.MYSQL_USER_NAME, env.MYSQL_USER_PASSWORD))
    run('mysql -u root -e "revoke super on *.* from \'%s\'@\'%%\';"' % env.MYSQL_USER_NAME)

@task
def create_database():
    run('mysql -u root -e "create database %s character set utf8mb4 collate utf8mb4_general_ci;"' % env.MYSQL_DATABASE_NAME)
