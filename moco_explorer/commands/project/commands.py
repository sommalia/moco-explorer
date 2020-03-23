import click


@click.group()
@click.pass_context
def project(ctx):
    pass


@project.command()
@click.pass_context
def getlist(ctx):
    moco = ctx.obj["moco"]
    formatter = ctx.obj["format"]

    items_list = moco.Project.getlist().items

    formatter.format_list(items_list)


@project.command()
@click.pass_context
def get(ctx):
    pass
