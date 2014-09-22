import urllib
import ephem
import json
import sys
import os

def fileOrUrl(filename, url):
    try:
        file =  open(filename)
        return file
    except IOError:
        return urllib.urlopen(url)

def getGlobalstarTLE(debug = False):
    TLE = {}
    try:
        file = fileOrUrl("globalstar-newgen.tle", 
                         "http://dirkcgrunwald.dyndns.org/~grunwald/globalstar-newgen.tle")
        while True:
            line1 = file.readline()
            if line1 == '':
                break
            else:
                line2 = file.readline()
                line3 = file.readline()
                globalstar, sat = line1.split()
                TLE[sat] = ephem.readtle(sat, line2, line3)
                if debug:
                    print "sat us {%s}" % (sat)
                    print "TLE is ", TLE[sat]
        return TLE
    except:
        print "Can't get globalstar TLE information"

def getZCTA():
    zctaFile = fileOrUrl("zcta.json",
                         "http://dirkcgrunwald.dyndns.org/~grunwald/zcta.json")
    zcta = json.load(zctaFile)
    return zcta

def putZCTA(zcta, filename = "./zcta2.json"):
    out = open(filename, "w")
    print >>out, json.dumps(zcta,
                            sort_keys=True,
                            indent=4,
                            separators=(',', ': '))
    out.close()


def nonZeroSamples(lyst):             # used for reporting
    samples = 0
    for sample in lyst:
        if sample > 0:
            samples = samples + 1
    return samples

#
# This code is from: http://www.johndcook.com/python_longitude_latitude.html
#
def distance_on_unit_sphere(lat1, long1, lat2, long2):

    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
        
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc
