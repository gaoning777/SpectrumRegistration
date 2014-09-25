#
# $Id: py-kdtree_test.py 2268 2008-08-20 10:08:58Z richert $
#

import unittest
import sys
sys.path.append("../")
from kdtree import KDTree_3Float, KDTree_2Float

class KDTree_3FloatTestCase(unittest.TestCase):
    def test_empty(self):
        nn = KDTree_3Float()
        self.assertEqual(0, nn.size())
        
        actual = nn.find_nearest((2,3,0))
        self.assertTrue(None==actual, "%s != %s"%(str(None), str(actual)))

    def test_get_all(self):
        nn = KDTree_3Float()
        o1 = object()
        nn.add(((1,1,0), id(o1)))
        o2 = object()
        nn.add(((10,10,0), id(o2)))
        o3 = object()
        nn.add(((11,11,0), id(o3)))

        self.assertEqual([((1,1,0), id(o1)), ((10,10,0), id(o2)), ((11,11,0), id(o3))], nn.get_all())
        self.assertEqual(3, len(nn))
        
        nn.remove(((10,10,0), id(o2)))
        self.assertEqual(2, len(nn))        
        self.assertEqual([((1,1,0), id(o1)), ((11,11,0), id(o3))], nn.get_all())
        
    def test_nearest(self):
        nn = KDTree_3Float()

        nn_id = {}
        
        o1 = object()
        nn.add(((1,1,0), id(o1)))
        nn_id[id(o1)] = o1
        o2 = object()
        nn.add(((10,10,0), id(o2)))
        nn_id[id(o2)] = o2
        o3 = object()
        nn.add(((4.1, 4.1,0), id(o3)))
        nn_id[id(o3)] = o3
        
        expected =  o3
        actual = nn.find_nearest((2.9,2.9,0))[1]
        self.assertTrue(expected==nn_id[actual], "%s != %s"%(str(expected), str(nn_id[actual])))

        expected = o3
        actual = nn.find_nearest((6, 6,0))[1]
        self.assertTrue(expected==nn_id[actual], "%s != %s"%(str(expected), str(nn_id[actual])))

    def test_remove(self):
        class C:
            def __init__(self, i):
                self.i = i
                self.next = None

        nn = KDTree_3Float()

        k1, o1 = (1.1,1.1,0), C(7)
        self.assertFalse(nn.remove((k1, id(o1))), "This cannot be removed!")
        nn.add((k1, id(o1)))

        k2, o2 = (1.1,1.1,0), C(7)
        nn.add((k2, id(o2)))

        self.assertEqual(2, nn.size())
        self.assertTrue(nn.remove((k2, id(o2))))
        self.assertEqual(1, nn.size())        
        self.assertFalse(nn.remove((k2, id(o2))))        
        self.assertEqual(1, nn.size())

        nearest = nn.find_nearest(k1)
        self.assertTrue(nearest[1] == id(o1), "%s != %s"%(nearest[1], o1))
        #self.assertTrue(nearest[1] is o1, "%s,%s is not %s"%(str(nearest[0]), str(nearest[1]), str((k1,id(o1)))))

class KDTree_2FloatTestCase(unittest.TestCase):
    def test_empty(self):
        nn = KDTree_2Float()
        self.assertEqual(0, nn.size())
        
        actual = nn.find_nearest((2.1,3.1))
        self.assertTrue(None==actual, "%s != %s"%(str(None), str(actual)))


    def test_ning(self):
	nn = KDTree_2Float()
	nn.add(((1.1,1.1),1))
	x = 1
	nn.remove(((1.1,1.1),x))
	self.assertEqual(1,len(nn))
	
    def test_get_all(self):
        nn = KDTree_2Float()
        o1 = object()
        nn.add(((1,1), id(o1)))
        o2 = object()
        nn.add(((10,10), id(o2)))
        o3 = object()
        nn.add(((11,11), id(o3)))

        self.assertEqual([((1,1), id(o1)), ((10,10), id(o2)), ((11,11), id(o3))], nn.get_all())
        self.assertEqual(3, len(nn))
        
        nn.remove(((10,10), id(o2)))
        self.assertEqual(2, len(nn))        
        self.assertEqual([((1,1), id(o1)), ((11,11), id(o3))], nn.get_all())
        
    def test_nearest(self):
        nn = KDTree_2Float()

        nn_id = {}
        
        o1 = object()
        nn.add(((1,1), id(o1)))
        nn_id[id(o1)] = o1
        o2 = object()
        nn.add(((10,10), id(o2)))
        nn_id[id(o2)] = o2
        o3 = object()
        nn.add(((4.1, 4.1), id(o3)))
        nn_id[id(o3)] = o3
        
        expected =  o3
        actual = nn.find_nearest((2.9,2.9))[1]
        self.assertTrue(expected==nn_id[actual], "%s != %s"%(str(expected), str(nn_id[actual])))

        expected = o3
        actual = nn.find_nearest((6, 6))[1]
        self.assertTrue(expected==nn_id[actual], "%s != %s"%(str(expected), str(nn_id[actual])))

    def test_remove(self):
        class C:
            def __init__(self, i):
                self.i = i
                self.next = None

        nn = KDTree_2Float()

        k1, o1 = (1.1,1.1), C(7)
        self.assertFalse(nn.remove((k1, id(o1))), "This cannot be removed!")
        nn.add((k1, id(o1)))

        k2, o2 = (1.1,1.1), C(7)
        nn.add((k2, id(o2)))

        self.assertEqual(2, nn.size())
        self.assertTrue(nn.remove((k2, id(o2))))
        self.assertEqual(1, nn.size())        
        self.assertFalse(nn.remove((k2, id(o2))))        
        self.assertEqual(1, nn.size())

        nearest = nn.find_nearest(k1)
        self.assertTrue(nearest[1] == id(o1), "%s != %s"%(nearest[1], o1))
        #self.assertTrue(nearest[1] is o1, "%s,%s is not %s"%(str(nearest[0]), str(nearest[1]), str((k1,id(o1)))))

def suite():
    return unittest.defaultTestLoader.loadTestsFromModule(sys.modules.get(__name__))
    
if __name__ == '__main__':
    unittest.main()
