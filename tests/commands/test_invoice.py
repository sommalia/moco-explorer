from ..base import BaseCliTest
from moco_explorer.commands import invoice

class TestCliInvoice(BaseCliTest):

    def test_getlist_in_commands_list(self):
        assert "getlist" in invoice.main.commands

    def test_get_in_commands_list(self):
        assert "get" in invoice.main.commands
