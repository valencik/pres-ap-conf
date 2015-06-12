from twilio.rest import TwilioRestClient
import yaml
 
# Import Sid and Auth Token from configuration file
conf = open('config.yaml')
dataMap = yaml.safe_load(conf)
conf.close()
account_sid = dataMap['account_sid']
auth_token  = dataMap['auth_token']

client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hello World!",
    to="+15051234567",    # Replace with your phone number
    from_="+15051234567") # Replace with your Twilio number
print(message.sid)
