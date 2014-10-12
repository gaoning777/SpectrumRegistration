import time
import httplib
import numpy as np


class Transaction(object):
    def __init__(self):
        pass


    def run(self):
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

		start=time.time()
		conn=httplib.HTTPConnection('spectrum',5000)
		request="/range_query?lon="+str(lon)+"&lat="+str(lat)+"&distance="+str(0.002)
		conn.request("GET",request)
		response=conn.getresponse()
		conn.close()

		end=time.time()
		self.custom_timers['response_time']=end-start
		assert(response.status==200),'Bad Response: HTTP %s' % response.status

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers