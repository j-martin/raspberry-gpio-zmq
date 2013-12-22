#!/usr/bin/env python

"""client.py basic ZMQ client that connects to the server.
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

from time import sleep

import zmq

import logger
import configuration


class Subscriber(object):
    """<ac:image ac:thumbnail="true" ac:width="300">for subscriber"""

    def __init__(self, config_path="./config/"):
        super(Subscriber, self).__init__()

        self.config = configuration.load(config_path)
        self.log = logger.create('CLIENT')
        self.connect()

    def connect(self):

        server = self.config['server_hostname']
        port = self.config['port_zmq']

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)

        self.log.info("Client Started - Waiting for server...")
        try:
            self.socket.connect("tcp://%s:%s" % (server, port))
        except zmq.error.ZMQError:
            # Hack for Travis-CI
            self.socket.connect("tcp://localhost:%s" % ( port))
        self.socket.setsockopt(zmq.SUBSCRIBE, "")

    def run(self):
        while 1:
            self.log.info(self.socket.recv())
            sleep(1)


if __name__ == '__main__':
    sub = Subscriber()
    sub.run()
