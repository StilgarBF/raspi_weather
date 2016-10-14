# -*- coding: utf-8 -*-

import smbus
import time

# wrapper for main-function to return a dictionary
def getData(addr = 0x23):
	data = {"light": readLight(addr)}
	
	return data

# found the following at a tutorial. TODO: seach source
# modified though

# read Light
# helpers for Light
def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number
  return ((data[1] + (256 * data[0])) / 1.2)
  
# tries  some rounds of datafetching because sometimes the sensor returns 0
# even though, there actually is light
def readLight(addr = 0x23):
	bus = smbus.SMBus(1)  # Rev 2 Pi uses 1
	values = []

	# got some strange readings! Read multiple times to even out peaks
	for x in range(0, 5):
		data = bus.read_i2c_block_data(addr, 0x20)
		light = convertToNumber(data)
  	
		if light is not 0:
			values.append(light)
	
	if len(values) == 0:
		return 0
	else:
		return round((sum(values) / len(values)), 1)
