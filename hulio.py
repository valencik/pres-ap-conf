from flask import Flask, request, redirect
import twilio.twiml
from phue import Bridge
import yaml

# Import tokens and settings from configuration file
conf = open('config.yaml')
dataMap = yaml.safe_load(conf)
conf.close()
account_sid = dataMap['account_sid']
auth_token  = dataMap['auth_token']
hue_bridge_IP= dataMap['hue_bridge_IP']

# Connect to the Hue Bridge
hue = Bridge(hue_bridge_IP)
#hue.connect()
 
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def colour_sms_vote():
    """Control the Hue lights with sms via Twilio."""
 
    payload_msg = request.form.get('Body')
    vote = payload_msg.strip().upper()
    print(vote)
    if vote == "RED":
        hue.set_light(1, 'on', True)
        hue.set_light(1, 'hue', 0)
        hue.set_light(1, 'bri', 254)
        hue.set_light(1, 'sat', 254)
        print("Changing light to RED")
    if vote == "BLUE":
        hue.set_light(1, 'on', True)
        hue.set_light(1, 'hue', 46603)
        hue.set_light(1, 'bri', 254)
        hue.set_light(1, 'sat', 254)
        print("Changing light to BLUE")
    if vote == "RESET" or vote == "WHITE":
        hue.set_light(1, 'on', True)
        hue.set_light(1, 'hue', 14922)
        hue.set_light(1, 'bri', 254)
        hue.set_light(1, 'sat', 144)
        print("Resetting light")

    resp = twilio.twiml.Response()
    resp.message("Got it!")
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
