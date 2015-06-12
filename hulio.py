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

# Connect to the Hue Bridge and start Flask
hue = Bridge(hue_bridge_IP)
#hue.connect()
app = Flask(__name__)

def hue_change(colour_name):
    hue.set_light(1, 'on', True)
    hue.set_light(1, 'bri', 254)
    hue.set_light(1, 'sat', 254)
    if colour_name == "RED":
        hue.set_light(1, 'hue', 0)
    if colour_name == "ORANGE":
        hue.set_light(1, 'hue', 5000)
    if colour_name == "GREEN":
        hue.set_light(1, 'hue', 24000)
    if colour_name == "BLUE":
        hue.set_light(1, 'hue', 46603)
    if colour_name == "RESET" or colour_name == "WHITE":
        hue.set_light(1, 'hue', 14922)
        print("Resetting light")
    return

@app.route("/", methods=['GET', 'POST'])
def colour_sms_vote():
    """Control the Hue lights with sms via Twilio."""
 
    payload_msg = request.form.get('Body')
    vote = payload_msg.strip().upper()
    print(vote)
    hue_change(vote)

    resp = twilio.twiml.Response()
    resp.message("Got it! -Robot Andrew")
    return str(resp)
 
if __name__ == "__main__":
    #app.run(debug=True)
    #app.run(host='140.184.27.192',port=5000)
    app.run(host='192.168.1.107',port=5000)
