# -*- coding: utf-8 -*-
import re, os

def getData(deviceIdentifier, dataKey):
	prefix = '/sys/bus/w1/devices/'
	suffix = '/w1_slave'
	
	path = prefix + deviceIdentifier + suffix
	
	data = {dataKey : _read_sensor(path)}
	return data

# function: read and parse sensor data file
def _read_sensor(path):
  value = "U"

  try:
    f = open(path, "r")
    line = f.readline()

    if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
      line = f.readline()
      m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)

      if m:
        value = round((float(m.group(2)) / 1000.0), 1)

    f.close()

  except (IOError), e:
    print time.strftime("%x %X"), "Error reading", path, ": ", e

  finally:
	return value
