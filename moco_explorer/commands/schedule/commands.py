import click
from moco_explorer.const import DEFAULT_DATETIME_FORMATS
from moco_wrapper.models.schedule import ScheduleAbsenceCode

@click.group(help="Schedule module")
@click.pass_context
def schedule(ctx):
    pass

@schedule.command(help="Retrieve a single schedule entry")
@click.argument("schedule-id", type=int)
@click.pass_context
def get(ctx, schedule_id):
    """
    Retrieve a single schedule entry

    :param ctx: click context
    :param schedule_id: id of the entry to retrieve
    :return: formatted schedule object
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    schedule_obj = moco.Schedule.get(schedule_id)
    formatter.format_single(schedule_obj.data)

@schedule.command(help="Retrieve a list of schedule objects")
@click.option("--start", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("--end", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("--user-id", type=int)
@click.option("--project-id", type=int)
@click.option("--absence-code", type=click.Choice([e.value for e in ScheduleAbsenceCode]))
@click.option("-p", "--page", help="Page number", default=1)
@click.option("-a", "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, start, end, user_id, project_id, absence_code, page, retrieve_all):
    """
    Retrieve a list of schedule objects

    :param ctx: click context
    :param start: start date
    :param end: end date
    :param user_id: user id
    :param project_id: project id
    :param absence_code: absence code
    :param page: page number
    :param retrieve_all: flag to retrieve all items from the system (ignores pag e option)
    :return: list of formatted schedule objects
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        next_page = 1
        end_reached = False

        while not end_reached:
            items_list = moco.Schedule.getlist(
                from_date=start,
                to_date=end,
                user_id=user_id,
                project_id=project_id,
                absence_code=absence_code,
                page=next_page
            )
            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Schedule.getlist(
            from_date=start,
            to_date=end,
            user_id=user_id,
            project_id=project_id,
            absence_code=absence_code,
            page=page
        )
        formatter.format_list(items_list.items)

