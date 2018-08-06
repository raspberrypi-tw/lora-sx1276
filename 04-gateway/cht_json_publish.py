#!/usr/bin/python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import numpy as np
import time
import json

host = "iot.cht.com.tw"

# change "DEVICE_NUMBER" to real number
topic = "/v1/device/<DEVICE_NUMBER>/rawdata"
print(topic)

# change "API_KEY" to real api key
user, password = "<API_KEY>", "<API_KEY>"

client = mqtt.Client()
client.username_pw_set(user, password)
client.connect(host, 1883, 60)

for i in range(100):
    v = str(int( np.random.random() *100))
    t = str(time.strftime("%Y-%m-%dT%H:%M:%S"))

    # change "SID" to real name
    payload = [{"id":"<SID>","value":[v], "time":t}]
    print(payload)
    client.publish(topic, "%s" % ( json.dumps(payload) ))
    time.sleep(1)

