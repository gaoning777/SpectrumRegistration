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
	

if __name__ == "__main__":
	#execfile('TreePopulate.py')
	tree = TreePopulate.buildTree()
	app.run(host='0.0.0.0')
