#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://www.thethingsnetwork.org/docs/applications/mqtt/api.html

#import ConfigParser
import socket
import random
import time
from ttn_var import *

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# 01, 67, c6, 00 in the beginning(PROTOCOL_VERSION[0] + RANDOM[1-2] + PKT_PUSH_DATA[3])
while True:
    TIME = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    pkt = ('{"stat":{\
"time":"' + str(TIME) + ' GMT",\
"lati":'  + str(LATI) + ',\
"long":'  + str(LONG) + ',\
"alti":'  + str(ALTI) + ',\
"rxnb":'  + str(RXNB) + ',\
"rxok":'  + str(RXOK) + ',\
"rxfw":'  + str(RXFW) + ',\
"ackr":'  + str(ACKR) + ',\
"dwnb":'  + str(DWNB) + ',\
"txnb":'  + str(TXNB) + ',\
"pfrm":"' + str(PFRM) + '",\
"mail":"' + str(MAIL) + '",\
"desc":"' + str(DESC) + '"\
}}').encode('utf-8')


    print("--------------------------------")
    print(pkt)

    sock.sendto(x + pkt, (UDP_IP, UDP_PORT))
    time.sleep(15)
