import pytest

from os import path
from moco_explorer.models import Configuration


@pytest.fixture()
def config_path():
    return "/tmp/.moco-explorer"


def test_create(config_path):
    c = Configuration(config_path)
    c.create("test api key", "test domain")

    assert path.exists(config_path)


def test_get(config_path):
    api_key = "test api key"
    domain = "test domain"

    c = Configuration(config_path)
    c.create(api_key, domain)

    del c
    c = Configuration(config_path)

    assert c.get("api_key") == api_key
    assert c.get("domain") == domain


def test_load_implicit_execute_on_get(config_path):
    c = Configuration(config_path)
    c.create("test", "test")

    del c
    c = Configuration(config_path)

    assert c.config is None

    c.get("api_key")

    assert c.config is not None


def test_delete(config_path):
    c = Configuration(config_path)
    c.create("test", "test")

    assert path.exists(config_path)

    c.delete()

    assert not path.exists(config_path)
