#!/usr/bin/env python

"""Tests for `moco_explorer` package."""

import pytest
from click.testing import CliRunner
from moco_explorer import cli
from .base import BaseCliTest


class TestCliMain(BaseCliTest):

    def test_project_command_in_commands_list(self):
        result = self.runner.invoke(cli.main)

        commands = self.extract_commands_list(result.output)
        assert "project" in commands

    def test_user_command_in_commands_list(self):
        result = self.runner.invoke(cli.main)

        commands = self.extract_commands_list(result.output)
        assert "user" in commands

    def test_invoice_in_commands_list(self):
        result = self.runner.invoke(cli.main)

        commands = self.extract_commands_list(result.output)
        assert "invoice" in commands

    def test_config_in_commands_list(self):
        result = self.runner.invoke(cli.main)

        commands = self.extract_commands_list(result.output)
        assert "config" in commands
