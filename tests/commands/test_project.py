from click.testing import CliRunner
from moco_explorer.commands import project
from ..base import BaseCliTest


class TestCliProject(BaseCliTest):

    def test_getlist_in_commands_list(self):
        result = self.runner.invoke(project.main, ["--help"])

        commands = self.extract_commands_list(result.output)
        assert "getlist" in commands

    def test_get_in_commands_list(self):
        result = self.runner.invoke(project.main, ["--help"])

        commands = self.extract_commands_list(result.output)
        assert "get" in commands
