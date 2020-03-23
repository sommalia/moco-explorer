from moco_explorer.commands import user
from ..base import BaseCliTest


class TestCliUser(BaseCliTest):

    def test_getlist_in_commands_list(self):
        assert "getlist" in user.main.commands

    def test_get_in_commands_list(self):
        assert "get" in user.main.commands
