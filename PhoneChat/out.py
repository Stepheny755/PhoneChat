#SEND DATA TO CALLER

from util import Util
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

class Out():

    def __init__(self):
        self.account_sid = open('sID.txt',"r").read().strip()
        self.auth_token = open('token.txt',"r").read().strip()
        self.client = Client(self.account_sid, self.auth_token)

    def call(self,fr,to,url):
        call = self.client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to=str(to),
                        from_=str(fr),
                    )
        return call

o = Out()
print(o.call("+17788006793","+17788914659","").sid)
