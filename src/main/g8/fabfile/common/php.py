# -*- coding: utf-8 -*-

from fabric.api import *
from fabric.contrib.files import *
import nginx

@task
def install():
    sudo('yum -y --enablerepo=remi install php php-fpm php-devel php-cli php-xml php-mysql php-mbstring php-gd php-xdebug php-pear')

@task
def config():
    sed(
        '/etc/php-fpm.d/www.conf',
        'user *=.*',
        'user = %s' % env.PHP_FPM_RUN_USER,
        use_sudo = True
    )
    sed(
        '/etc/php-fpm.d/www.conf',
        'group *=.*',
        'group = %s' % env.PHP_FPM_RUN_GROUP,
        use_sudo = True
    )

@task
def chkconfig():
    sudo('chkconfig php-fpm on')

@task
def restart():
    sudo('service php-fpm restart')

@task
def nginx_config():
    upload_template(
        'fabfile/common/templates/nginx.site.conf',
        '/etc/nginx/conf.d/%s.conf' % env.NGINX_PHP_VHOST,
        context = {
            'vhost': env.NGINX_PHP_VHOST,
            'docroot': env.NGINX_PHP_DOCROOT,
            'fuel_env': env.FUEL_ENV
        },
        use_sudo = True,
        use_jinja = True,
        mode = 0644
    )
    sudo('chown root.root /etc/nginx/conf.d/%s.conf' % env.NGINX_PHP_VHOST)
    sudo('mkdir -p /var/log/nginx/%s/' % env.NGINX_PHP_VHOST)
    sudo('chown nginx.nginx /var/log/nginx/%s/' % env.NGINX_PHP_VHOST)
    sudo('chmod 755 /var/log/nginx/%s/' % env.NGINX_PHP_VHOST)
    nginx._restart()

@task
def add_local_hosts():
    local('sudo sh -c "echo %s %s >> /etc/hosts"' % (env.NGINX_PHP_LOCAL_HOSTS, env.NGINX_PHP_VHOST))
