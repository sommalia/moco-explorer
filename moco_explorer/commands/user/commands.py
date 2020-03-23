import click
from moco_wrapper import Moco

@click.group()
@click.pass_context
def user(ctx):
    pass

@user.command()
@click.pass_context
def getlist(ctx):
    pass

@user.command()
@click.pass_context
def get(ctx):
    pass
