#!/usr/bin/env python

"""demo_server.py, runs raspzmq/server.py
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

import raspzmq.server as server

s = server.Publisher(config_path="./config/")
s.run() #Simple infinite look so the server keep running