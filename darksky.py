#!/usr/bin/python
import os
import sys
import requests
import simplejson as json
import time
import Adafruit_CharLCD as LCD

def darksky():

	header = {'Accept': 'application/json'}
	baseurl = 'https://api.forecast.io/forecast/'
	apikey = sys.argv[1]
	location = '/38.9132,-77.0326'

	data = requests.get(baseurl + apikey + location, headers=header)
	dataJSON = json.loads(data.text, encoding="utf-8")

	curr = dataJSON['currently']['temperature']
	max = dataJSON['daily']['data'][0]['temperatureMax']
	summary = dataJSON['daily']['data'][0]['summary']

	return "C: %s, H: %s \n %s" % (curr, max, summary)

if __name__ == "__main__":	

	lcd = LCD.Adafruit_CharLCDPlate()

	while True: 
		print darksky()
		time.sleep(3)
