import click
from moco_wrapper.models.offer import OfferStatus
from moco_explorer.const import DEFAULT_DATETIME_FORMATS


@click.group()
@click.pass_context
def offer(ctx):
    pass


@offer.command()
@click.argument("offer-id", type=int)
@click.pass_context
def get(ctx, offer_id):
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    offer_item = moco.Offer.get(offer_id)
    formatter.format_single(offer_item.data)


@offer.command()
@click.option("--status", type=click.Choice([e.value for e in OfferStatus]))
@click.option("--start", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("--end", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("-p", '--page', type=int)
@click.option("-a", "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, status, start, end, page, retrieve_all):
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []
        items_list = moco.Offer.getlist(page=1, from_date=start, to_date=end, status=status)
        all_items.extend(items_list.items)

        for i in range(2, items_list.last_page + 1):
            items_list = moco.Offer.getlist(page=i, from_date=start, to_date=end, status=status)
            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Offer.getlist(page=page, from_date=start, to_date=end, status=status)
        formatter.format_list(items_list.items)
