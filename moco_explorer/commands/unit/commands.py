import click

@click.group()
@click.pass_context
def unit(ctx):
    pass


@unit.command(help="Retrieve a single unit")
@click.argument("unit-id", type=int)
@click.pass_context
def get(ctx, unit_id):
    """
    Retrieve a single unit

    :param ctx: click context
    :param unit_id: id of the unit
    :return: formatted unit
    """

    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    unit_obj = moco.Unit.get(unit_id)
    formatter.format_single(unit_obj.data)


@unit.command(help="Retrieve a list of units")
@click.option("-p", '--page', type=int)
@click.option("-a", "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, page, retrieve_all):
    """
    Retrieve a list of units

    :param ctx: click context
    :param page: page number
    :param retrieve_all: flag to retrieve all items from the system (ignores page)
    :return: formatted unit list
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.Unit.getlist(
                page=next_page
            )

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Unit.getlist(page=page)
        formatter.format_list(items_list.items)
