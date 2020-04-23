import click


@click.group()
@click.pass_context
def project(ctx):
    pass


@project.command()
@click.pass_context
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option("--include-archived", help="include archived projects", is_flag=True)
@click.option("--include-company", help="include whole company", is_flag=True)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
def getlist(ctx, page, include_archived, include_company, retrieve_all):
    moco = ctx.obj["moco"]
    formatter = ctx.obj["format"]

    if retrieve_all:
        all_items = []

        items_list = moco.Project.getlist(
            page=1,
            include_archived=include_archived,
            include_company=include_company
        )

        all_items.extend(items_list.items)

        for i in range(2, items_list.last_page + 1):
            items_list = moco.Project.getlist(
                page=i,
                include_archived=include_archived,
                include_company=include_company,
            )
            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Project.getlist(
            page=page,
            include_archived=include_archived,
            include_company=include_company
        )
        formatter.format_list(items_list.items)

@project.command()
@click.argument("project-id", type=int)
@click.pass_context
def get(ctx, project_id):
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    company_obj = moco.Project.get(project_id)
    formatter.format_single(company_obj.data)
