/** \file
 * Provides a Python interface for the libkdtree++.
 *
 * \author Willi Richert <w.richert@gmx.net>
 *
 *
 * This defines a proxy to a (int, int) -> long long KD-Tree. The long
 * long is needed to save a reference to Python's object id(). Thereby,
 * you can associate Python objects with 2D integer points.
 * 
 * If you want to customize it you can adapt the following: 
 * 
 *  * Dimension of the KD-Tree point vector.
 *    * DIM: number of dimensions.
 *    * operator==() and operator<<(): adapt to the number of comparisons
 *    * py-kdtree.i: Add or adapt all usages of PyArg_ParseTuple() to reflect the 
 *      number of dimensions.
 *    * adapt query_records in find_nearest() and count_within_range()
 *  * Type of points.
 *    * coord_t: If you want to have e.g. floats you have 
 *      to adapt all usages of PyArg_ParseTuple(): Change "i" to "f" e.g.
 *  * Type of associated data. 
 *    * data_t: currently unsigned long long, which is "L" in py-kdtree.i
 *    * PyArg_ParseTuple() has to be changed to reflect changes in data_t
 * 
 */


#ifndef _PY_KDTREE_H_
#define _PY_KDTREE_H_

#include <kdtree++/kdtree.hpp>

#include <iostream>
#include <vector>
#include <limits>

template <size_t DIM, typename COORD_T, typename DATA_T > 
struct record_t {
  static const size_t dim = DIM;
  typedef COORD_T coord_t;
  typedef DATA_T data_t;

  typedef coord_t point_t[dim];
 
  inline coord_t operator[](size_t const N) const { return point[N]; }

  point_t point;
  data_t data;
};

typedef double RANGE_T;

////////////////////////////////////////////////////////////////////////////////
// Definition of (int,int) with data type unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_2iull record_t<2, int, unsigned long long>
#define KDTREE_TYPE_2iull KDTree::KDTree<2, RECORD_2iull, std::pointer_to_binary_function<RECORD_2iull,int,double> >

inline bool operator==(RECORD_2iull const& A, RECORD_2iull const& B) {
    return A.point[0] == B.point[0] && A.point[1] == B.point[1] && A.data == B.data;
}

std::ostream& operator<<(std::ostream& out, RECORD_2iull const& T)
{
    return out << '(' << T.point[0] << ',' << T.point[1] << '|' << T.data << ')';
}


////////////////////////////////////////////////////////////////////////////////
// Definition of (int,int,int) with data type unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_3iull record_t<3, int, unsigned long long>
#define KDTREE_TYPE_3iull KDTree::KDTree<3, RECORD_3iull, std::pointer_to_binary_function<RECORD_3iull,int,double> >

inline bool operator==(RECORD_3iull const& A, RECORD_3iull const& B) {
    return A.point[0] == B.point[0] && A.point[1] == B.point[1] && A.point[2] == B.point[2] && A.data == B.data;
}

std::ostream& operator<<(std::ostream& out, RECORD_3iull const& T)
{
    return out << '(' << T.point[0] << ',' << T.point[1] << ',' << T.point[2] << '|' << T.data << ')';
}


////////////////////////////////////////////////////////////////////////////////
// Definition of (int,int,int,int) with data type unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_4iull record_t<4, int, unsigned long long>
#define KDTREE_TYPE_4iull KDTree::KDTree<4, RECORD_4iull, std::pointer_to_binary_function<RECORD_4iull,int,double> >

inline bool operator==(RECORD_4iull const& A, RECORD_4iull const& B) {
    return A.point[0] == B.point[0] && A.point[1] == B.point[1] && A.point[2] == B.point[2] && A.point[3] == B.point[3] && A.data == B.data;
}

std::ostream& operator<<(std::ostream& out, RECORD_4iull const& T)
{
    return out << '(' << T.point[0] << ',' << T.point[1] << ',' << T.point[2] << ',' << T.point[3] << '|' << T.data << ')';
}


////////////////////////////////////////////////////////////////////////////////
// Definition of (int,int,int,int,int) with data type unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_5iull record_t<5, int, unsigned long long>
#define KDTREE_TYPE_5iull KDTree::KDTree<5, RECORD_5iull, std::pointer_to_binary_function<RECORD_5iull,int,double> >

