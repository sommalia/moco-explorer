from .base import BaseFormatter
from json import dumps
from click import echo


class JsonFormatter(BaseFormatter):

    def format_single(self, target):
        echo(
            dumps(target, indent=4, sort_keys=True, default=lambda x: x.__dict__)
        )

    def format_list(self, target):
        echo(
            dumps(target, indent=4, sort_keys=True, default=lambda x: x.__dict__)
        )
