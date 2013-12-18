#!/usr/bin/env python

"""demo_server.py, runs raspzmq/server.py
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

import raspzmq.server as server, server_web

s = server.Publisher(config_path="./config/")
w = server_web.run(config_path="./config/")