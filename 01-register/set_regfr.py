#!/usr/bin/python3
# -*- coding:utf-8 -*-

import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 5000000 

RegFrMsb = 0x06

def set_freq(f):
    i = int(f * 16384.)    # choose floor
    msb = i // 65536
    i -= msb * 65536
    mid = i // 256 
    i -= mid * 256 
    lsb = i 
    return spi.xfer([RegFrMsb | 0x80, msb, mid, lsb])

def get_freq():
    msb, mid, lsb = spi.xfer([0x06 & 0x7F, 0, 0, 0])[1:]
    f = lsb + 256*(mid + 256*msb)
    return f / 16384.

set_freq(868)
print(get_freq())

spi.close()
