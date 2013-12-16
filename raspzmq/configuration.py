#!/usr/bin/env python

"""configuration.py, loads the general configuration
for both the server and the client.
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

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