inline bool operator==(RECORD_5iull const& A, RECORD_5iull const& B) {
    return A.point[0] == B.point[0] && A.point[1] == B.point[1] && A.point[2] == B.point[2] && A.point[3] == B.point[3] && A.point[4] == B.point[4] && A.data == B.data;
}

std::ostream& operator<<(std::ostream& out, RECORD_5iull const& T)
{
    return out << '(' << T.point[0] << ',' << T.point[1] << ',' << T.point[2] << ',' << T.point[3] << ',' << T.point[4] << '|' << T.data << ')';
}


////////////////////////////////////////////////////////////////////////////////
// Definition of (int,int,int,int,int,int) with data type unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_6iull record_t<6, int, unsigned long long>
#define KDTREE_TYPE_6iull KDTree::KDTree<6, RECORD_6iull, std::pointer_to_binary_function<RECORD_6iull,int,double> >

inline bool operator==(RECORD_6iull const& A, RECORD_6iull const& B) {
    return A.point[0] == B.point[0] && A.point[1] == B.point[1] && A.point[2] == B.point[2] && A.point[3] == B.point[3] && A.point[4] == B.point[4] && A.point[5] == B.point[5] && A.data == B.data;
}

std::ostream& operator<<(std::ostream& out, RECORD_6iull const& T)
{
    return out << '(' << T.point[0] << ',' << T.point[1] << ',' << T.point[2] << ',' << T.point[3] << ',' << T.point[4] << ',' << T.point[5] << '|' << T.data << ')';
}


////////////////////////////////////////////////////////////////////////////////
// Definition of (float,float) with data type unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_2full record_t<2, float, unsigned long long>
#define KDTREE_TYPE_2full KDTree::KDTree<2, RECORD_2full, std::pointer_to_binary_function<RECORD_2full,int,double> >

inline bool operator==(RECORD_2full const& A, RECORD_2full const& B) {
    return A.point[0] == B.point[0] && A.point[1] == B.point[1] && A.data == B.data;
}

std::ostream& operator<<(std::ostream& out, RECORD_2full const& T)
{
    return out << '(' << T.point[0] << ',' << T.point[1] << '|' << T.data << ')';
}


////////////////////////////////////////////////////////////////////////////////
// Definition of (float,float,float) with data type unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_3full record_t<3, float, unsigned long long>
#define KDTREE_TYPE_3full KDTree::KDTree<3, RECORD_3full, std::pointer_to_binary_function<RECORD_3full,int,double> >

inline bool operator==(RECORD_3full const& A, RECORD_3full const& B) {
    return A.point[0] == B.point[0] && A.point[1] == B.point[1] && A.point[2] == B.point[2] && A.data == B.data;
}

std::ostream& operator<<(std::ostream& out, RECORD_3full const& T)
{
    return out << '(' << T.point[0] << ',' << T.point[1] << ',' << T.point[2] << '|' << T.data << ')';
}


////////////////////////////////////////////////////////////////////////////////
// Definition of (float,float,float,float) with data type unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_4full record_t<4, float, unsigned long long>
#define KDTREE_TYPE_4full KDTree::KDTree<4, RECORD_4full, std::pointer_to_binary_function<RECORD_4full,int,double> >

inline bool operator==(RECORD_4full const& A, RECORD_4full const& B) {
    return A.point[0] == B.point[0] && A.point[1] == B.point[1] && A.point[2] == B.point[2] && A.point[3] == B.point[3] && A.data == B.data;
}

std::ostream& operator<<(std::ostream& out, RECORD_4full const& T)
{
    return out << '(' << T.point[0] << ',' << T.point[1] << ',' << T.point[2] << ',' << T.point[3] << '|' << T.data << ')';
}


////////////////////////////////////////////////////////////////////////////////
// Definition of (float,float,float,float,float) with data type unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_5full record_t<5, float, unsigned long long>
#define KDTREE_TYPE_5full KDTree::KDTree<5, RECORD_5full, std::pointer_to_binary_function<RECORD_5full,int,double> >

inline bool operator==(RECORD_5full const& A, RECORD_5full const& B) {
    return A.point[0] == B.point[0] && A.point[1] == B.point[1] && A.point[2] == B.point[2] && A.point[3] == B.point[3] && A.point[4] == B.point[4] && A.data == B.data;
}

