#include "../include/nanoflann.hpp"
#include <cstdlib>
#include <iostream>
#include <sys/time.h>

using namespace std;
using namespace nanoflann;

template <typename T>
struct PointCloud
{
	struct Point
	{
		T  x,y;
	};

	std::vector<Point>  pts;

	typedef  PointCloud Derived; //!< In this case the dataset class is myself.

	/// CRTP helper method
	inline const Derived& derived() const { return *static_cast<const Derived*>(this); }
	/// CRTP helper method
	inline       Derived& derived()       { return *static_cast<Derived*>(this); }

	inline void add_point(T x,T y)
	{
		Point p;
		p.x=x;
		p.y=y;
		pts.push_back(p);
	}
	// Must return the number of data points
	inline size_t kdtree_get_point_count() const { return pts.size(); }

	// Returns the distance between the vector "p1[0:size-1]" and the data point with index "idx_p2" stored in the class:
	inline float kdtree_distance(const T *p1, const size_t idx_p2,size_t size) const
	{
		float d0=p1[0]-pts[idx_p2].x;
		float d1=p1[1]-pts[idx_p2].y;
		return d0*d0+d1*d1;
	}

	// Returns the dim'th component of the idx'th point in the class:
	// Since this is inlined and the "dim" argument is typically an immediate value, the
	//  "if/else's" are actually solved at compile time.
	inline float kdtree_get_pt(const size_t idx, int dim) const
	{
		if (dim==0) return pts[idx].x;
		else return pts[idx].y;
	}

	// Optional bounding-box computation: return false to default to a standard bbox computation loop.
	//   Return true if the BBOX was already computed by the class and returned in "bb" so it can be avoided to redo it again.
	//   Look at bb.size() to find out the expected dimensionality (e.g. 2 or 3 for point clouds)
	template <class BBOX>
	bool kdtree_get_bbox(BBOX &bb) const { return false; }

};

double get_time()
{
        struct timeval tv;
        gettimeofday(&tv,NULL);
        return tv.tv_sec+tv.tv_usec/1000000.0;
}


template <typename T>
void generatePointCloud(PointCloud<T> &point)
{
	
	while(true)
	{
		//add code here to add new points
		point.add_point(1.0,2.0);
		break;
	}
}

template <typename num_t>
void perf_test()
{
	PointCloud<num_t> cloud;

	// Generate points:
	generatePointCloud(cloud);

	// construct an randomized kd-tree index using 4 kd-trees
	double t0=get_time();

	typedef KDTreeSingleIndexAdaptor<
		L2_Simple_Adaptor<num_t, PointCloud<num_t> > ,
		PointCloud<num_t>,
		2 /* dim */
		> my_kd_tree_t;

	my_kd_tree_t   index(2 /*dim*/, cloud, KDTreeSingleIndexAdaptorParams(10 /* max leaf */) );
	index.buildIndex();
	double t1=get_time();
	cout << "Build Index<>: " << (t1-t0)*1e3 << " ms\n";

}


int main(int argc, char** argv)
{
	perf_test<float>();
	return 0;
}

