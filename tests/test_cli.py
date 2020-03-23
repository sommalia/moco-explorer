#!/usr/bin/env python

"""Tests for `moco_explorer` package."""

import pytest
from click.testing import CliRunner
from moco_explorer import cli
from .base import BaseCliTest


class TestCliMain(BaseCliTest):

    def test_project_command_in_commands_list(self):
        assert "project" in cli.main.commands

    def test_user_command_in_commands_list(self):
        assert "user" in cli.main.commands

    def test_invoice_in_commands_list(self):
        assert "invoice" in cli.main.commands

    def test_config_in_commands_list(self):
        assert "config" in cli.main.commands

