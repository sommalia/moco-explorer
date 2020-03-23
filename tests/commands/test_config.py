from ..base import BaseCliTest
from moco_explorer.commands import config


class TestCliConfig(BaseCliTest):

    def test_get_in_commands_list(self):
        assert "get" in config.main.commands

    def test_create_in_commands_list(self):
        assert "create" in config.main.commands
