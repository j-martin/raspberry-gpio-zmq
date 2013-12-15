# Raspberry-GPIO-ZMQ
Linking realworld input from a RaspberryPi to the interwebs!

Monitors the GPIO events (on/off) of the RaspberryPi (may work on other device with some work) and notifies clients via ZMQ (client.py), email, sms (text) or pushbullet (push to Android, Chrome and iOS (planned)).

It can be used for example as an adhoc security system or anything really.

## Setup

- Configure the config/general.json file to match your setup.
- Configure the config/mapping.json file to match how how your GPIO is connected to your device(s). The default file is configured as if it was connected to the sensor of an alarm system.

- Copy the files on both the server and the client(s).
- Run "pip install -r requirements.txt" on both. On some systems you may have to install PyZMQ manually or with another package manager.
- Run "sudo python demo_server.py". The server needs to run as ROOT to access the GPIO interface, unless you configure your server differently.
- Run "python demo_client.py" on the client(s).

## Depedencies
See requirements.txt

## Todo

- Implementing a webserver (Flask) to see the logs.