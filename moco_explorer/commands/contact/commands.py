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

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.Contact.getlist(page=next_page)

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Contact.getlist(page=page)
        formatter.format_list(items_list.items)
