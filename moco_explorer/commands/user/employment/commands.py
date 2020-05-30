import click
from moco_explorer.const import DEFAULT_DATETIME_FORMATS

@click.group(help="User employment module")
@click.pass_context
def employment(ctx):
    pass

@employment.command(help="Retrieve a single user employment")
@click.argument("employment-id", type=int)
@click.pass_context
def get(ctx, employment_id):
    """
    Retrieve a single user employment

    :param ctx: click context
    :param employment_id: id of the employment
    :return: formatted employment object
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    employment_obj = moco.UserEmployment.get(employment_id)
    formatter.format_single(employment_obj.data)

@employment.command(help="Retrieve a list of user employments")
@click.option("--start", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("--end", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("--user-id", type=int)
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, start, end, user_id, page, retrieve_all):
    """
    Retrieve a list of user employments

    :param ctx: click context
    :param start: start date
    :param end: end date
    :param user_id: user id
    :param page: page
    :param retrieve_all: flag to retrieve all objects from the system (ignores page option)
    :return: formatted list of user employments
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        next_page = 1
        end_reached = False

        while not end_reached:
            items_list = moco.UserEmployment.getlist(
                from_date=start,
                to_date=end,
                user_id=user_id,
                page=next_page
            )

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.UserEmployment.getlist(
            from_date=start,
            to_date=end,
            user_id=user_id,
            page=page
        )
        formatter.format_list(items_list.items)

