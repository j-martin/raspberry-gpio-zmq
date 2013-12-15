from os import path
from json import loads


def load(config_path):

    config_path += 'general.json'

    if path.isfile(config_path):
        data = open(config_path).read()
        return loads(data)

    else:
        print 'Config file not found: %r' % config_path
        exit
