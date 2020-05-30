import click

@click.group(help="Project task module")
@click.pass_context
def task(ctx):
    pass

@task.command(help="Retrieve a single project task")
@click.argument("project-id", type=int)
@click.argument("task-id", type=int)
@click.pass_context
def get(ctx, project_id, task_id):
    """
    Retrieve a single project task

    :param ctx: click context
    :param project_id: id of the project the task belongs to
    :param task_id: id of the task
    :return: formatted task object
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    task_obj = moco.ProjectTask.get(project_id, task_id)
    formatter.format_single(task_obj.data)

@task.command(help="Retrieve a list of project tasks")
@click.argument("project-id", type=int)
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, project_id, page, retrieve_all):
    """
    Retrieve a list of project tasks

    :param ctx: click context
    :param project_id: id of the project the tasks belong to
    :param page: page number
    :param retrieve_all: flag to retrieve all items from the system (ignores page option)
    :return: formatted list of project tasks
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.ProjectTask.getlist(project_id, page=next_page)

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.ProjectTask.getlist(project_id, page=page)
        formatter.format_list(items_list.items)
