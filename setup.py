from distutils.core import setup

setup(
    name='raspberry-gpio-zmq',
    version='0.10',
    packages=['raspzmq', 'raspzmq.vendors', 'raspzmq.vendors.AlertPushBullet'],
    url='https://github.com/j-martin/raspberry-gpio-zmq',
    license='MIT',
    author='Jean-Martin Archer',
    author_email='raspzmq@jmartin.ca',
    description='Monitors the GPIO events (on/off) of the RaspberryPi (may work on other device with some work) and notifies clients via ZMQ (client.py), AlertEmail, AlertSMS (text) or AlertPushBullet (push to Android, Chrome and iOS (planned)).'
)
