#!/usr/bin/python3
# -*- coding:utf-8 -*-

import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 5000000 

RegFrMsb = 0x06
RegFrMid = 0x07
RegFrLsb = 0x08
Value    = 0

msb = spi.xfer([RegFrMsb & 0x7F, Value])[1]
mid = spi.xfer([RegFrMid & 0x7F, Value])[1]
lsb = spi.xfer([RegFrLsb & 0x7F, Value])[1]
f = lsb + 256*(mid + 256*msb)
print(f / 16384.0)

spi.close()
