# -*- coding: utf-8 -*-
import argparse
import json

# sqlite to store data
import sqlite3 as lite

# custom
import collector as collector

# process arguments
parser = argparse.ArgumentParser(description="disable sql")
parser.add_argument("--noSQL")
args, leftovers = parser.parse_known_args()

disableStorage = args.noSQL is not None

if disableStorage:
  print "nothing will be saved\n"

parser = argparse.ArgumentParser(description="storeWhat")
parser.add_argument("--store")
args, leftovers = parser.parse_known_args()

storeOnlyOn = args.store is not None
storeOnly = args.store

if storeOnlyOn:
  print "store only %s\n" % (storeOnly)

# ------------------------------------------------------------------

# fetch data from sensors

data = collector.getData()

if not disableStorage:
	# store everything
	try:
		con = lite.connect('/var/www/html/sqlite/sensor.db');
		
		with con:
			cur = con.cursor()
	
			if (not storeOnlyOn) or (storeOnly == 'pressure'):
				query = "INSERT INTO sensordata (value, type, source) VALUES (" + str(data["pressure"]) + ", 'pressure', 'BMP180')"
				cur.execute(query)
	
			if (not storeOnlyOn) or (storeOnly == 'humidity'):
				query = "INSERT INTO sensordata (value, type, source) VALUES (" + str(data["humidity"]) + ", 'humidity', 'DHT22')"
				cur.execute(query)
	
			if (not storeOnlyOn) or (storeOnly == 'temperature'):
				query = "INSERT INTO sensordata (value, type, source) VALUES (" + str(data["temperature"]) + ", 'temperature', 'DHT22')"
				cur.execute(query)
	
			if (not storeOnlyOn) or (storeOnly == 'temperatureOutside'):
				query = "INSERT INTO sensordata (value, type, source) VALUES (" + str(round(data["outsideTemperature"], 1)) + ", 'temperatureOutside', 'DS1820')"
				cur.execute(query)
	
			if (not storeOnlyOn) or (storeOnly == 'light'):
				
				timescale = '15min'
				
				if(storeOnly == 'light'):
					timescale = '2min'
					
				query = "INSERT INTO sensordata (value, type, source, timescale) VALUES (" + str(data["light"]) + ", 'light', 'BH1750FVI', '" + timescale + "')"
				cur.execute(query)
	
	except lite.Error, e:
		print "Error %s:" % e.args[0]
	    
	finally:
	    
		if con:
			con.close()
		
print json.dumps(collector.getData(), indent=2)
