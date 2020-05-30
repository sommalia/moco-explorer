import click

@click.group(help="User Holiday module")
@click.pass_context
def holiday(ctx):
    pass

@holiday.command(help="Retrieve a single user holiday")
@click.argument("holiday-id")
@click.pass_context
def get(ctx, holiday_id):
    """
    Retrieve a single holiday entry

    :param ctx: click context
    :param holiday_id: id of the entry to retrieve
    :return: formatted holiday entry
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    holiday_obj = moco.UserHoliday.get(holiday_id)
    formatter.format_single(holiday_obj.data)

@holiday.command(help="Retrieve a list of user holidays")
@click.option("--year", type=int)
@click.option("--user-id", type=int)
@click.option("-p", "--page", help="Page number")
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, year, user_id, page, retrieve_all):
    """
    Retrieve a list of user holiday objects

    :param ctx: click context
    :param year: year
    :param user_id: user id
    :param page: page number
    :param retrieve_all: flag to retrieve all items from the system (ignore page option)
    :return: formatted list of user holiday entries
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        next_page = 1
        end_reached = False

        while not end_reached:
            items_list = moco.UserHoliday.getlist(
                year=year,
                user_id=user_id,
                page=next_page
            )
            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.UserHoliday.getlist(
            year=year,
            user_id=user_id,
            page=page
        )
        formatter.format_list(items_list.items)
