#!/usr/bin/env python

"""logger.py, basic logger configuration.
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

import logging
import os
import logging.handlers


def create(name, log_path="./logs/"):

    mkpath(log_path)

    log_filename = log_path + name.lower() + '.log'

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    console_output = logging.StreamHandler()
    console_output.setLevel(logging.DEBUG)

    file_output = logging.handlers.TimedRotatingFileHandler(
        log_filename, when="D", interval=1, backupCount=7)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_output.setFormatter(formatter)
    console_output.setFormatter(formatter)

    logger.addHandler(console_output)
    logger.addHandler(file_output)

    return logger


def mkpath(path):

    if not os.path.isdir(path):
        try:
            os.mkdir(path)
        except:
            print 'Log creation (directory) failed.'
            return 1

    return 0
