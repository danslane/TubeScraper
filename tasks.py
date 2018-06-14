from invoke import task, run

@task
def unitTests():
    run('py.test')

@task
def lint():
    patterns = []
    patterns.append('**/*.py')
    for pattern in patterns:
        run('pep8 %s' % pattern)

@task
def clean(bytecode=True):
    patterns = ['build']
    if bytecode:
        patterns.append('**/*.pyc')
    for pattern in patterns:
        run('rm -rf %s' % pattern)

@task(default=True)
def build():
    unitTests()
    lint()
