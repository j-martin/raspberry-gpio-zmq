#!/usr/bin/env python

"""demo_client.py, runs raspzmq/client.py
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

import raspzmq.client as client

s = client.Subscriber(config_path="./config/")
s.run()  # Simple infinite look so the client keep running
