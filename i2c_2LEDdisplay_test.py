#!/usr/bin/env python3
### Author: RaspberryPj
### Date: July 2015
### 2x MCP23008 chips controlling 2x FND500 7-segment displays

import smbus
import time

## Define Variables
bus = smbus.SMBus(1)	# For Raspberry Pi v2 - (1)
addr_10 = 0x20			# MCP23008 at 0x20
addr_01 = 0x21			# MCP23008 at 0x21
iodir_register = 0x00
gpio_register = 0x09
#Dictionary for 7-segment display byte-addressing
dict_disp = {
   "Off":0x00, 0:0x3F, 1:0x06, 2:0x5B, 3:0x4F, 4:0x66, 
   5:0x6D, 6:0x7D, 7:0x07, 8:0x7F, 9:0x6F, "On":0xFF
   }

## Enable I/O Direction Register as outputs
bus.write_byte_data(addr_10, iodir_register, 0x00)
bus.write_byte_data(addr_01, iodir_register, 0x00)

## Define method for displaying numbers
def display(num):
   num = int(num)		# Force integer
   if (num > 99):
      print "Error.  Currently only accepting numbers 0 to 99"
   elif (num < 10):
      bus.write_byte_data(addr_10, gpio_register, dict_disp['Off'])
      bus.write_byte_data(addr_01, gpio_register, dict_disp[num])
   else:
      str_num=str(num)		# convert to string
      a = int(str_num[:1])	# slice off first character
      b = int(str_num[-1:]) # slice off last character
      bus.write_byte_data(addr_10, gpio_register, dict_disp[a])
      bus.write_byte_data(addr_01, gpio_register, dict_disp[b])

## Count from 0 to 99
for i in range(0,100):
   print "Counting..." + str(i)
   display(i)
   time.sleep(0.3)

## Turn both 7-segment displays off
bus.write_byte_data(addr_10, gpio_register, dict_disp['Off'])
bus.write_byte_data(addr_01, gpio_register, dict_disp['Off'])

# End