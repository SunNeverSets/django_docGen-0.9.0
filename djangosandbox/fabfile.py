from fabric import Connection, task

@task
def development(ctx):
    config = Config(overrides={'sudo': {'password': 'c137'}})
    c = Connection('park@165.22.92.197', config=config)
    
@task
def uname(context):
    context.run("dir")