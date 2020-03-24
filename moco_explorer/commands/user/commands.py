import click
from moco_wrapper import Moco

@click.group()
@click.pass_context
def user(ctx):
    pass

@user.command()
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option("--include-archived", help="include archived users", is_flag=True)
@click.option('-a', "--retrieve-all", help="loops over the whole list", is_flag=True)
@click.pass_context
def getlist(ctx, page, include_archived, retrieve_all):
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []
        items_list = moco.User.getlist(page=1, include_archived=include_archived)
        all_items.extend(items_list.items)

        for i in range(2, items_list.last_page + 1):
            items_list = moco.User.getlist(page=i, include_archived=include_archived)
            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.User.getlist(page=page, include_archived=include_archived)
        formatter.format_list(items_list.items)


@user.command()
@click.pass_context
def get(ctx):
    pass
