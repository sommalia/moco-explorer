import click

@click.group(help="Project contract module")
@click.pass_context
def contract(ctx):
    pass

@contract.command(help="Retrieve a single contract")
@click.argument("project-id", type=int)
@click.argument("contract-id", type=int)
@click.pass_context
def get(ctx, project_id, contract_id):
    """
    Retrieve a single project contract

    :param ctx: click contract
    :param project_id: id of the project the contract belongs to
    :param contract_id: id of the contract
    :return: formatted contract object
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    contract_obj = moco.ProjectContract.get(project_id, contract_id)
    formatter.format_single(contract_obj.data)


@contract.command(help="Retrieve a list of project contracts")
@click.argument("project-id")
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, project_id, page, retrieve_all):
    """
    Retrieve a list of project contracts

    :param ctx: click context
    :param project_id: id of the project the contracts belong to
    :param page: page number
    :param retrieve_all: flag to retrieve all objects from the system (ignores page option)
    :return: formatted list of project contracts
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.ProjectContract.getlist(project_id, page=next_page)

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.ProjectContract.getlist(project_id, page=page)
        formatter.format_list(items_list.items)



