import click
from moco_explorer.const import DEFAULT_DATETIME_FORMATS

@click.group(help="User presence module")
@click.pass_context
def presence(ctx):
    pass

@presence.command(help="Retrieve a single user presence")
@click.argument("presence-id")
@click.pass_context
def get(ctx, presence_id):
    """
    Retrieve a single presence object

    :param ctx: click context
    :param presence_id: id of user presence to retrieve
    :return: formatted user presence
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    presence_obj = moco.UserPresence.get(presence_id)
    formatter.format_single(presence_obj.data)

@presence.command(help="Retrieve a list of user presences")
@click.option("--start", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("--end", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("--user-id", type=int)
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, start, end, user_id, page, retrieve_all):
    """
    Retrieve a list of user presences

    :param ctx: click context
    :param start: start date
    :param end: end date
    :param user_id: user id
    :param page: page
    :param retrieve_all: flag to retrieve all objects from the system (ignores page option)
    :return: formatted list of user presences
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        next_page = 1
        end_reached = False

        while not end_reached:
            items_list = moco.UserPresence.getlist(
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
        items_list = moco.UserPresence.getlist(
            from_date=start,
            to_date=end,
            user_id=user_id,
            page=page
        )
        formatter.format_list(items_list.items)
