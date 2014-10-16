from flask import Flask
from flask import request
import TreePopulate
app = Flask(__name__)

#testing
@app.route("/hello")
def hello():
	return "Hello World!"

@app.route("/range_query",methods=['GET'])
def range_query():
	lon=float(request.args.get('lon',''))# second param is default value
	lat=float(request.args.get('lat',''))
	distance=float(request.args.get('distance',''))
	#return "nearest neighbor searching of (lon:%s, lat:%s) within radius of %s." % (str(lon), str(lat), str(distance))
	result=tree.find_within_range((lon,lat),distance)
	return str(result)
	
@app.route("/add_ap",methods=['GET'])
def add_ap():
	lon=float(request.args.get('lon',''))
	lat=float(request.args.get('lat',''))
	tree.add(((lon,lat),1))
	return "(lon=%lf,lat=%lf) is inserted into the tree." %(lon,lat)

@app.route("/remove_ap",methods=['GET'])
def remove_ap():
	lon=float(request.args.get('lon',''))
	lat=float(request.args.get('lat',''))
	if(tree.remove(((lon,lat),1))):
		return "(lon=%lf,lat=%lf) is removed from the tree." %(lon,lat)
	return "remove failed."

@app.route("/optimize",methods=['GET'])
def optimize():
	tree.optimize()
	return "optimize complete."

if __name__ == "__main__":
	# flask uses thread local objects so that the tree object  is accessible from all the other functions.
	tree = TreePopulate.buildTree()
	app.run(host='0.0.0.0')
