import click
from moco_explorer.const import DEFAULT_DATETIME_FORMATS

@click.group(help="Invoice payment module")
@click.pass_context
def payment(ctx):
    pass


@payment.command(help="Retrieve a single invoice payment")
@click.argument("payment-id", type=int)
@click.pass_context
def get(ctx, payment_id):
    """
    Retrieve a single invoice payment

    :param ctx: click context
    :param payment_id: id of the payment
    :return: formatted payment
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    payment_obj = moco.InvoicePayment.get(payment_id)
    formatter.format_single(payment_obj.data)


@payment.command(help="Retrieve a list of invoice payments")
@click.option("--invoice-id", type=int)
@click.option("--start", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("--end", type=click.DateTime(formats=DEFAULT_DATETIME_FORMATS))
@click.option("-p", '--page', type=int)
@click.option("-a", "--retrieve-all", help="Retrieve all objects from the system (ignores page option)", is_flag=True)
@click.pass_context
def getlist(ctx, invoice_id, start, end, page, retrieve_all):
    """
    Retrieve a list of invoice payments

    :param ctx: click context
    :param invoice_id: id of the invoice the payment belongs to
    :param start: start date
    :param end: end date
    :param page: page number
    :param retrieve_all: flag to retrieve all objects from the system (ignores page option)
    :return: formatted list of invoice payments
    """
    formatter = ctx.obj["format"]
    moco = ctx.obj["moco"]

    if retrieve_all:
        all_items = []

        end_reached = False
        next_page = 1

        while not end_reached:
            items_list = moco.InvoicePayment.getlist(
                page=next_page,
                invoice_id=invoice_id,
                date_from=start,
                date_to=end
            )

            next_page = items_list.next_page
            end_reached = items_list.is_last

            all_items.extend(items_list.items)

        formatter.format_list(all_items)
    else:
        items_list = moco.InvoicePayment.getlist(
            page=page,
            invoice_id=invoice_id,
            date_from=start,
            date_to=end
        )
        formatter.format_list(items_list.items)
