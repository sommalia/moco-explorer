"""Console script for moco_explorer."""
import sys
import click

import moco_explorer.commands as cmd


@click.group()
def main(args=None):
    """Console script for moco_explorer."""
    click.echo("Replace this message by putting your code into "
               "moco_explorer.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")

    return 0


main.add_command(cmd.project)
main.add_command(cmd.user)
main.add_command(cmd.invoice)

if __name__ == "__main__":
    # add sys.path when directly called
    sys.exit(main())  # pragma: no cover
