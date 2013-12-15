import raspzmq.alerts as alerts
import configuration


def test_pushbullet():
    config = configuration.load()
    p = alerts.pushbullet(config['alerts']['pushbullet'])
    p.send_notification('This is a test.')


def test_sms():
    config = configuration.load()
    s = alerts.sms(config['alerts']['sms'])
    s.send_notification('This is a test.')


def test_email():
    config = configuration.load()
    e = alerts.email(config['alerts']['email'])
    e.send_notification('This is a test.')
