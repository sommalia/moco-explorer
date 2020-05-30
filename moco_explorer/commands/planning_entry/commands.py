import click
from moco_explorer.const import DEFAULT_DATETIME_FORMATS

@click.group(help="Planning entry module")
@click.pass_context
def planning_entry(ctx):
    pass

@planning_entry.command(help="Retrieve a single planning entry")
@click.argument("entry-id", type=int)
@click.pass_context
def get(ctx, entry_id):
    """
    Retrieve a single planning entry object

    :param ctx: click context
    :param entry_id: id of the planning entry to retrieve
    :return: formatted planning entry
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    entry_obj = moco.PlanningEntry.get(entry_id)
    formatter.format_single(entry_obj.data)

@planning_entry.command(help="Retrieve a list of planning entries")
@click.option("--start", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("--end", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("--user-id", type=int)
@click.option("--project-id", type=int)
@click.option("-p", "--page", help="Page number", default=1)
@click.option("-a", "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, start, end, user_id, project_id, page, retrieve_all):
    """
    Retrieve a list of planning entries

    :param ctx: click context
    :param start: start date
    :param end: end date
    :param user_id: user id
    :param project_id: project id
    :param page: page number
    :param retrieve_all: flat to retrieve all items from the system (ignores page option)
    :return: formatted list of planning entries
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.PlanningEntry.getlist(
                start_date=start,
                end_date=end,
                user_id=user_id,
                project_id=project_id,
                page=next_page
            )
            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.PlanningEntry.getlist(
            start_date=start,
            end_date=end,
            user_id=user_id,
            project_id=project_id,
            page=page
        )
        formatter.format_list(items_list.items)


