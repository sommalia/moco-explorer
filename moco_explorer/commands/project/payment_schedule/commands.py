import click

@click.group(help="Project payment schedule module (fixed price projects only)")
@click.pass_context
def payment_schedule(ctx):
    pass


@payment_schedule.command(help="Retrive a single project payment schedule")
@click.argument("project-id", type=int)
@click.argument("schedule-id", type=int)
@click.pass_context
def get(ctx, project_id, schedule_id):
    """
    Retrieve a single project payment schedule

    :param ctx: click context
    :param project_id: id of the project the schedule belongs to
    :param schedule_id: id of the payment schedule
    :return: fomatted payment schedule
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    schedule_obj = moco.ProjectPaymentSchedule.get(project_id, schedule_id)
    formatter.format_single(schedule_obj.data)


@payment_schedule.command(help="Retrieve a list of project payment schedules")
@click.argument("project-id", type=int)
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, project_id, page, retrieve_all):
    """
    Retrieve a list of project payment schedules

    :param ctx: click context
    :param project_id: id of the project the payment schedules belong to
    :param page: page number
    :param retrieve_all: flag to retrieve all objects from the system (ignores page option)
    :return: formatted list of payment schedules
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.ProjectPaymentSchedule.getlist(project_id, page=next_page)

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.ProjectPaymentSchedule.getlist(project_id, page=page)
        formatter.format_list(items_list.items)
