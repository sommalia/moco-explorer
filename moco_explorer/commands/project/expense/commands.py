import click
from moco_explorer.const import DEFAULT_DATETIME_FORMATS

@click.group(help="Project expense module")
@click.pass_context
def expense(ctx):
    pass


@expense.command(help="Retrieve a single project expense")
@click.argument("project-id", type=int)
@click.argument("expense-id", type=int)
@click.pass_context
def get(ctx, project_id, expense_id):
    """
    Retrieve a single project expense

    :param ctx: click context
    :param project_id: id of the project the expense belongs to
    :param expense_id: id of the expense
    :return: formatted expense object
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    expense_obj = moco.ProjectExpense.get(project_id, expense_id)
    formatter.format_single(expense_obj.data)


@expense.command(help="Retrieve a list of project expenses (by project)")
@click.argument("project-id", type=int)
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, project_id, page, retrieve_all):
    """
    Retrieve a list of project expenses

    :param ctx: click context
    :param project_id: id of the project the expenses belong to
    :param page: page number
    :param retrieve_all: flag to retrieve all objects from the system (ignores page option)
    :return: formatted list of project expenses
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.ProjectExpense.getlist(project_id, page=next_page)

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.ProjectExpense.getlist(project_id, page=page)
        formatter.format_list(items_list.items)



@expense.command(help="Retrieve a list of project expenses (regardless of project)")
@click.option("--start", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("--end", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getall(ctx, start, end, page, retrieve_all):
    """
    Retrieve a list of project expenses regardless of the projects they belong to

    :param ctx: click context
    :param start: start date
    :param end: end date
    :param page: page number
    :param retrieve_all: flag to retrieve all objects from the system (ignores page option)
    :return: formatted list of project expenses
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.ProjectExpense.getall(from_date=start, to_date=end, page=next_page)

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.ProjectExpense.getall(from_date=start, to_date=end, page=page)
        formatter.format_list(items_list.items)
