from .base import BaseFormatter
import click


class RawFormatter(BaseFormatter):
    def format_list(self, target):
        click.echo(target)

    def format_single(self, target):
        click.echo(target)
