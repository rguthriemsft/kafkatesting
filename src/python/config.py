"""Connection configuration pointing to a Kafka cluster"""
from configparser import ConfigParser
import os

class Configuration:
    """Simplifies access to configuration file"""

    _config_parser = ConfigParser()

    def __init__(self):

        with open('src/python/config.ini') as file_handler:
            self._config_parser.read_file(file_handler)
            self.default = dict(self._config_parser['default'])
            self.consumer = dict(self._config_parser['consumer'])
            self.consumer.update(self.default)
            self.custom = dict(self._config_parser['custom_config'])
