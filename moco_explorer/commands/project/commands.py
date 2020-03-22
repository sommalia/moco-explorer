import click


@click.group()
@click.pass_context
def project(ctx):
    pass


@project.command()
@click.pass_context
def getlist(ctx):
    pass


@project.command()
@click.pass_context
def get(ctx):
    pass
