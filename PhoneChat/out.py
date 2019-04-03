#SEND DATA TO CALLER
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = open('sID.txt',"r").read().strip()
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+15558675310',
                        from_='+15017122661'
                    )

print(call.sid)
