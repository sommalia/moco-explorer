from ..base import BaseCliTest
from moco_explorer.commands import config


class TestCliConfig(BaseCliTest):

    def test_get_in_commands_list(self):
        result = self.runner.invoke(config.main)

        commands = self.extract_commands_list(result.output)
        assert "get" in commands

    def test_create_in_commands_list(self):
        result = self.runner.invoke(config.main)

        commands = self.extract_commands_list(result.output)
        assert "create" in commands
