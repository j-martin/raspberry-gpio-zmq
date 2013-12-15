import sys
import zmq
from time import sleep
import logger
import configuration

log = logger.create('CLIENT')


class subscriber(object):

    """docstring for subscriber"""

    def __init__(self, config_path = "./config/"):
        super(subscriber, self).__init__()

        self.config = configuration.load(config_path)
        self.log = logger.create('CLIENT')
        self.connect()

    def connect(self):

        server = self.config['server']
        port = self.config['port']

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)

        self.log.info("Client Started - Waiting for server...")
        self.socket.connect("tcp://%s:%s" % (server, port))

        self.socket.setsockopt(zmq.SUBSCRIBE, "")

    def run(self):
        while 1:
            self.log.info(self.socket.recv())
            sleep(1)

if __name__ == '__main__':
    sub = subscriber()
    sub.run()
