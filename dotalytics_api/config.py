import configparser
import asyncio

config = None


async def get(key: str, section: str = 'DEFAULT'):
    global config
    if config is None:
        config = await configparser.ConfigParser()
        config.read('config.ini')

    return config.get(section, key)
