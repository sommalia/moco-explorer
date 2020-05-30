import click
from moco_explorer.const import DEFAULT_DATETIME_FORMATS

@click.group()
@click.pass_context
def activity(ctx):
    pass

@activity.command()
@click.argument("activity-id", type=int)
@click.pass_context
def get(ctx, activity_id):
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    activity_obj = moco.Activity.get(activity_id)
    formatter.format_single(activity_obj.data)


@activity.command()
@click.argument("start", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.argument("end", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("--user-id", type=int)
@click.option("--project-id", type=int)
@click.option("--task-id", type=int)
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, start, end, user_id, project_id, task_id, page, retrieve_all):
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.Activity.getlist(
                page=next_page,
                from_date=start,
                to_date=end,
                user_id=user_id,
                project_id=project_id,
                task_id=task_id
            )

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Activity.getlist(
            page=page,
            from_date=start,
            to_date=end,
            user_id=user_id,
            project_id=project_id,
            task_id=task_id
        )
        formatter.format_list(items_list.items)


