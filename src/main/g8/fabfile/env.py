from fabric.api import task, env

@task
def default():
    env.hosts = [ '$host$' ]
    env.user = '$login_user$'
    env.key_filename = '$login_keyfile$'
