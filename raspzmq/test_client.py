#!/usr/bin/env python

"""test_client.py, testing client.py
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

import raspzmq.client


def test_starting_the_client():
    m = raspzmq.client.Subscriber('./config/')

    print(dir(m))
