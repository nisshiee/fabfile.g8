from fabric.api import task
import env
import common

@task
def setup_all():
    env.default()
    print("Please customize!!: " + __file__)
