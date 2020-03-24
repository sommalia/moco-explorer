"""Console script for moco_explorer."""
import sys
import click
import json
from os import environ, path

from moco_wrapper import Moco

import moco_explorer.commands as cmd
import moco_explorer.models as models

DEFAULT_CONFIG = path.join(environ.get("HOME"), ".moco_explorer.json")


@click.group()
@click.option("--config", default=DEFAULT_CONFIG)
@click.option("--mode", type=click.Choice(["interactive", "script"]), default="interactive")
@click.option("--formatter", type=click.Choice(["json", "csv", "text"]), default="text")
@click.option("--debug-proxy", is_flag=True)
@click.pass_context
def main(ctx, config, mode, formatter, debug_proxy):
    """Console script for moco_explorer."""
    ctx.ensure_object(dict)

    # load current config file for authentication
    configuration = models.Configuration(config)
    ctx.obj["config"] = configuration

    if ctx.invoked_subcommand != "config" and not path.exists(config) and mode == "interactive":
        # interactive mode, path does not exists, also tries to invoke non config command
        click.echo("config file does not exist, create it")
        ctx.invoke(cmd.config.create)

    if ctx.invoked_subcommand != "config":
        ctx.invoke(cmd.config.authenticate)
        ctx.obj["moco"] = Moco(
            auth={
                "api_key": configuration.get("api_key"),
                "domain": configuration.get("domain")
            }
        )

        if debug_proxy:
            ctx.obj["moco"].requestor.session.proxies = {
                "https": "127.0.0.1:8080"
            }
            ctx.obj["moco"].requestor.session.verify = False

    if formatter == "json":
        ctx.obj["format"] = models.format.JsonFormatter()
    elif formatter == "csv":
        ctx.obj["format"] = models.format.CsvFormatter()
    else:
        ctx.obj["format"] = models.format.TextFormatter()

    return 0


main.add_command(cmd.project.main)
main.add_command(cmd.user.main)
main.add_command(cmd.invoice.main)
main.add_command(cmd.config.main)

if __name__ == "__main__":
    sys.exit(main(obj={}))  # pragma: no cover
