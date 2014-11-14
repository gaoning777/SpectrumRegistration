from flask import Flask
from flask import request
#from UpdateQueueproxy import *
import TreePopulate
import subprocess
app = Flask(__name__)

#testing
@app.route("/")
def hello():
	return "Hello World!"

@app.route("/range_query",methods=['GET'])
def range_query():
	lon=float(request.args.get('lon',''))# second param is default value
	lat=float(request.args.get('lat',''))
	distance=float(request.args.get('distance',''))
	# process the remaining update transactions
	'''
	trans=queues.pop(serverIP)
        while trans!=None:
                kind,lat,lon=Transaction.deserialize(trans)
		if kind==2:
			tree.add(((lon,lat),1))
		elif kind==3:
			tree.remove(((lon,lat),1))
                trans=queues.pop(serverIP)
	# return "nearest neighbor searching of (lon:%s, lat:%s) within radius of %s." % (str(lon), str(lat), str(distance))
	'''
	result=tree.find_within_range((lon,lat),distance)
	return str(result)
	
@app.route("/add_ap",methods=['GET'])
def add_ap():
	lon=float(request.args.get('lon',''))
	lat=float(request.args.get('lat',''))
	# synchronize
	# update the requests from the other servers at first
	queues.add_add_toothers(serverIP,lat,lon)
	tree.add(((lon,lat),1))
	return "(lon=%lf,lat=%lf) is inserted into the tree." %(lon,lat)

@app.route("/remove_ap",methods=['GET'])
def remove_ap():
	lon=float(request.args.get('lon',''))
	lat=float(request.args.get('lat',''))
	queues.add_remove_toothers(serverIP,lat,lon)
	if(tree.remove(((lon,lat),1))):
		return "(lon=%lf,lat=%lf) is removed from the tree." %(lon,lat)
	return "remove failed."

@app.route("/optimize",methods=['GET'])
def optimize():
	tree.optimize()
	return "optimize complete."

if __name__ == "__main__":
	# flask uses thread local objects so that the tree object  is accessible from all the other functions.
	# tree = TreePopulate.buildTree()
	# initializing the Concoord object requires IP addresses and ports
	'''
	servermapFile=open('concoord/servermap','r')
	servermap=list()
	for line in servermapFile:
		servermap.append(line.strip())
	param=""
	for serverIP in servermap:
		param+=serverIP+":14000,"
	queues = TransactionQueues(param[:-1])
	# obtain its own IP address
	p1=subprocess.Popen(["ifconfig","eth0"],stdout=subprocess.PIPE)
	p2=subprocess.Popen(["grep","inet addr"],stdin=p1.stdout,stdout=subprocess.PIPE)
	p3=subprocess.Popen(["awk","-F:",'{ print $2 }'],stdin=p2.stdout,stdout=subprocess.PIPE)
	p4=subprocess.Popen(["awk",'{ print $1 }'],stdin=p3.stdout,stdout=subprocess.PIPE)
	ip=p4.communicate()
	serverIP=ip[0].strip()
	'''
	app.run(host='0.0.0.0',debug=True)
