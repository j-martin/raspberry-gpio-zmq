#!/usr/bin/env python

"""test_config.py, test configuration.py
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

import raspzmq.configuration


def test_load():
    config = raspzmq.configuration.load('./config/')

    assert (len(config) > 3)
