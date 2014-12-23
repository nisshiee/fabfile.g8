from fabric.api import task, env

@task
def default():
    env.hosts = [ '$host$' ]
    env.user = '$login_user$'
    env.key_filename = '$login_keyfile$'

    # ==================== common ====================
    env.MYSQL_BUFFER_POOL_SIZE = '$mysql_buffer_pool_size$'
    env.MYSQL_USER_NAME = '$mysql_user_name$'
    env.MYSQL_USER_PASSWORD = '$mysql_user_password$'
    env.MYSQL_DATABASE_NAME = '$mysql_database_name$'

    env.NGINX_PHP_VHOST = '$nginx_php_vhost$'
    env.NGINX_PHP_DOCROOT = '$nginx_php_docroot$'
    env.NGINX_PHP_LOCAL_HOSTS = '$host$'
    env.PHP_FPM_RUN_USER = '$php_fpm_run_user$'
    env.PHP_FPM_RUN_GROUP = '$php_fpm_run_group$'
    env.FUEL_ENV = '$fuel_env$'
