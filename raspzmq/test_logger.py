#!/usr/bin/env python

"""raspberry-gpio-zmq
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

import raspzmq.logger
import os


def test_the_logger():

    log = raspzmq.logger.create('test')

    log.debug('debug message')
    log.info('info message')
    log.warn('warn message')
    log.error('error message')
    log.critical('critical message')
