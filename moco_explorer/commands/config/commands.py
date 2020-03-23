import click
from moco_wrapper import Moco


@click.group()
@click.pass_context
def config(ctx):
    pass


@config.command()
@click.pass_context
def get(ctx):
    configuration = ctx.obj["config"]
    configuration.load()
    click.echo(configuration.config)


@config.command()
@click.option("--skip-auth", is_flag=True)
@click.pass_context
def create(ctx, skip_auth):
    domain = click.prompt("Enter your moco domain")
    email = click.prompt("Enter your moco email")
    password = click.prompt("Enter your moco password", hide_input=True)

    auth = {
        "domain": domain,
        "email": email,
        "password": password
    }

    if not skip_auth:
        moco = Moco(auth=auth)
        moco.authenticate()

        configuration = ctx.obj["config"]
        configuration.create(
            moco.api_key,
            moco.domain
        )
    else:
        configuration = ctx.obj["config"]
        configuration.create_account_auth(email, password, domain)

@config.command()
@click.pass_context
def authenticate(ctx):
    configuration = ctx.obj["config"]
    configuration.load()

    if configuration.needs_authentication:
        auth = {
            "domain" : configuration.get("domain"),
            "email" : configuration.get("email"),
            "password": configuration.get("password")
        }

        moco = Moco(auth=auth)
        moco.authenticate()

        configuration.create(
            moco.api_key,
            moco.domain
        )

        configuration.load()

