import click


@click.group()
def contact():
    pass


@contact.command(help="Retrieve a single contact")
@click.argument("contact-id", type=int)
@click.pass_context
def get(ctx, contact_id):
    """
    Retrieve a single contact object

    :param ctx: click context
    :param contact_id: id of the contact object
    :return: formatted contact
    """

    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    contact_obj = moco.Contact.get(contact_id)
    formatter.format_single(contact_obj.data)


@contact.command(help="Retrieve a list of contacts")
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="loops over the whole list", is_flag=True)
@click.pass_context
def getlist(ctx, page, retrieve_all):
    """
    Retrieve a list of contact objects

    :param ctx: click context
    :param page: page number
    :param retrieve_all: flag to retrieve all objects from the system (ignores page option)
    :return: formatted list of contact objects
    """

    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []
        items_list = moco.Contact.getlist(page=1)
        all_items.extend(items_list.items)

        for i in range(2, items_list.last_page + 1):
            items_list = moco.Contact.getlist(page=i)
            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Contact.getlist(page=page)
        formatter.format_list(items_list.items)
