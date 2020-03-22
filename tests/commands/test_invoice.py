from ..base import BaseCliTest
from moco_explorer.commands import invoice

class TestCliInvoice(BaseCliTest):

    def test_getlist_in_commands_list(self):
        result = self.runner.invoke(invoice)

        commands = self.extract_commands_list(result.output)
        assert "getlist" in commands

    def test_get_in_commands_list(self):
        result = self.runner.invoke(invoice)

        commands = self.extract_commands_list(result.output)
        assert "get" in commands
