import sys
import zmq
from time import sleep
import logger
import configuration

log = logger.create('CLIENT')

class subscriber(object):

    """docstring for subscriber"""

    def __init__(self):
        super(subscriber, self).__init__()

        self.config = configuration.load()
        log = logger.create('client')

    def connect(self):

        server = self.config['server']
        port = self.config['port']

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)

        log.info("Collecting updates from server...")
        self.socket.connect("tcp://%s:%s" % (server, port))

        topicfilter = "26"
        self.socket.setsockopt(zmq.SUBSCRIBE, topicfilter)
    
    def run(self):
        while 1:
            log.info(self.socket.recv())
            sleep(5)

if __name__ == '__main__':
    sub = subscriber()
    sub.connect()
    sub.run()
