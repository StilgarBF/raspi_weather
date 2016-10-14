# -*- coding: utf-8 -*-

# for DHT22 temperature and humidity
import Adafruit_DHT

def getData(pin):
	sensor_dht = Adafruit_DHT.DHT22
	humidity, temperature = Adafruit_DHT.read_retry(sensor_dht, pin);
	
	data = {
		"temperature" : round(temperature, 2),
		"humidity" : round(humidity, 2)
	}
	
	return data
