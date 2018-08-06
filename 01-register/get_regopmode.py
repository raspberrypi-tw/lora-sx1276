#!/usr/bin/python3
# -*- coding:utf-8 -*-

import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 5000000 

RegOpMode = 0x01
Value     = 0

# Read
ret = spi.xfer([RegOpMode & 0x7F, Value])[1]
print(ret)         # 128
print(ret >> 7)    # 1

spi.close()

