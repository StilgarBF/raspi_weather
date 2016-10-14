# -*- coding: utf-8 -*-

import Adafruit_BMP.BMP085 as BMP085

def getData():
	sensor_bmp = BMP085.BMP085()
	
	# this sensor delivers temperature too, but it was 2°C off
	# temperature = sensor_bmp.read_temperature()
	
	values = []
	
	# got some strange readings! Read multiple times to even out peaks
	for x in range(0, 3):
		pressure = sensor_bmp.read_pressure()
		altitude = sensor_bmp.read_altitude()
		
		altitude = 359
		psea = pressure / pow(1.0 - altitude/44330.0, 5.255)
		
		pressure = psea / 100;
		
		if(950 <= pressure <= 1070):
			values.append(pressure)

	data = {"pressure": round((sum(values) / len(values)), 1)}
	
	return data