std::ostream& operator<<(std::ostream& out, RECORD_5full const& T)
{
    return out << '(' << T.point[0] << ',' << T.point[1] << ',' << T.point[2] << ',' << T.point[3] << ',' << T.point[4] << '|' << T.data << ')';
}


////////////////////////////////////////////////////////////////////////////////
// Definition of (float,float,float,float,float,float) with data type unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_6full record_t<6, float, unsigned long long>
#define KDTREE_TYPE_6full KDTree::KDTree<6, RECORD_6full, std::pointer_to_binary_function<RECORD_6full,int,double> >

inline bool operator==(RECORD_6full const& A, RECORD_6full const& B) {
    return A.point[0] == B.point[0] && A.point[1] == B.point[1] && A.point[2] == B.point[2] && A.point[3] == B.point[3] && A.point[4] == B.point[4] && A.point[5] == B.point[5] && A.data == B.data;
}

std::ostream& operator<<(std::ostream& out, RECORD_6full const& T)
{
    return out << '(' << T.point[0] << ',' << T.point[1] << ',' << T.point[2] << ',' << T.point[3] << ',' << T.point[4] << ',' << T.point[5] << '|' << T.data << ')';
}


////////////////////////////////////////////////////////////////////////////////
// END OF TYPE SPECIFIC DEFINITIONS
////////////////////////////////////////////////////////////////////////////////


template <class RECORD_T>
inline double tac(RECORD_T r, int k) { return r[k]; }

template <size_t DIM, typename COORD_T, typename DATA_T > 
class PyKDTree {
public:

  typedef record_t<DIM, COORD_T, DATA_T> RECORD_T;
  typedef KDTree::KDTree<DIM, RECORD_T, std::pointer_to_binary_function<RECORD_T,int,double> > TREE_T;
  TREE_T tree;

  PyKDTree() : tree(std::ptr_fun(tac<RECORD_T>)) {  };

  void add(RECORD_T T) { tree.insert(T); };

  /**
     Exact erase.
  */
  bool remove(RECORD_T T) { 
    bool removed = false;

    typename TREE_T::const_iterator it = tree.find_exact(T);
    if (it!=tree.end()) {
      tree.erase_exact(T); 
      removed = true;
    }
    return removed;
  };

  int size(void) { return tree.size(); }

  void optimize(void) { tree.optimise(); }
  
  RECORD_T* find_exact(RECORD_T T) {
    RECORD_T* found = NULL;
    typename TREE_T::const_iterator it = tree.find_exact(T);
    if (it!=tree.end())
      found = new RECORD_T(*it);

    return found;
  }

  size_t count_within_range(typename RECORD_T::point_t T, RANGE_T range) {
    RECORD_T query_record;
    memcpy(query_record.point, T, sizeof(COORD_T)*DIM);

    return tree.count_within_range(query_record, range);
  }

  std::vector<RECORD_T >* find_within_range(typename RECORD_T::point_t T, RANGE_T range) {
    RECORD_T query_record;
    memcpy(query_record.point, T, sizeof(COORD_T)*DIM);

    std::vector<RECORD_T> *v = new std::vector<RECORD_T>;
    tree.find_within_range(query_record, range, std::back_inserter(*v));
    return v;
  }

  RECORD_T* find_nearest (typename RECORD_T::point_t T) {
    RECORD_T* found = NULL;
    RECORD_T query_record;
    memcpy(query_record.point, T, sizeof(COORD_T)*DIM);

    std::pair<typename TREE_T::const_iterator, typename TREE_T::distance_type> best = 
      tree.find_nearest(query_record, std::numeric_limits<typename TREE_T::distance_type>::max());

    if (best.first!=tree.end()) {
      found = new RECORD_T(*best.first);
    }
    return found;
  }

  std::vector<RECORD_T >* get_all() {
    std::vector<RECORD_T>* v = new std::vector<RECORD_T>;

    for (typename TREE_T::const_iterator iter=tree.begin(); iter!=tree.end(); ++iter) {
      v->push_back(*iter);
    }

    return v;
  }

  size_t __len__() { return tree.size(); }
};
#endif //_PY_KDTREE_H_
