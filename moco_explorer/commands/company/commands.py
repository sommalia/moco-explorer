import click
from moco_wrapper.models.company import CompanyType


@click.group()
@click.pass_context
def company(ctx):
    pass


@company.command()
@click.argument("company-id", type=int)
@click.pass_context
def get(ctx, company_id):
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    company_item = moco.Company.get(company_id)
    formatter.format_single(company_item.data)


@company.command()
@click.option("-t", "--company-type", type=click.Choice([e.value for e in CompanyType]))
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, company_type, page, retrieve_all):
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []
        items_list = moco.Company.getlist(company_type=company_type, page=1)
        all_items.extend(items_list.items)

        for i in range(2, items_list.last_page + 1):
            items_list = moco.Company.getlist(company_type=company_type, page=i)
            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Company.getlist(company_type=company_type, page=page)
        formatter.format_list(items_list.items)
