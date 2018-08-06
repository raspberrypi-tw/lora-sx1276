#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" A simple beacon transmitter class to send a 1-byte message (0x0f) in regular time intervals. """
# Copyright 2015 Mayer Analytics Ltd.
#
# This file is part of pySX127x.
#
# pySX127x is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# pySX127x is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You can be released from the requirements of the license by obtaining a commercial license. Such a license is
# mandatory as soon as you develop commercial activities involving pySX127x without disclosing the source code of your
# own applications, or shipping pySX127x with a closed source product.
#
# You should have received a copy of the GNU General Public License along with pySX127.  If not, see
# <http://www.gnu.org/licenses/>.


from time import sleep
import json
import packer
import time
import sys
sys.path.insert(0, '../')
from SX127x.LoRa import *
from SX127x.board_config import BOARD
import numpy as np

BOARD.setup()

try:
    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass


class LoRaBeacon(LoRa):
    def __init__(self, verbose=False):
        super(LoRaBeacon, self).__init__(verbose)
        self.set_mode(MODE.SLEEP)
        #self.set_dio_mapping([0,0,0,0,0,0])    # RX
        self.set_dio_mapping([1,0,0,0,0,0])    # TX
        self._id = "NODE_01"
        self.rx_done = False

    def on_rx_done(self):
        print("\nRxDone")

        payload = self.read_payload(nocheck=True)
        data = ''.join([chr(c) for c in payload])
        print("Time: {}".format(str(time.ctime())))
        print("Raw RX: {}".format(data))

        try:
            _length, _data = packer.Unpack_Str(data)
            print("Time: {}".format( str(time.ctime() )))
            print("Length: {}".format( _length ))
            print("Receive: {}".format( _data ))
        except:
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print("Non-hexadecimal digit found...")
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print("Receive: {}".format( data))


        # set TX
        self.rx_done = True
        # comment it will receive countinous
        self.set_dio_mapping([1,0,0,0,0,0])    # TX
        self.set_mode(MODE.STDBY)
        self.clear_irq_flags(TxDone=1)


    def on_tx_done(self):
        print("\nTxDone")
        # set RX
        self.set_dio_mapping([0,0,0,0,0,0])    # RX
        sleep(1)
        self.reset_ptr_rx()
        self.set_mode(MODE.RXCONT)
        self.clear_irq_flags(RxDone=1)
      

    def start(self):
        while True:
            print('----------------------------------')
            sleep(1)

            try:
                rawinput = raw_input(">>> ")
            except NameError:
                rawinput = input(">>> ")
            except KeyboardInterrupt:
                lora.set_mode(MODE.SLEEP)
                sleep(.5)
                BOARD.teardown()
                exit()

            if len(rawinput) < 200:

                data = {"id":self._id, "data":rawinput}
                _length, _payload = packer.Pack_Str( json.dumps(data) )

                try:
                    # for python2
                    data = [int(hex(ord(c)), 0) for c in _payload]
                except:
                    # for python3 
                    data = [int(hex(c), 0) for c in _payload]

                for i in range(3):
                    if self.rx_done is True:
                        self.rx_done = False
                        break
                    else:
                        self.set_mode(MODE.SLEEP)
                        self.set_dio_mapping([1,0,0,0,0,0])    # TX
                        sleep(.5)
                        lora.set_pa_config(pa_select=1)
                        self.clear_irq_flags(TxDone=1)
                        self.set_mode(MODE.STDBY)
                        sleep(.5)
                        print("Raw TX: {}".format(data))

                        self.write_payload(data)
                        self.set_mode(MODE.TX)

                        ## ALOHA(1~3) ## on_tx_done
                        t = i*i + int(np.random.random() * float(_length))
                        print("ALOHA Waiting: {}".format( t))
                        sleep(t)


lora = LoRaBeacon()
lora.set_mode(MODE.STDBY)
lora.set_pa_config(pa_select=1)

try:
    lora.start()
except KeyboardInterrupt:
    sys.stdout.flush()
    print("")
    sys.stderr.write("KeyboardInterrupt\n")
finally:
    sys.stdout.flush()
    lora.set_mode(MODE.SLEEP)
    sleep(.5)
    BOARD.teardown()
