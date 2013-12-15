import zmq
import sys
import time
import alerts
import logger
import configuration

try:
    import RPi.GPIO as GPIO
except ImportError:
    print('RPi.GPIO module not found. Are you on a RaspberryPi?')
    exit()


class publisher(object):

    """docstring for publisher inputs of the GPIO. The channels should be specified."""

    def __init__(self, channels=[24, 26]):
        super(publisher, self).__init__()

        self.config = configuration.load()

        self.register_logger()

        self.channels = channels
        self.register_server()
        self.register_channels()
        self.register_alerts()

        log.info('The server is ready!')

    def register_logger(self):
        log_path = self.config['general']['log_path']
        self.log = logger.create(name='SERVER', log_path=log_path)

    def event_callback(self, channel):
        """Function that runs when an input changes."""

        if GPIO.input(channel) == 1:
            message = ('%s has been closed.' % channel)

        else:
            message = ('%s has been opened.' % channel)

        log.warn(message)
        self.socket.send("%d %s" % (channel, message))
        self.send_alerts()

    def register_alerts(self):
        alerts = self.config['alerts']
        alerts_list = []

        if alerts['sms']['on']:
            alerts_list.append(alerts.sms(alerts['sms']))

        if alerts['pushbullet']['on']:
            alerts_list.append(alerts.pushbullet(alerts['pushbullet']))

        if alerts['email']['on']:
            alerts_list.append(alerts.sms(alerts['pushbullet']))

        self.alerts = alerts_list

    def send_alerts(self, message):

        for alert in self.alerts:
            alert.send_notification(message)

        log.info('Notification sent!')

    def register_server(self):
        server = self.config['general']['server']
        port = self.config['general']['port']

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind("tcp://*:%s" % port)
        log.info('Server on port %s ready!' % port)

    def register_channels(self):

        GPIO.setmode(GPIO.BOARD)
        for channel in self.channels:
            GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(
                channel, GPIO.BOTH, callback=self.event_callback)
        log.info('GPIO Channels ready!')
        return 0

    def run(self):
        """Infinite loop"""
        while True:
            time.sleep(60)

if __name__ == '__main__':
    m = publisher()
    m.run()
