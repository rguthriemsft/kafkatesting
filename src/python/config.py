"""Connection configuration pointing to a Kafka cluster"""
from configparser import ConfigParser
import os

class Configuration:
    """Simplifies access to configuration file"""

    _config_parser = ConfigParser()

    def __init__(self):

        with open('src/python/config.ini') as file_handler:
            self._config_parser.read_file(file_handler)
            self.consumer = dict(self._config_parser['consumer'])
            self.consumer.update(dict(self._config_parser['default']))
            self.producer = dict(self._config_parser['producer'])
            self.producer.update(dict(self._config_parser['default']))
            self.custom = dict(self._config_parser['custom_config'])
            print(self.consumer)
            print(self.producer)
            print(self.custom)