#!/usr/bin/env python

"""_test_alerts.py, tests the alerts. The underscore for the
nosetest default scanner to ignore it
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

import raspzmq.alerts as alerts
import configuration


def test_pushbullet():
    config = configuration.load()
    p = alerts.AlertPushBullet(config['alerts']['AlertPushBullet'])
    p.send_notification('This is a test.')


def test_sms():
    config = configuration.load()
    s = alerts.AlertSMS(config['alerts']['AlertSMS'])
    s.send_notification('This is a test.')


def test_email():
    config = configuration.load()
    e = alerts.AlertEmail(config['alerts']['AlertEmail'])
    e.send_notification('This is a test.')
