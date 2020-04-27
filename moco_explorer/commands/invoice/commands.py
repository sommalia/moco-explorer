import click

from moco_explorer.commands.invoice import payment

from os.path import realpath

@click.group()
@click.pass_context
def invoice(ctx):
    pass

# add payment module
invoice.add_command(payment.main)

@invoice.command(help="Retrieve a single invoice")
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, page, retrieve_all):
    """
    Retrieve a list of invoice objects

    :param ctx: click context
    :param page: page number
    :param retrieve_all: flag to retrieve a objects from the system (ignores page option)
    :return: formatted list of invoice objects
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.Invoice.getlist(page=next_page)

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Invoice.getlist(page=page)
        formatter.format_list(items_list.items)


@invoice.command(help="Retrieve a single invoice")
@click.argument("invoice-id", type=int)
@click.pass_context
def get(ctx, invoice_id):
    """
    Retrieve a single invoice

    :param ctx: click context
    :param invoice_id: id of the invoice
    :return: formatted invoice object
    """

    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    invoice_item = moco.Invoice.get(invoice_id)
    formatter.format_single(invoice_item.data)


@invoice.command(help="Retrieve the pdf document of an invoice")
@click.argument("invoice-id", type=int)
@click.argument("out-path", type=click.Path(exists=False, writable=True))
@click.pass_context
def pdf(ctx, invoice_id, out_path):
    """
    Retrieve the pdf document of an invoice

    :param ctx: click context
    :param invoice_id: id of the invoice
    :param out_path: path for the pdf file to saved to
    """

    moco = ctx.obj["moco"]

    invoice_pdf = moco.Invoice.pdf(invoice_id)
    invoice_pdf.write_to_file(out_path)

    click.echo("Pdf document successfully saved to {}".format(realpath(out_path)))
