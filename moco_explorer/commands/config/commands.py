import click

@click.group()
@click.pass_context
def config():
    pass

@config.command()
@click.pass_context
def get():
    pass

@config.command()
@click.pass_context
def create():
    pass



