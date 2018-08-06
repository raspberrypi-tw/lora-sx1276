#!/usr/bin/python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
from ttn_var import *

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: {}".format(str(rc)))
    client.subscribe("+/devices/#")

def on_message(client, userdata, msg):
    print("topic: {}, message: {}".format(msg.topic, str(msg.payload)))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(user, password)
client.connect(ttn_router, 1883, 60)

client.loop_forever()

