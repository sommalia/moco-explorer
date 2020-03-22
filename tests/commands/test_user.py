from moco_explorer.commands import user
from ..base import BaseCliTest


class TestCliUser(BaseCliTest):

    def test_getlist_in_commands_list(self):
        result = self.runner.invoke(user)

        commands = self.extract_commands_list(result.output)
        assert "getlist" in commands

    def test_get_in_commands_list(self):
        result = self.runner.invoke(user)

        commands = self.extract_commands_list(result.output)
        assert "get" in commands
