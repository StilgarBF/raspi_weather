# -*- coding: utf-8 -*-

# custom
import modules.dht22 as dht22
import modules.bh1750 as bh1750
import modules.bmp180 as bmp180
import modules.ds1820 as ds1820
from modules.helpers import mergeDicts

def getData():
	data = {}
	
	dhtPin = 17
	data = mergeDicts(data, dht22.getData(dhtPin))
	data = mergeDicts(data, bh1750.getData())
	data = mergeDicts(data, bmp180.getData())
	
	outsideTempSensorID = "28-0316805422ff"
	data = mergeDicts(data, ds1820.getData(outsideTempSensorID, "outsideTemperature"))
	
	outsideTempSensorID = "28-0516801d5aff"
	data = mergeDicts(data, ds1820.getData(outsideTempSensorID, "insideTemperature"))
	
	return data