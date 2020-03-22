from click.testing import CliRunner


class BaseCliTest(object):

    def setup(self):
        self.runner = CliRunner()

    def extract_commands_list(self, output):
        lines = [x.strip() for x in output.split("\n")]

        commands = []
        commands_found = False
        for l in lines:
            if commands_found and l.strip() != '':
                commands.append(l)

            if l == "Commands:":
                commands_found = True

        return commands
