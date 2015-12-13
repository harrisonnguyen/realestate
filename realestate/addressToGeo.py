#!/usr/bin/python
from lxml import html
import requests
import re
import sys
import urllib
import csv


def main():
	makeShapeFile()

def getLatLong(coord, address):
    
	#formats the string to make it a valid url
	#address = urllib.quote(address, safe='') 
	#forms the http request
	httpRequest = "https://maps.googleapis.com/maps/api/geocode/xml?address=" + address +"%NSW&key=AIzaSyC3S-4_i8u4oPzm7WZFtG-xX8UMxLRb00k"
	#httpRequest = "https://maps.googleapis.com/maps/api/geocode/xml?address=128%20Botany%20Road%20Alexandria%NSW&key=AIzaSyC3S-4_i8u4oPzm7WZFtG-xX8UMxLRb00k"
	#print httpRequest
    #gets the page

	page = requests.get(httpRequest) 
	#content = page.text
	content = page.content.split()
	latitude = 0
	longitude = 0
	content.reverse()
	#print content
	while True:
		string = content.pop()
		#print string
	#find matches for latitude and longitude
		if "<status>OVER" in string:
			coord.append(float(999.999))
			break
		if "<location>" in string:
			string = content.pop()
			string = re.sub("<lat>",'',string)
			string = re.sub("</lat>",'',string)
			latitude = string.strip(' ').strip('\n')
			string = content.pop()
			string = re.sub("<lng>",'',string)
			string = re.sub("</lng>",'',string)
			longitude = string.strip(' ').strip('\n')
			break
		if "</result>" in string:
			#reached end of page
			coord.append(float(999.999))
			break;
	#print latitude, longitude
	coord.append(float(longitude))
	coord.append(float(latitude))

    
    
def makeShapeFile():
	with open("realestatedata2000_2040.csv",'r') as p:
		with open("realestatedata2000_2040a.csv",'w') as csvoutput:
			fieldnames = ['sold_date','bathrooms', 'car', 'price','bedrooms', 'descript', 'address', 'postalCode', 'propertyType', 'coordinates']
			writer = csv.DictWriter(csvoutput, fieldnames=fieldnames, lineterminator='\n')
			reader = csv.DictReader(p)
			writer.writeheader()
			#i = 0
			for row in reader:                    
				if "0.0" in row['coordinates'] or not row['coordinates'] or "999.999" in row['coordinates']:
					address = row["address"]          
					coord = []
					getLatLong(coord, address)
					if coord[0] == 999.999:
						print "Status over query limit"
						break
					else:
						row.update({'coordinates' : str(coord[0]) + "," +  str(coord[1])})
				#if coord[0] == 0: #if the api calls are exhausted
				#	print row
				#	break                        
						print address, ": ", str(coord[0]) + "," +  str(coord[1])
				#i += 1
				writer.writerow(row)
main()
