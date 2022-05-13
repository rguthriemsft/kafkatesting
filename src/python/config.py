"""Connection configuration pointing to a Kafka cluster"""
from configparser import ConfigParser

class Configuration:
    """Simplifies access to configuration file"""

    config_parser = ConfigParser()


    def __init__(self):
        self.config_parser.read_file('config.ini')

    def default(self):
        """Returns the 'default' section of the configuration"""
        return dict(self.config_parser['default'])

    def consumer(self):
        """Returns the 'consumer' section of the configuration"""
        return dict(self.config_parser['consumer'])
