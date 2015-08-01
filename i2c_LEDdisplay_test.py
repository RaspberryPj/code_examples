#!/usr/bin/env python3
### Author: RaspberryPj
### Date: July 2015
### 1x MCP23008 chip controlling 1x FND500 7-segment display

import smbus
import time

## Define Variables
bus = smbus.SMBus(1)	# For Raspberry Pi v2 - (1)
address = 0x20			# MCP23008 at 0x20
iodir_register = 0x00
gpio_register = 0x09
#Dictionary for 7-segment display byte-addressing
dict_disp = {
   "Off":0x00, 0:0x3F, 1:0x06, 2:0x5B, 3:0x4F, 4:0x66, 
   5:0x6D, 6:0x7D, 7:0x07, 8:0x7F, 9:0x6F, "On":0xFF
   }

## Enable I/O Direction Register as outputs
bus.write_byte_data(address, iodir_register, 0x00)

## Flash all segments on and off 3 times
print "Testing all segments..."
for i in range(0,3):
   bus.write_byte_data(address, gpio_register, dict_disp['On'])
   time.sleep(0.2)
   bus.write_byte_data(address, gpio_register, dict_disp['Off'])
   time.sleep(0.2)

## Display numbers counting from 0 to 9
print "Counting to 9..."
for x in range(0,10):
   bus.write_byte_data(address, gpio_register, dict_disp[x])
   time.sleep(0.5)

## Turn 7-segment display off
bus.write_byte_data(address, gpio_register, dict_disp['Off'])

print "Testing complete"

# End