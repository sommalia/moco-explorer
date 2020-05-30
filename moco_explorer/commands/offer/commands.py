import click
from moco_wrapper.models.offer import OfferStatus
from moco_explorer.const import DEFAULT_DATETIME_FORMATS


@click.group()
@click.pass_context
def offer(ctx):
    pass


@offer.command(help="Retrieve single offer")
@click.argument("offer-id", type=int)
@click.pass_context
def get(ctx, offer_id):
    """
    Retrieve a single offer
    :param ctx: click context
    :param offer_id: id of the offer
    :return: formatter offer object
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    offer_item = moco.Offer.get(offer_id)
    formatter.format_single(offer_item.data)


@offer.command(help="Retrieve a list of offers")
@click.option("--status", type=click.Choice([e.value for e in OfferStatus]))
@click.option("--start", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("--end", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("-p", '--page', type=int)
@click.option("-a", "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, status, start, end, page, retrieve_all):
    """
    Retrieve a list of offers

    :param ctx: click context
    :param status: state of the offers
    :param start: start date for the offers
    :param end: end date for the offers
    :param page: page number
    :param retrieve_all: flag to retrieve all items from the system (ignores page option)
    :return: formatted list of offers
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.Offer.getlist(page=next_page, from_date=start, to_date=end, status=status)

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Offer.getlist(page=page, from_date=start, to_date=end, status=status)
        formatter.format_list(items_list.items)
