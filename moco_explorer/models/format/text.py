from .base import BaseFormatter
import click

class TextFormatter(BaseFormatter):
    def format_single(self, target):
        click.echo(target)

    def format_list(self, target):
        click.echo(target)
