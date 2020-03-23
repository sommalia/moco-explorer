import pytest

from ..base import BaseCliTest
from moco_explorer.commands import config
from moco_explorer.models.format import RawFormatter
from moco_explorer.models import Configuration

@pytest.fixture
def config_path():
    return "/tmp/.moco-explorer"

class TestCliConfig(BaseCliTest):

    def test_get_in_commands_list(self):
        assert "get" in config.main.commands

    def test_create_in_commands_list(self):
        assert "create" in config.main.commands

    def test_get(self, config_path):
        api_key = "test config get api key"
        domain = "test config get domain"

        c = Configuration(config_path)
        c.create(api_key, domain)

        obj = {
            "config": c,
            "format": RawFormatter()
        }

        result = self.runner.invoke(config.get, obj=obj)

        assert api_key in result.output
        assert domain in result.output
        assert result.exit_code == 0
