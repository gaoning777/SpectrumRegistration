# test the latency and # of requests a single node can handle

import numpy as np
import sys
import httplib
from timeit import default_timer as timer
def generateOneAP():
	# unit of 0.005 degree(0.5KM)
	# for suburban areas, 10 APs per square km
	# 
	# lon: -122.678(Portland,OR) to -71.060(Boston,MA)
	#	10323 units
	# lat: 32.749(San Diego,CA)  to 47.590(Seattle, WA)
	#	2968 units
	unit=0.005
	lon=-122.678+float(np.random.randint(1,10324))*0.005
	lat=  32.749+float(np.random.randint(1,2969) )*0.005
	return lon,lat

def query(lon,lat,distance):
	# return length of the response
	# empty return set has length 2
	# failure to repsond has return 0
	
	#second return value is latency
	
	#time it
	start=timer()
	conn=httplib.HTTPConnection('spectrum',5000)
	request="/range_query?lon="+str(lon)+"&lat="+str(lat)+"&distance="+str(distance)
	conn.request("GET",request)
	response=conn.getresponse()
	if response.status==200:
		data=response.read()
		length=len(data)
		end=timer()
		conn.close()
		return length,end-start
	else:
		conn.close()
		return 0,0

def test_all_queries_serial(num):
	# parameter num is the number of queries
	# distance is 0.002 degree(200meters) in order to reduce the effect from network communication
	length=[]
	latency=[]
	for i in range(num):
		lon,lat=generateOneAP()
		tmpLength,tmpLatency=query(lon,lat,0.002)
		# print tmpLength,tmpLatency
		length.append(tmpLength)
		latency.append(tmpLatency)
	goodResponse=0
	totalLatency=0.0
	for index in range(len(length)):
		if length[index] != 0:
			goodResponse+=1
			totalLatency+=latency[index]	
	print "test_all_queries_serial summary:"
	print "percentage of good response: ",str(100*1.0*goodResponse/len(length)),"%"
	print "average latency is: ",str(totalLatency/len(length))


def main():
	test_all_queries_serial(10)
if __name__=="__main__":
	main()

