#!/usr/bin/python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import json
import base64
from ttn_var import *

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: {}".format(str(rc)))
    client.subscribe("+/devices/#")

def on_message(client, userdata, msg):
    #print("topic: {}, message: {}".format(msg.topic, str(msg.payload)))
    jdict = json.loads( str(msg.payload, 'utf-8') )
    mtime = jdict['metadata']['time']
    dev_id = jdict['dev_id']
    payload_raw = jdict['payload_raw']
    payload_plain = base64.b64decode(jdict['payload_raw'])
    print("time:{}, dev_id:{}".format(mtime, dev_id))
    print("payload_raw:{}, payload_decode:{}".format(payload_raw, payload_plain))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(user, password)
client.connect(ttn_router, 1883, 60)

client.loop_forever()

