import zmq
from logger import logger
import sys
import time
import config

try:
    import RPi.GPIO as GPIO
except ImportError:
    logger.critical('RPi.GPIO module not found. Are you on a RaspberryPi?')
    exit()


config = config.load()
logger.name = __name__.upper()

class polling(object):

    """docstring for polling inputs of the GPIO. The channels should be specified."""

    def __init__(self, channels=[24, 26], port="5556"):
        super(polling, self).__init__()
        self.channels = channels
        self.register_server(port=port)
        self.register_channels()

    def event_callback(self, channel):
        """Function that runs when an input changes."""

        if GPIO.input(channel) == 1:
            message = ('%s has been closed.' % channel)

        else:
            message = ('%s has been opened.' % channel)

        logger.info(message)
        self.socket.send("%d %s" % (channel, message))

    def register_server(self, port="5556"):

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind("tcp://*:%s" % port)
        logger.info('Server on port %s ready!' % port)

    def register_channels(self):

        GPIO.setmode(GPIO.BOARD)
        for channel in self.channels:
            GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(
                channel, GPIO.BOTH, callback=self.event_callback)
        logger.info('GPIO Channels ready!')
        return 0

    def run(self):
        """Infinite loop"""
        while True:
            time.sleep(60)

if __name__ == '__main__':
    m = polling()
    m.run()
