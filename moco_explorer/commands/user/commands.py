import click
from moco_wrapper import Moco

@click.group()
@click.pass_context
def user(ctx):
    pass

@user.command()
@click.pass_context
def getlist(ctx):
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]



@user.command()
@click.pass_context
def get(ctx):
    pass
