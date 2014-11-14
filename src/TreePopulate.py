import urllib
import sys
import os
import json
import numpy as np
import cpyext
sys.path.append("../python-bindings/")
cpyext.load_module("../python-bindings/_kdtree.so","_kdtree")
from kdtree import KDTree_2Float

# populate the tree with the pre constructed tree in ../data/APs.json generated by TreeDataGeneration.py
def buildTree():
	APFile = open('../data/APs.json')
	APsMap=json.load(APFile)
	nn = KDTree_2Float()
	for AP in APsMap:
		nn.add(((float(AP[0]),float(AP[1])),1))
	nn.optimize()

	# start flask_service
	return nn

if __name__=="__main__":
	buildTree()
