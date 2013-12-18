#!/usr/bin/env python

"""demo_server_web.py, runs raspzmq/server_web.py
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

import raspzmq.server_web as server_web

w = server_web.run(config_path="./config/")
