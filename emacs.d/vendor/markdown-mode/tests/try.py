import paho.mqtt.client as mqtt
import json
import uuid
import calendar
from time import sleep
from datetime import datetime
import time



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("efergy/log")
    print("rc: " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    message = msg.payload.decode("utf-8")
    print(message)
    d = json.loads(message)
    print(d['message'])
    print(d['correlationid'])


def on_publish(client, userdata, mid):
    print("Published: " + str(mid))

def on_subscribe(client, userdata, mid, grantedqos):
    print("Subscribed: " + str(mid) + " " + str(grantedqos))

def on_log(client, userdata, level, string):
    print(string)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.on_subscribe = on_subscribe
client.on_log = on_log
current_time = datetime.now()


client.connect("192.168.0.103", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
