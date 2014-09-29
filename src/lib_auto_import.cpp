#define KDTREE_DEFINE_OSTREAM_OPERATORS
#include "../include/kdtree++/kdtree.hpp"

#include <deque>
#include <iostream>
#include <vector>
#include <limits>
#include <functional>
#include <set>

struct twin
{
  typedef float value_type;

  twin(value_type a, value_type b)
  {
    d[0] = a;
    d[1] = b;
  }

  twin(const twin & x)
  {
    d[0] = x.d[0];
    d[1] = x.d[1];
  }

  ~twin()
  {
  }

  double distance_to(twin const& x) const
  {
     double dist = 0;
     for (int i = 0; i != 2; ++i)
        dist += (d[i]-x.d[i])*(d[i]-x.d[i]);
     return std::sqrt(dist);
  }

  inline value_type operator[](size_t const N) const { return d[N]; }

  value_type d[2];
};

inline bool operator==(twin const& A, twin const& B) {
  return A.d[0] == B.d[0] && A.d[1] == B.d[1] ;
}

std::ostream& operator<<(std::ostream& out, twin const& T)
{
  return out << '(' << T.d[0] << ',' << T.d[1] << ')';
}

inline double tac( twin t, size_t k ) { return t[k]; }

typedef KDTree::KDTree<2, twin, std::pointer_to_binary_function<twin,size_t,double> > tree_type;

struct Predicate
{
   bool operator()( twin const& t ) const
   {
      return t[0] > 3;  // anything, we are currently testing that it compiles.
   }
};

// never finds anything
struct FalsePredicate
{
   bool operator()( twin const& t ) const { return false; }
};

int main()
{
  tree_type src(std::ptr_fun(tac));

  twin c0(1, 1); src.insert(c0);
  twin c1(1, 2); src.insert(c1);
  twin c2(2, 1); src.insert(c2);
  twin c3(2, 2); src.insert(c3);
/*
  twin c4(8.30, 0.72); src.insert(c4);
  twin c5(5.12, 7.66); src.insert(c5);
  twin c6(3.13, 3.10); src.insert(c6);
  twin c7(9.62, 7.56); src.insert(c7);
  twin c8(2.09, 2.17); src.insert(c8);
  twin c9(2.11, 0.01); src.insert(c9);
*/
  //edit here to add/remove nodes
  //insert user insert and erase to add/remove nodes and after that call optimise the balance the tree.
  std::cout << src << std::endl;

/*
  src.erase(c0);
  src.erase(c1);
  src.erase(c3);
  src.erase(c5);
*/
  src.optimise();

  std::cout << src << std::endl;

  twin s(1,1);
  std::vector<twin> v;
  unsigned int const range=1;
  src.find_within_range(s,range,std::back_inserter(v));
  std::cout << "found   " << v.size() << " nodes within range " << range
                << " of " << s << ":\n";
  std::vector<twin>::const_iterator ci = v.begin();
  for (; ci != v.end(); ++ci)
  	std::cout << *ci << " ";
  std::cout << "\n" << std::endl; 

  std::pair<tree_type::const_iterator,double> results=src.find_nearest(s,1.0);
  std::cout<<*results.first<<" "<<results.second<<std::endl;

  return 0;
}
