from vendors.pushbullet.pushbullet import PushBullet
from twilio.rest import TwilioRestClient
import smtplib
import configuration


class alerts(object):

    """docstring for alerts"""

    def __init__(self):
        self.config = configuration.load()
        self.register()

    def register(self):
        alerts = self.config['alerts']
        alerts_list = []

        if alerts['sms']['on']:
            alerts_list.append(alerts.sms(alerts['sms']))

        if alerts['pushbullet']['on']:
            alerts_list.append(alerts.pushbullet(alerts['pushbullet']))

        if alerts['email']['on']:
            alerts_list.append(alerts.sms(alerts['pushbullet']))

        self.alerts = alerts_list

    def send(self, message):

        for alert in self.alerts:
            alert.send_notification(message)


class basic_alert(object):

    """docstring for basic_alert class. This is more an interface/contract
     than anything else"""

    def __init__(self, config):
        self.config = config
        self.setup()

    def setup(self):
        pass

    def send_notification(self, message):
        pass


class email(basic_alert):

    """docstring for email"""

    def setup(self):

        self.sender = self.config['email_sender']
        self.receivers = self.config['email_receivers']
        self.server = self.config['server']

    def send_notification(self, message):

        email_body = """From: Alert <%s>
        To: Alert <%s>
        Subject: %s

        This is a test e-mail message.
        """ % (self.sender, self.receivers, message)

        try:
            smtpObj = smtplib.SMTP(self.server)
            smtpObj.sendmail(self.sender, self.receivers, email_body)
            print "Successfully sent email"
        except SMTPException:
            print "Error: unable to send email"


class pushbullet(basic_alert):

    """docstring for pushbullet. Get you api key from
    https://www.pushbullet.com/account

        Use the pyPushBullet API to know which deviceID to use.
    """

    def setup(self):

        self.push = PushBullet(self.config['apikey'])

    def send_notification(self, message):

        for device in self.config['device']:
            self.push.pushNote(device, message, message)

    def get_device_id(self):
        print self.push.getDevices()


class sms(basic_alert):

    """docstring for sms, uses your twilio.com account."""

    def setup(self):
        # Your Account Sid and Auth Token from twilio.com/user/account
        account_sid = self.config['twilio_sid']
        auth_token = self.config['twilio_auth_token']
        self.client = TwilioRestClient(account_sid, auth_token)

    def send_notification(self, message):
        message = self.client.sms.messages.create(body=message,
                                             to=self.config['to_number'],
                                             from_=self.config["from_number"])
