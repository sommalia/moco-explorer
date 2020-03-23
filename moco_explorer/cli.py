"""Console script for moco_explorer."""
import sys
import click
import json
from os import environ, path

import moco_explorer.commands as cmd
import moco_explorer.models as models

DEFAULT_CONFIG = path.join(environ.get("HOME"), ".moco_explorer.json")


@click.group()
@click.option("--config", default=DEFAULT_CONFIG)
@click.option("--mode", type=click.Choice(["interactive", "script"]), default="interactive")
@click.pass_context
def main(ctx, config, mode):
    """Console script for moco_explorer."""
    ctx.ensure_object(dict)

    # load current config file for authentication
    configuration = models.Configuration(config)
    ctx.obj["config"] = configuration

    if ctx.invoked_subcommand != "config" and not path.exists(config) and mode == "interactive":
        # interactive mode, path does not exists, also tries to invoke non config command
        click.echo("config file does not exist, create it")
        ctx.invoke(cmd.config.create)

    return 0


main.add_command(cmd.project.main)
main.add_command(cmd.user.main)
main.add_command(cmd.invoice.main)
main.add_command(cmd.config.main)

if __name__ == "__main__":
    sys.exit(main(obj={}))  # pragma: no cover
