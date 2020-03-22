import click


@click.group()
@click.pass_context
def invoice(ctx):
    pass


@invoice.command()
@click.pass_context
def getlist(ctx):
    pass


@invoice.command()
@click.pass_context
def get(ctx):
    pass
