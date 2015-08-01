#!/usr/bin/env python3
### Author: RaspberryPj
### Date: July 2015
### 1x MCP23008 chip - testing with 1x 3mm Red LED

import smbus
import time

## Define Variables
bus = smbus.SMBus(1)	# For Raspberry Pi v2 - (1)
address = 0x20			# MCP23008 at 0x20
iodir_register = 0x00
gpio_register = 0x09

## Enable I/O Direction Register setting GP0 as output
bus.write_byte_data(address, iodir_register, 0xfe)

## Flash LED at GP0 on and off 3 times
for i in range(0,3):
   bus.write_byte_data(address, gpio_register, 0x01)
   time.sleep(0.5)
   bus.write_byte_data(address, gpio_register, 0x00)
   time.sleep(0.5)

# End

