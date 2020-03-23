import click
from moco_wrapper import Moco

@click.group()
@click.pass_context
def config(ctx):
    pass

@config.command()
@click.pass_context
def get(ctx):
    pass

@config.command()
@click.pass_context
def create(ctx):
    domain = click.prompt("Enter your moco domain")
    email = click.prompt("Enter your moco email")
    password = click.prompt("Enter your moco password", hide_input=True)

    auth = {
        "domain": domain,
        "email": email,
        "password": password
    }

    moco = Moco(auth=auth)
    moco.authenticate()

    configuration = ctx.obj["config"]
    configuration.create(
        moco.api_key,
        moco.domain
    )





