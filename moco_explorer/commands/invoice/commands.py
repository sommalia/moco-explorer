import click


@click.group()
@click.pass_context
def invoice(ctx):
    pass


@invoice.command()
@click.option("-p", "--page", help="page number", type=int, default=1)
@click.option('-a', "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, page, retrieve_all):
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []
        items_list = moco.Invoice.getlist(page=1)
        all_items.extend(items_list.items)

        for i in range(2, items_list.last_page + 1):
            items_list = moco.Invoice.getlist(page=i)
            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.Invoice.getlist(page=page)
        formatter.format_list(items_list.items)


@invoice.command()
@click.argument("invoice-id", type=int)
@click.pass_context
def get(ctx, invoice_id):
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    invoice_item = moco.Invoice.get(invoice_id)
    formatter.format_single(invoice_item.data)


@invoice.command()
@click.argument("invoice-id", type=int)
@click.argument("out_path", type=click.Path(exists=False, writable=True))
@click.pass_context
def pdf(ctx, invoice_id, out_path):
    moco = ctx.obj["moco"]

    invoice_pdf = moco.Invoice.pdf(invoice_id)
    invoice_pdf.write_to_file(out_path)
