import click

from moco_explorer.commands.project import contract, expense, recurring_expense, task, payment_schedule


@click.group(help="Project module")
@click.pass_context
def project(ctx):
    pass


# add project modules
project.add_command(contract.main)
project.add_command(expense.main)
project.add_command(recurring_expense.main)
project.add_command(task.main)
project.add_command(payment_schedule.main)


@project.command(help="Retrieve a list of projects")
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option("--include-archived", help="include archived projects", is_flag=True)
@click.option("--include-company", help="include whole company", is_flag=True)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, page, include_archived, include_company, retrieve_all):
    """
    Retrieve a list of projects

    :param ctx: click context
    :param page: page number
    :param include_archived: flag to include archived projects
    :param include_company: flag to include a whole company object in the response
    :param retrieve_all: flag to retrieve all objects from the system (ignores page option)
    :return: formatted list of projects
    """
    moco = ctx.obj["moco"]
    formatter = ctx.obj["format"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.Project.getlist(
                page=next_page,
                include_archived=include_archived,
                include_company=include_company,
            )

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Project.getlist(
            page=page,
            include_archived=include_archived,
            include_company=include_company
        )
        formatter.format_list(items_list.items)


@project.command(help="Retrieve a single project")
@click.argument("project-id", type=int)
@click.pass_context
def get(ctx, project_id):
    """
    Retrieve a single projects

    :param ctx: click context
    :param project_id: id of the projects
    :return: formatted project object
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    company_obj = moco.Project.get(project_id)
    formatter.format_single(company_obj.data)
