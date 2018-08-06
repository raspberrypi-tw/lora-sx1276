#!/usr/bin/python3
# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2016, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# packer.py
# A demo program for lora to send message compatible with python2/3
#
# Author : sosorry
# Date   : 10/03/2017
#

import sys
import codecs
import binascii

SOH  = "01"    # 0x01
ACK  = "06"    # 0x06
#CRLF = "\r\n"  # 0x32 0x41 0x33 0x31
CRLF = "43524C46"  # CRLF \r\n

#
# pack string to customized payload
#
# payload: [SOH]    [LENGTH]   [PAYLOAD]          [CRLF]
#          2 bytes  6 bytes    length * 2 bytes   4 bytes
#
def Pack_Str(string):
    try:
        # python2
        data   = string.encode("hex")
    except:
        # python3
        data = string.encode('utf-8')

    length = len(data)

    if length < 10:
        length = str(0) + str(0) + str(length)
    elif length >= 10 and length < 100:
        length = str(0)  + str(length)
    else:
        length = str(length)

    try:
        # python2
        payload = SOH + length.encode("hex") + data + CRLF
    except:
        # python3
        payload = bytes(SOH, 'utf-8') + str(length).encode(encoding='utf-8') + data + bytes(CRLF, 'utf-8')

    return [length, payload]


#
# unpack payload to string
#
def Unpack_Str(string):
    try:
        # python2
        soh    = string[0:1]
        length = int((string[2:8]).decode("hex")) /2
        #data   = (string[8:-2]).decode("hex")
        data   = (string[8:-8]).decode("hex")
    except:
        # python3
        soh    = string[0:2]
        length = string[2:5]
        data   = string[5:-8]

    return [length, data]

