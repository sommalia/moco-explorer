import click
from moco_wrapper.models.company import CompanyType


@click.group()
@click.pass_context
def company(ctx):
    pass


@company.command(help="Retrieve a single company")
@click.argument("company-id", type=int)
@click.pass_context
def get(ctx, company_id):
    """
    Retrieve a single company

    :param ctx: click context
    :param company_id: id of the company
    :return: formatted company
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    company_item = moco.Company.get(company_id)
    formatter.format_single(company_item.data)


@company.command(help="Retrieve a list of companies")
@click.option("-t", "--company-type", type=click.Choice([e.value for e in CompanyType]))
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, company_type, page, retrieve_all):
    """
    Retrieve a list of companies

    :param ctx: click context
    :param company_type: type of company
    :param page: page number
    :param retrieve_all: flag to retrieve all items from the system (ignores pae option)
    :return: formatted list of companies
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.Company.getlist(company_type=company_type, page=next_page)

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Company.getlist(company_type=company_type, page=page)
        formatter.format_list(items_list.items)
