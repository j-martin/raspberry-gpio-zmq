# Raspberry-GPIO-ZMQ

[![Build Status](https://travis-ci.org/j-martin/raspberry-gpio-zmq.png?branch=master)](https://travis-ci.org/j-martin/raspberry-gpio-zmq)

Linking realworld input from a RaspberryPi to the interwebs!

Monitors the GPIO events (on/off) of the RaspberryPi (may work on other device with some work) and notifies clients via ZMQ (client.py), email, sms (text) or pushbullet (push to Android, Chrome and iOS (planned)). It also feature a webserver (Flask) to check the logs.

![Screenshot](https://raw.github.com/j-martin/raspberry-gpio-zmq/master/static/img/screenshot.png)

It can be used for example as an ad-hoc security system or anything really.

This project has been tested against Python 2.6 and 2.7 only.

## Setup

- Clone the repo: "git clone git@github.com:j-martin/raspberry-gpio-zmq.git"
- Configure the config/general.json file to match your setup.
- Configure the config/mapping.json file to match how how your GPIO is connected to your device(s). The default file is configured as if it was connected to the sensor of an alarm system.

- Copy the files on both the server and the client(s).
- Run "pip install -r requirements.txt" on both. On some systems you may have to install PyZMQ manually or with another package manager.
- Run "sudo python demo_server.py & python demo_server_web.py". The server needs to run as ROOT to access the GPIO interface, unless you configure your server differently.
- Run "python demo_client.py" on the client(s).
- Once launched, the server's web interface can be access at serverip:5001.

## Dependencies
See requirements.txt

## Configuration

### config/general.json

"server_hostname" is the name of the RaspberryPi server (used by the client);
"port_zmq", it's port
"port_http", the port of the http server
"host_http", the host address the http server will serve. By default every interface. You might want to change this.
"log_path", where the logs are stored (used by the main server, the client and the web/log server)
"credentials", of the web/log server.

```json
{
  "server_hostname": "raspberrypi",
  "port_zmq": "45678",
  "port_http": "5001",
  "host_http": "0.0.0.0",
  "log_path": "./logs/",
  "credentials": {
    "username": "admin",
    "password": "secrets"
  },
  "alerts": {
    "sms": {
      "on": false,
      "twilio_sid": "enter_your_sid",
      "twilio_auth_token": "enter_your_authtoken",
      "from_number": "the-num-ber",
      "to_number": "the-num-ber"
    },
    "pushbullet": {
      "on": false,
      "apikey": "enter_your_apikey",
      "device": [
        "enteryour device id, six number"
      ]
    },
    "email": {
      "on": false,
      "server": "foo@bar.com:25",
      "email_sender": "me@me.com",
      "email_receivers": [
        "you@you.com"
      ]
    }
  }
}
```

### config/mapping.json

The "pin" (int) number is the RaspberryPi GPIO pin that the sensor or switch is connected to. The "sensor" is the name that server will report. The "state" is the name of the states. Here a value of 0 -> "closed", and a 1 -> "open".

```json
  {
    "pin": 3,
    "sensor": "Door Front",
    "state": [
      "closed",
      "open"
    ]
  },
```

## Compatibility
- Server
-- Raspbian (Linux pi 3.10.23+ #608 PREEMPT)
- Client (zmq)
-- Windows 8.1
-- MacOS X 10.9
-- Ubuntu 13.10
