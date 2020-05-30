import click
from moco_explorer.commands.user import holiday, employment, presence

@click.group()
@click.pass_context
def user(ctx):
    pass


# add user modules
user.add_command(holiday.main)
user.add_command(employment.main)
user.add_command(presence.main)


@user.command(help="Retrieve a list of users")
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option("--include-archived", help="include archived users", is_flag=True)
@click.option('-a', "--retrieve-all", help="loops over the whole list", is_flag=True)
@click.pass_context
def getlist(ctx, page, include_archived, retrieve_all):
    """
    Retrieve a list of users

    :param ctx: click context
    :param page: page number
    :param include_archived: flag to include archived users
    :param retrieve_all: flag to retrieve all objects from the system (ignores page option)
    :return: formatted list of users
    """

    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.User.getlist(page=next_page, include_archived=include_archived)

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.User.getlist(page=page, include_archived=include_archived)
        formatter.format_list(items_list.items)


@user.command(help="Retrieve a single user")
@click.argument("user-id", type=int)
@click.pass_context
def get(ctx, user_id):
    """
    Retrive a single user

    :param ctx: click context
    :param user_id: id of the user
    :return: formatted user object
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    user_obj = moco.User.get(user_id)
    formatter.format_single(user_obj.data)
