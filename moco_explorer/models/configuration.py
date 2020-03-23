import json


class Configuration(object):

    def __init__(self, config_path):
        """
        Class constructor

        :param config_path: file path to the configuration json file
        """
        self.config_path = config_path

        self.config = None

    def load(self):
        """
        Load the current configuration file as dictionary
        """
        config = None
        with open(self.config_path, "r") as fp:
            config = json.load(fp)

        self.config = config

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
