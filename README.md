# Raspberry Pi weatherstation

A collection of scripts to fetch data from sensors connected to a Raspberry Pi.

## Included sensors

 * **DHT22** temperature and humidity (GPIO)
 * **DS1820** temperature (1-wire)
 * **BH1750** light intensity (I2C)
 * **BMP180** barometric pressure and Temperature/Altitude (I2C)


## Files

* modules/
  * contains modules to fetch data form the sensors. Every modul has a *getData* method.
* collector.py
  * Helper that queries all sensors and compiles a dictionary with all values.
* show.py
  * Basic excample that orints the result
* store.py
  * Stores the data to a sqlite DB.  


## Example

```
me@myraspi:/myfolder# sudo python store.py
{
  "pressure": 1012.7, 
  "insideTemperature": 17.4, 
  "temperature": 17.5, 
  "light": 1.7, 
  "outsideTemperature": 10.9, 
  "humidity": 49.1
}
```

## License

Some components of the modules have been taken from online-tutorials.
No License, until I have compiled and noted all sources.