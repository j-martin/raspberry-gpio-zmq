import zmq
import sys
import time
import alerts
import logger
import configuration
import mapping

try:
    import RPi.GPIO as GPIO
except ImportError:
    print('RPi.GPIO module not found. Are you on a RaspberryPi?')
    exit()


class publisher(object):

    """docstring for publisher inputs of the GPIO. The channels should be specified."""

    def __init__(self):
        super(publisher, self).__init__()

        self.config = configuration.load()
        self.mapping = mapping.mapping()

        self.register_logger()

        self.channels = self.mapping.get_channels()
        self.register_zmq_server()
        self.register_channels()
        self.alerts = alerts.alerts()

        self.log.info('The server is ready!')

    def register_logger(self):
        log_path = self.config['log_path']
        self.log = logger.create(name='SERVER', log_path=log_path)

    def event_callback(self, channel):
        """Function that runs when an input changes."""

        message = mapping.get_message(channel, GPIO.input(channel))
        self.log.warn(message)
        self.zmq_socket.send("%d %s" % (channel, message))
        self.alerts.send(message)

    def register_zmq_server(self):
        port = self.config['port']

        self.context = zmq.Context()
        self.zmq_socket = self.context.socket(zmq.PUB)
        self.zmq_socket.bind("tcp://*:%s" % port)
        self.log.info('Server on port %s ready!' % port)

    def close_zmq_server(self):
        port = self.config['port']
        self.zmq_socket.unbind("tcp://*:%s" % port)
        self.log.info('Server on port %s has been closed!' % port)

    def register_channels(self):

        GPIO.setmode(GPIO.BOARD)
        for channel in self.channels:
            GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(
                channel, GPIO.BOTH, callback=self.event_callback)
        self.log.info('GPIO Channels ready!')
        return 0

    def run(self):
        """Infinite loop"""
        while True:
            time.sleep(60)

if __name__ == '__main__':
    m = publisher()
    m.run()
