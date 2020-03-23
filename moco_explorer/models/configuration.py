import json

from os import unlink


class Configuration(object):

    def __init__(self, config_path):
        """
        Class constructor

        :param config_path: file path to the configuration json file
        """
        self.config_path = config_path

        self.config = None
        self.needs_authentication = True

    def load(self):
        """
        Load the current configuration file as dictionary
        """
        config = None
        with open(self.config_path, "r") as fp:
            config = json.load(fp)

        self.config = config

        if "password" in self.config.keys():
            self.needs_authentication = True

        if "api_key" in self.config.keys():
            self.needs_authentication = False

    def get(self, key):
        """
        Get a configuration value from the config file, by specified key

        :param key: Key for the value to retrieve
        :return: The value
        """

        if self.config is None:
            self.load()

        return self.config[key]

    def create(self, api_key, domain):
        """
        Creates a new config file

        :param api_key: Api key
        :param domain: Api domain path

        .. note:: An existing configuration file will be overwritten
        """
        config = {
            "api_key": api_key,
            "domain": domain
        }

        with open(self.config_path, "w") as fp:
            json.dump(config, fp)

        self.config = None

    def create_account_auth(self, email, password, domain):
        """
        Creates the configuration file with user authentication information

        :param email: Users email address
        :param password: Users password
        :param domain: Api domain path

        .. note:: This file will be overwritten once authentication was successfull
        """
        config = {
            "email": email,
            "password": password,
            "domain": domain
        }

        with open(self.config_path, "w") as fp:
            json.dump(config, fp)

        self.config = None

    def delete(self):
        unlink(self.config_path)
