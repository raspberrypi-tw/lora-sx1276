# One Days Workshop for Raspberry Pi LoRa SX127x

## Intro
In this workshop, you will learn about:
1. What is LoRa?
2. How to control the SX127x LoRa module.
3. Connect to The Things Network(TTN) LoRaWAN.
4. Build your own private LoRa gateway.

The slide is available on [用Raspberry Pi + LoRa實做微型物聯網閘道器](https://www.slideshare.net/raspberrypi-tw/raspberry-pi-lora)


## Environment
[Raspberry Pi 3B](https://www.raspberrypi.com.tw/10684/55/)/[Raspberry Pi 3B+](https://www.raspberrypi.com.tw/19429/57/) + SanDisk 32G microSD  + [MiniLoRa](https://www.raspberrypi.com.tw/21088/minilora-module/) + 2018-06-27-raspbian-stretch.img

## Prerequisite
### Install required package and Python module
```shell  
$ sudo apt-get update
$ sudo apt-get install -y python-dev python-pip x11vnc mosquitto mosquitto-clients
$ sudo pip install spidev numpy pyserial paho-mqtt base58 pycrypto
$ sudo pip3 install paho-mqtt
```

## More LoRa module and RF Kit
* [RN2483 LoRa Technology Mote 低功率 LoRa 開發套件](https://www.raspberrypi.com.tw/21125/rn2483-lora-technology-mote/)
* [Great Scott Gadgets HackRF One](https://www.raspberrypi.com.tw/21095/hackrf-one-software-defined-radio/)

