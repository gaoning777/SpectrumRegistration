import urllib
import sys
import os
import numpy as np
import json

def fileOrUrl(filename, url):
	try:
		file =  open(filename)
		return file
	except IOError:
		return urllib.urlopen(url)

def getZCTA():
	zctaFile = fileOrUrl("../data/zcta.json","http://dirkcgrunwald.dyndns.org/~grunwald/zcta.json")
	zcta = json.load(zctaFile)
	return zcta

def putAPs(APsMap, filename = "../data/APs.json"):
	out = open(filename, "w")
	# similar to out.write()
	print >>out, json.dumps(APsMap,
                            sort_keys=True,
                            indent=4,
                            separators=(',', ': '))
	out.close()

def generateAP(lon,lat,sqmi,num):
	radius=np.sqrt(sqmi/np.pi)
	radiusArr=np.random.rand(num)*radius
	angleArr=np.random.rand(num)*2*np.pi
	x=lon+radiusArr*np.cos(angleArr)/111.12
	y=lat+radiusArr*np.sin(angleArr)/111.12
	return x,y

def GenerateTree():
	ZCTA = getZCTA()
	print "There are ",len(ZCTA.keys()), " zipcode tabulation areas"

	APsMap=list()
	# NumRural: how many access points in rural areas
	# AreasRural: # of rural areas
	# sqMiRural: sum of sqmi of rural areas
	NumRural, NumSubUrban, NumUrban=0,0,0
	AreasRural, AreasSubUrban, AreasUrban = 0, 0, 0
	SqMiRural, SqMiSubUrban, SqMiUrban = 0, 0, 0

	TotalAPs = 0
	TotalPop = 0
	ZeroAPs  = 0
	
	for zipName in ZCTA.keys():
		z=ZCTA[zipName]
		if z['pop'] <=1:
			#
			# An extremely rural area, with no APs
			#
			# aps stores how many access points
			z['aps']=0
			NumRural = NumRural+0
			AreasRural = AreasRural + 1
			SqMiRural = SqMiRural + z['aland_sqmi']
		else:
			#
			# Compute population density
			#
			pd = z['pop'] /  z["aland_sqmi"]								  
			#												      
			# The type of area is determined by the population density.
			# Although it's not a definitive source, http://greatdata.com/rural-urban-data
			# states the Department of Defense had established the following designations for a ZIP Code:
			# Urban: 3,000+ persons per square mile
			# Suburban: 1,000 - 3,000 persons per square mile
			# Rural: less than 1,000 persons per square mile
			#
			# As that website indicates, this is a course and sometimes inaccurate
			# classification. We'll use cut-offs that make more areas be classified
			# as "urban" and thus increase the number of WiFi access points and is
			# more inline with Census designation of "urban" (>1000 ppl/mi)
			#
			# The value 0.386 is the conversion factor between square miles 
			# and square kilometers. I.e. 1 sq.mi is 1/0.386 or 2.59 sq. km
			#
			if pd < 750:								        
				z['aps'] = int(z['aland_sqmi'] * 0.05 / 0.386) # 1 AP every 20 sq. km
				NumRural = NumRural + z['aps']
				AreasRural = AreasRural + 1
				SqMiRural = SqMiRural + z['aland_sqmi']
			elif pd < 1000:								     
				z['aps'] = int(z['aland_sqmi'] * 10 / 0.386)    # 10 AP's every square km
				NumSubUrban = NumSubUrban + z['aps']
				AreasSubUrban = AreasSubUrban + 1
				SqMiSubUrban = SqMiSubUrban + z['aland_sqmi']
			else:												  
				z['aps'] = int(z['aland_sqmi'] * 16 / 0.386)    # 16 AP's every square km
				NumUrban = NumUrban + z['aps']
				AreasUrban = AreasUrban + 1
				SqMiUrban = SqMiUrban + z['aland_sqmi']

			# generate points
			lon,lat=generateAP(z['lon'],z['lat'],z['aland_sqmi'],z['aps'])
			for i in range(len(lon)):
				APsMap.append((lon[i],lat[i]))

 			TotalAPs = TotalAPs + z['aps']
			TotalPop = TotalPop + z['pop']
		if z['aps'] == 0:
			ZeroAPs = ZeroAPs + 1
	print "the number of APs is ",TotalAPs
	print "Total population is", TotalPop, "with", TotalAPs, "AP's"
	print "Of the ", len(ZCTA.keys()), "zip codes", \
    	ZeroAPs, "do not have an AP (", int(1000* ZeroAPs / len(ZCTA.keys())) / 10., "%)"
	print AreasRural, "rural areas with", NumRural, "AP's over", \
    	SqMiRural, "SqMi or ", SqMiRural/ 0.386, "SqKm"
	print AreasSubUrban, "suburban areas with", NumSubUrban, "AP's over", \
    	SqMiSubUrban, "SqMi or", SqMiSubUrban / 0.386, "SqKm"
	print AreasUrban, "urban areas with", NumUrban, "AP's over", \
    	SqMiUrban, "SqMi or ", SqMiUrban / 0.386, "SqKm"
	putAPs(APsMap)

if __name__== "__main__":
	GenerateTree()



	