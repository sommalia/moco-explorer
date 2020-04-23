from .csv import CsvFormatter
import click


class TextFormatter(CsvFormatter):
    def format_single(self, target):
        target_as_dict = self.obj_to_dict(target)
        flat_dict = self.flatten_dict(target_as_dict)

        header_keys = self._sort_header_keys(flat_dict.keys())

        lines = {
            "base": []
        }

        for key in header_keys:
            if "." in key:
                prefix = ".".join(key.split(".")[:-1])
                if prefix not in lines.keys():
                    lines[prefix] = []

                lines[prefix].append((key, flat_dict[key]))
            else:
                lines["base"].append((key, flat_dict[key]))

        click.echo("information:")
        for key, value in lines["base"]:
            if value.strip() != "":
                click.echo("{}: {}".format(key, value))

        if len([x for x in lines.keys() if x != "base"]) > 0:
            other_line_keys = [x for x in lines.keys() if x != "base"]
            for other_line_key in other_line_keys:
                click.echo("")
                click.echo("{} info:".format(other_line_key))

                for key, value in lines[other_line_key]:
                    if value.strip() != "":
                        click.echo("{}: {}".format(key, value))

    def format_list(self, target):
        for i, item in enumerate(target):
            self.format_single(item)

            terminal_width, terminal_height = click.get_terminal_size()
            splitter_line = "".join(["="] * terminal_width)

            if i < len(target) - 1:
                click.echo(splitter_line)
                click.echo(splitter_line)
