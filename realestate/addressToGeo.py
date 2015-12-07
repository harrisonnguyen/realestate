#!/usr/bin/python
from lxml import html
import requests
import re
import sys
import urllib
import csv
import shapefile


def main():
	makeShapeFile()

def getLatLong(coord, address):
    
	#formats the string to make it a valid url
	address = urllib.quote(address, safe='') 
	#forms the http request
	httpRequest = "https://maps.googleapis.com/maps/api/geocode/json?address="  + address 
	

    #gets the page

	page = requests.get(httpRequest) 
	#content = page.text
	content = page.content.split('\n')
	latitude = 0
	longitude = 0

	for line in content:
		#find matches for latitude and longitude

		if re.search("lat", line):
			line = re.sub('.*: ', '', line)
			line = re.sub(',.*', '', line)
			latitude = line
		if re.search("lng", line):
			line = re.sub('.*: ', '', line)
			line = re.sub(',.*', '', line)
			longitude = line
		#longitude is after latitude in the file
			break

	coord.append(float(longitude))
	coord.append(float(latitude))

    
    
def makeShapeFile():
	with open("output.csv",'r') as p:
		with open("realestatedata.csv",'w') as csvoutput:
			fieldnames = ['bathrooms', 'car', 'price','bedrooms', 'descript', 'address', 'postalCode', 'propertyType', 'coordinates']
			writer = csv.DictWriter(csvoutput, fieldnames=fieldnames, lineterminator='\n')
			reader = csv.DictReader(p)
			writer.writeheader()
			#i = 0
			for row in reader:                    
				address = row["address"]          
				coord = []            
				getLatLong(coord, address)
				row.update({'coordinates' : str(coord[0]) + "," +  str(coord[1])})
				#if coord[0] == 0: #if the api calls are exhausted
				#	print row
				#	break                        
				#print i, ": ", str(coord[0]) + "," +  str(coord[1])
				#i += 1
				writer.writerow(row)
main()
