import sys
sys.path.append("../python-bindings/")
from kdtree import KDTree_2Float


def main():
	nn = KDTree_2Float()
	nn.add(((1.0,1.0),3))
	nn.add(((2.0,2.0),5))
	nn.add(((1.0,2.0),6))
	nn.add(((2.0,1.0),4))
	print len(nn)
	result= {}
	result = nn.find_within_range((1.0,1.0),0.9)
	for record in result:
		print record
        
	nn.remove(((2.0,2.0),5))
	print len(nn)

    
if __name__ == '__main__':
    main()
