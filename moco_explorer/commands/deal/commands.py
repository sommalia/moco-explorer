import click
from moco_wrapper.models.deal import DealStatus


@click.group()
@click.pass_context
def deal(ctx):
    pass


@deal.command(help="Retrieve a single deal object")
@click.argument("deal-id", type=int)
@click.pass_context
def get(ctx, deal_id):
    """
    Retrieve a single deal object

    :param ctx: click context
    :param deal_id: deal id
    :return: formatted deal object
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    deal_obj = moco.Deal.get(deal_id)
    formatter.format_single(deal_obj.data)


@deal.command(help="Retrieve a list of deal objects")
@click.option("--status", type=click.Choice([e.value for e in DealStatus]))
@click.option("-p", "--page", help="Page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, status, page, retrieve_all):
    """
    Retrieve a list of deal objects

    :param ctx: click context
    :param status: deal status
    :param page: page number
    :param retrieve_all: flag to retrieve all objects from the system (ignores page option)
    :return: formatted list of deal objects
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.Deal.getlist(page=next_page, status=status)

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Deal.getlist(page=page, status=status)
        formatter.format_list(items_list.items)
