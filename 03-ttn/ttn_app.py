#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys 
sys.path.insert(0, '../')
import LoRaWAN
from LoRaWAN.MHDR import MHDR
from LoRaWAN.PhyPayload import PhyPayload
from LoRaWAN.MHDR import MHDR
import time
import base64
import socket
from ttn_var import *

# initialize socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# initialize LoRaWAN packet
lorawan = PhyPayload(NWS_KEY, APPS_KEY)

try:
    while True:
        # accept input from keyobard
        rawinput = input("Send data to TTN >>> ")
        lorawan.create(MHDR.UNCONF_DATA_UP, {'devaddr': DEV_ADDR, 'fcnt': 1, 'data': list(map(ord, rawinput)) })
        raw = lorawan.to_raw()
        raw_bytes = bytearray(raw)
        raw_b64 = base64.b64encode(raw_bytes).decode('utf-8')

        TIME = int(time.strftime("%s"))

        pkt = ('{"rxpk":[{\
"tmst":'  + str(TIME) + ',\
"chan":'  + str(CHAN) + ',\
"rfch":'  + str(RFCH) + ',\
"freq":'  + str(FREQ) + ',\
"stat":'  + str(STAT) + ',\
"modu":"' + str(MODU) + '",\
"datr":"' + str(DATR) + '",\
"codr":"' + str(CODR) + '",\
"lsnr":'  + str(LSNR) + ',\
"rssi":'  + str(RSSI) + ',\
"size":'  + str(SIZE) + ',\
"data":"' + raw_b64 + '"}]}').encode('utf-8')

        print("--------------------------------")
        print(pkt)

        sock.sendto(x + pkt, (UDP_IP, UDP_PORT))
        time.sleep(15)

except KeyboardInterrupt:
    sys.stdout.flush()
    print("")
    sys.stderr.write("KeyboardInterrupt\n")
finally:
    sys.stdout.flush()
    time.sleep(.5)
    
