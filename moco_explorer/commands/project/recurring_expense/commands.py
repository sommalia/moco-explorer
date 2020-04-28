import click

@click.group(help="Project recurring expense module")
@click.pass_context
def recurring_expense(ctx):
    pass

@recurring_expense.command(help="Retrieve a single recurring expense")
@click.argument("project-id", type=int)
@click.argument("recurring-expense-id", type=int)
@click.pass_context
def get(ctx, project_id, recurring_expense_id):
    """
    Retrieve a single recurring expense

    :param ctx: click context
    :param project_id: id of the project the recurring expense belongs to
    :param recurring_expense_id: id of the recurring expense
    :return: formatted recurring expense
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    recurring_expense_obj = moco.ProjectRecurringExpense.get(project_id, recurring_expense_id)
    formatter.format_single(recurring_expense_obj.data)


@recurring_expense.command(help="Retrieve a list of recurring expenses")
@click.argument("project-id", type=int)
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, project_id, page, retrieve_all):
    """
    Retrieve a list of recurring expenses

    :param ctx: click context
    :param project_id: id of the project the recurring expenses belong to
    :return: formatted list of recurring expenses
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.ProjectRecurringExpense.getlist(project_id, page=next_page)

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.ProjectRecurringExpense.getlist(project_id, page=page)
        formatter.format_list(items_list.items)

