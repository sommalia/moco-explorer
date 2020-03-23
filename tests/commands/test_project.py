from click.testing import CliRunner
from moco_explorer.commands import project
from ..base import BaseCliTest


class TestCliProject(BaseCliTest):

    def test_getlist_in_commands_list(self):
        assert "getlist" in project.main.commands

    def test_get_in_commands_list(self):
        assert "get" in project.main.commands
