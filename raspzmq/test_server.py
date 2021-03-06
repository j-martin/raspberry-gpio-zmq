#!/usr/bin/env python

"""raspberry-gpio-zmq
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

import raspzmq.server


class fakeGPIO(object):
    """<ac:image ac:thumbnail="true" ac:width="300">for fakeGPIO so tests can be run on somehting
    else than a RaspberryPi"""

    def __init__(self):
        self.BOARD = 1
        self.IN = 1
        self.BOTH = 1
        self.PUD_DOWN = 1

    def setup(self, mapping, value, pull_up_down, *kargs):
        return 0

    def setmode(self, *kargs):
        return 0

    def add_event_detect(self, channel, value, callback, *kargs):
        return 0

    def input(self, *kargs):
        return 0

    def setmode(self, *kargs):
        return 0

    def setmode(self, *kargs):
        return 0


def test_starting_the_server():
    raspzmq.server.GPIO = fakeGPIO()
    m = raspzmq.server.Publisher()
