import click

@click.group(help="Deal category module")
@click.pass_context
def category(ctx):
    pass


@category.command(help="Retrieve a single deal category")
@click.argument("deal-category-id", type=int)
@click.pass_context
def get(ctx, deal_category_id):
    """
    Retrieve a single deal category

    :param ctx: click context
    :param deal_category_id: id of the category
    :return: formatted category object
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    deal_cat_obj = moco.DealCategory.get(deal_category_id)
    formatter.format_single(deal_cat_obj.data)

@category.command(help="Retrieve a list of deal catgories")
@click.option("-p", "--page", help="Page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, page, retrieve_all):
    """
    Retrieve a list of category objects

    :param ctx: click context
    :param page: page number
    :param retrieve_all: flag to retrieve all objects from the system (ignores page option)
    :return: formatted list of categories
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        if not end_reached:
            items_list = moco.DealCategory.getlist(page=next_page)

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.DealCategory.getlist(page=page)
        formatter.format_list(items_list.items)
