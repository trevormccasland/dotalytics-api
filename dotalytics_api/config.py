import configparser
import asyncio

config = None


def get(key: str, section: str = 'DEFAULT'):
    global config
    if config is None:
        config = configparser.ConfigParser()
        config.read('config.ini')
    return config.get(section, key)
