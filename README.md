# Raspberry-GPIO-ZMQ

Monitors 

Linking realworld input from a RaspberryPi to the interwebs!

## Setup

- Configure the config/general.json file to match your setup.
- Configure the config/mapping.json file to match how how your GPIO is connected to your device(s). The default file is configured as if it was connected to the sensor of an alarm system.

- Copy the files on both the server and the client(s).
- Run "pip install -r requirements.txt" on both.
- Run "sudo python raspzmq/server.py". The server needs to run as ROOT to access the GPIO interface, unless you configure your server differently.
- Run "python raspzmq/client.py" on the client(s).

## Todo

- Implementing a webserver (Flask) to see the logs.