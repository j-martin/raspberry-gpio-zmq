import RPi.GPIO as GPIO
import time


class monitor(object):

    """docstring for monitor inputs of the GPIO. The channels should be specified."""

    def __init__(self, channels=[24, 26]):
        super(monitor, self).__init__()
        self.channels = channels
        self.register_channels()

    def event_callback(self, channel):
        """Function that runs when an input changes."""

        if GPIO.input(channel) == 1:
            print('%s has been closed.' % channel)
        else:
            print('%s has been opened.' % channel)

    def register_channels(self):

        GPIO.setmode(GPIO.BOARD)
        for channel in self.channels:
            GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            GPIO.add_event_detect(
                channel, GPIO.BOTH, callback=self.event_callback)
        return 0

    def run(self):
        """Infinite loop"""
        while True:
            time.sleep(60)

if __name__ == '__main__':
    m = monitor()
    m.run()
