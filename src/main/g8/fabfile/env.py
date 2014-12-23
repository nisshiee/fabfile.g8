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
