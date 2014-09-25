/** \file
 *
 * Provides a Python interface for the libkdtree++.
 *
 * \author Willi Richert <w.richert@gmx.net>
 *
 */

%module kdtree

%{
#define SWIG_FILE_WITH_INIT
#include "py-kdtree.hpp"
%}


%ignore record_t::operator[];
%ignore operator==;
%ignore operator<<;
%ignore KDTree::KDTree::operator=;
%ignore tac;

////////////////////////////////////////////////////////////////////////////////
// TYPE (int,int) -> unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_2iull record_t<2, int, unsigned long long> // cf. py-kdtree.hpp

%typemap(in) RECORD_2iull::point_t (RECORD_2iull::point_t point) {
   if (PyTuple_Check($input)) {
     if (PyArg_ParseTuple($input,"ii", &point[0],&point[1])!=0) 
     {
       $1 = point;
     } else {
       PyErr_SetString(PyExc_TypeError,"tuple must contain 2 ints");
       return NULL;
     }

   } else {
     PyErr_SetString(PyExc_TypeError,"expected a tuple.");
     return NULL;
   } 
  }
 
%typemap(in) RECORD_2iull (RECORD_2iull temp) {
  if (PyTuple_Check($input)) {
    if (PyArg_ParseTuple($input,"(ii)L", &temp.point[0],&temp.point[1], &temp.data)!=0) 
    {
      $1 = temp;
    } else {
      PyErr_SetString(PyExc_TypeError,"tuple must have 2 elements: (2 dim int vector, unsigned long long value)");
      return NULL;
    }

  } else {
    PyErr_SetString(PyExc_TypeError,"expected a tuple.");
    return NULL;
  } 
 }

 %typemap(out) RECORD_2iull * {
   RECORD_2iull * r = $1;
   PyObject* py_result;

   if (r != NULL) {

     py_result = PyTuple_New(2);
     if (py_result==NULL) {
       PyErr_SetString(PyErr_Occurred(),"unable to create a tuple.");
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 0, Py_BuildValue("(ii)", r->point[0],r->point[1]))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(a) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 1, Py_BuildValue("L", r->data))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(b) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }
   } else {
     py_result = Py_BuildValue("");
   }

   $result = py_result;
  }
 
%typemap(out) std::vector<RECORD_2iull  >*  {
  std::vector<RECORD_2iull >* v = $1;

  PyObject* py_result = PyList_New(v->size());
  if (py_result==NULL) {
    PyErr_SetString(PyErr_Occurred(),"unable to create a list.");
    return NULL;
  }
  std::vector<RECORD_2iull  >::const_iterator iter = v->begin();

  for (size_t i=0; i<v->size(); i++, iter++) {
    if (PyList_SetItem(py_result, i, Py_BuildValue("(ii)L", (*iter).point[0],(*iter).point[1], (*iter).data))==-1) {
      PyErr_SetString(PyErr_Occurred(),"(c) when setting element");

      Py_DECREF(py_result);
      return NULL;
    } else {
      //std::cout << "successfully set element " << *iter << std::endl;
    }
  }

  $result = py_result;
 }


////////////////////////////////////////////////////////////////////////////////
// TYPE (int,int,int) -> unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_3iull record_t<3, int, unsigned long long> // cf. py-kdtree.hpp

%typemap(in) RECORD_3iull::point_t (RECORD_3iull::point_t point) {
   if (PyTuple_Check($input)) {
     if (PyArg_ParseTuple($input,"iii", &point[0],&point[1],&point[2])!=0) 
     {
       $1 = point;
     } else {
       PyErr_SetString(PyExc_TypeError,"tuple must contain 3 ints");
       return NULL;
     }

   } else {
     PyErr_SetString(PyExc_TypeError,"expected a tuple.");
     return NULL;
   } 
  }
 
%typemap(in) RECORD_3iull (RECORD_3iull temp) {
  if (PyTuple_Check($input)) {
    if (PyArg_ParseTuple($input,"(iii)L", &temp.point[0],&temp.point[1],&temp.point[2], &temp.data)!=0) 
    {
      $1 = temp;
    } else {
      PyErr_SetString(PyExc_TypeError,"tuple must have 3 elements: (3 dim int vector, unsigned long long value)");
      return NULL;
    }

  } else {
    PyErr_SetString(PyExc_TypeError,"expected a tuple.");
    return NULL;
  } 
 }

 %typemap(out) RECORD_3iull * {
   RECORD_3iull * r = $1;
   PyObject* py_result;

   if (r != NULL) {

     py_result = PyTuple_New(2);
     if (py_result==NULL) {
       PyErr_SetString(PyErr_Occurred(),"unable to create a tuple.");
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 0, Py_BuildValue("(iii)", r->point[0],r->point[1],r->point[2]))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(a) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 1, Py_BuildValue("L", r->data))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(b) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }
   } else {
     py_result = Py_BuildValue("");
   }

   $result = py_result;
  }
 
%typemap(out) std::vector<RECORD_3iull  >*  {
  std::vector<RECORD_3iull >* v = $1;

  PyObject* py_result = PyList_New(v->size());
  if (py_result==NULL) {
    PyErr_SetString(PyErr_Occurred(),"unable to create a list.");
    return NULL;
  }
  std::vector<RECORD_3iull  >::const_iterator iter = v->begin();

  for (size_t i=0; i<v->size(); i++, iter++) {
    if (PyList_SetItem(py_result, i, Py_BuildValue("(iii)L", (*iter).point[0],(*iter).point[1],(*iter).point[2], (*iter).data))==-1) {
      PyErr_SetString(PyErr_Occurred(),"(c) when setting element");

      Py_DECREF(py_result);
      return NULL;
    } else {
      //std::cout << "successfully set element " << *iter << std::endl;
    }
  }

  $result = py_result;
 }


////////////////////////////////////////////////////////////////////////////////
// TYPE (int,int,int,int) -> unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_4iull record_t<4, int, unsigned long long> // cf. py-kdtree.hpp

%typemap(in) RECORD_4iull::point_t (RECORD_4iull::point_t point) {
   if (PyTuple_Check($input)) {
     if (PyArg_ParseTuple($input,"iiii", &point[0],&point[1],&point[2],&point[3])!=0) 
     {
       $1 = point;
     } else {
       PyErr_SetString(PyExc_TypeError,"tuple must contain 4 ints");
       return NULL;
     }

   } else {
     PyErr_SetString(PyExc_TypeError,"expected a tuple.");
     return NULL;
   } 
  }
 
%typemap(in) RECORD_4iull (RECORD_4iull temp) {
  if (PyTuple_Check($input)) {
    if (PyArg_ParseTuple($input,"(iiii)L", &temp.point[0],&temp.point[1],&temp.point[2],&temp.point[3], &temp.data)!=0) 
    {
      $1 = temp;
    } else {
      PyErr_SetString(PyExc_TypeError,"tuple must have 4 elements: (4 dim int vector, unsigned long long value)");
      return NULL;
    }

  } else {
    PyErr_SetString(PyExc_TypeError,"expected a tuple.");
    return NULL;
  } 
 }

 %typemap(out) RECORD_4iull * {
   RECORD_4iull * r = $1;
   PyObject* py_result;

   if (r != NULL) {

     py_result = PyTuple_New(2);
     if (py_result==NULL) {
       PyErr_SetString(PyErr_Occurred(),"unable to create a tuple.");
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 0, Py_BuildValue("(iiii)", r->point[0],r->point[1],r->point[2],r->point[3]))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(a) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 1, Py_BuildValue("L", r->data))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(b) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }
   } else {
     py_result = Py_BuildValue("");
   }

   $result = py_result;
  }
 
%typemap(out) std::vector<RECORD_4iull  >*  {
  std::vector<RECORD_4iull >* v = $1;

  PyObject* py_result = PyList_New(v->size());
  if (py_result==NULL) {
    PyErr_SetString(PyErr_Occurred(),"unable to create a list.");
    return NULL;
  }
  std::vector<RECORD_4iull  >::const_iterator iter = v->begin();

  for (size_t i=0; i<v->size(); i++, iter++) {
    if (PyList_SetItem(py_result, i, Py_BuildValue("(iiii)L", (*iter).point[0],(*iter).point[1],(*iter).point[2],(*iter).point[3], (*iter).data))==-1) {
      PyErr_SetString(PyErr_Occurred(),"(c) when setting element");

      Py_DECREF(py_result);
      return NULL;
    } else {
      //std::cout << "successfully set element " << *iter << std::endl;
    }
  }

  $result = py_result;
 }


////////////////////////////////////////////////////////////////////////////////
// TYPE (int,int,int,int,int) -> unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_5iull record_t<5, int, unsigned long long> // cf. py-kdtree.hpp

%typemap(in) RECORD_5iull::point_t (RECORD_5iull::point_t point) {
   if (PyTuple_Check($input)) {
     if (PyArg_ParseTuple($input,"iiiii", &point[0],&point[1],&point[2],&point[3],&point[4])!=0) 
     {
       $1 = point;
     } else {
       PyErr_SetString(PyExc_TypeError,"tuple must contain 5 ints");
       return NULL;
     }

   } else {
     PyErr_SetString(PyExc_TypeError,"expected a tuple.");
     return NULL;
   } 
  }
 
%typemap(in) RECORD_5iull (RECORD_5iull temp) {
  if (PyTuple_Check($input)) {
    if (PyArg_ParseTuple($input,"(iiiii)L", &temp.point[0],&temp.point[1],&temp.point[2],&temp.point[3],&temp.point[4], &temp.data)!=0) 
    {
      $1 = temp;
    } else {
      PyErr_SetString(PyExc_TypeError,"tuple must have 5 elements: (5 dim int vector, unsigned long long value)");
      return NULL;
    }

  } else {
    PyErr_SetString(PyExc_TypeError,"expected a tuple.");
    return NULL;
  } 
 }

 %typemap(out) RECORD_5iull * {
   RECORD_5iull * r = $1;
   PyObject* py_result;

   if (r != NULL) {

     py_result = PyTuple_New(2);
     if (py_result==NULL) {
       PyErr_SetString(PyErr_Occurred(),"unable to create a tuple.");
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 0, Py_BuildValue("(iiiii)", r->point[0],r->point[1],r->point[2],r->point[3],r->point[4]))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(a) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 1, Py_BuildValue("L", r->data))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(b) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }
   } else {
     py_result = Py_BuildValue("");
   }

   $result = py_result;
  }
 
%typemap(out) std::vector<RECORD_5iull  >*  {
  std::vector<RECORD_5iull >* v = $1;

  PyObject* py_result = PyList_New(v->size());
  if (py_result==NULL) {
    PyErr_SetString(PyErr_Occurred(),"unable to create a list.");
    return NULL;
  }
  std::vector<RECORD_5iull  >::const_iterator iter = v->begin();

  for (size_t i=0; i<v->size(); i++, iter++) {
    if (PyList_SetItem(py_result, i, Py_BuildValue("(iiiii)L", (*iter).point[0],(*iter).point[1],(*iter).point[2],(*iter).point[3],(*iter).point[4], (*iter).data))==-1) {
      PyErr_SetString(PyErr_Occurred(),"(c) when setting element");

      Py_DECREF(py_result);
      return NULL;
    } else {
      //std::cout << "successfully set element " << *iter << std::endl;
    }
  }

  $result = py_result;
 }


////////////////////////////////////////////////////////////////////////////////
// TYPE (int,int,int,int,int,int) -> unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_6iull record_t<6, int, unsigned long long> // cf. py-kdtree.hpp

%typemap(in) RECORD_6iull::point_t (RECORD_6iull::point_t point) {
   if (PyTuple_Check($input)) {
     if (PyArg_ParseTuple($input,"iiiiii", &point[0],&point[1],&point[2],&point[3],&point[4],&point[5])!=0) 
     {
       $1 = point;
     } else {
       PyErr_SetString(PyExc_TypeError,"tuple must contain 6 ints");
       return NULL;
     }

   } else {
     PyErr_SetString(PyExc_TypeError,"expected a tuple.");
     return NULL;
   } 
  }
 
%typemap(in) RECORD_6iull (RECORD_6iull temp) {
  if (PyTuple_Check($input)) {
    if (PyArg_ParseTuple($input,"(iiiiii)L", &temp.point[0],&temp.point[1],&temp.point[2],&temp.point[3],&temp.point[4],&temp.point[5], &temp.data)!=0) 
    {
      $1 = temp;
    } else {
      PyErr_SetString(PyExc_TypeError,"tuple must have 6 elements: (6 dim int vector, unsigned long long value)");
      return NULL;
    }

  } else {
    PyErr_SetString(PyExc_TypeError,"expected a tuple.");
    return NULL;
  } 
 }

 %typemap(out) RECORD_6iull * {
   RECORD_6iull * r = $1;
   PyObject* py_result;

   if (r != NULL) {

     py_result = PyTuple_New(2);
     if (py_result==NULL) {
       PyErr_SetString(PyErr_Occurred(),"unable to create a tuple.");
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 0, Py_BuildValue("(iiiiii)", r->point[0],r->point[1],r->point[2],r->point[3],r->point[4],r->point[5]))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(a) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 1, Py_BuildValue("L", r->data))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(b) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }
   } else {
     py_result = Py_BuildValue("");
   }

   $result = py_result;
  }
 
%typemap(out) std::vector<RECORD_6iull  >*  {
  std::vector<RECORD_6iull >* v = $1;

  PyObject* py_result = PyList_New(v->size());
  if (py_result==NULL) {
    PyErr_SetString(PyErr_Occurred(),"unable to create a list.");
    return NULL;
  }
  std::vector<RECORD_6iull  >::const_iterator iter = v->begin();

  for (size_t i=0; i<v->size(); i++, iter++) {
    if (PyList_SetItem(py_result, i, Py_BuildValue("(iiiiii)L", (*iter).point[0],(*iter).point[1],(*iter).point[2],(*iter).point[3],(*iter).point[4],(*iter).point[5], (*iter).data))==-1) {
      PyErr_SetString(PyErr_Occurred(),"(c) when setting element");

      Py_DECREF(py_result);
      return NULL;
    } else {
      //std::cout << "successfully set element " << *iter << std::endl;
    }
  }

  $result = py_result;
 }


////////////////////////////////////////////////////////////////////////////////
// TYPE (float,float) -> unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_2full record_t<2, float, unsigned long long> // cf. py-kdtree.hpp

%typemap(in) RECORD_2full::point_t (RECORD_2full::point_t point) {
   if (PyTuple_Check($input)) {
     if (PyArg_ParseTuple($input,"ff", &point[0],&point[1])!=0) 
     {
       $1 = point;
     } else {
       PyErr_SetString(PyExc_TypeError,"tuple must contain 2 ints");
       return NULL;
     }

   } else {
     PyErr_SetString(PyExc_TypeError,"expected a tuple.");
     return NULL;
   } 
  }
 
%typemap(in) RECORD_2full (RECORD_2full temp) {
  if (PyTuple_Check($input)) {
    if (PyArg_ParseTuple($input,"(ff)L", &temp.point[0],&temp.point[1], &temp.data)!=0) 
    {
      $1 = temp;
    } else {
      PyErr_SetString(PyExc_TypeError,"tuple must have 2 elements: (2 dim float vector, unsigned long long value)");
      return NULL;
    }

  } else {
    PyErr_SetString(PyExc_TypeError,"expected a tuple.");
    return NULL;
  } 
 }

 %typemap(out) RECORD_2full * {
   RECORD_2full * r = $1;
   PyObject* py_result;

   if (r != NULL) {

     py_result = PyTuple_New(2);
     if (py_result==NULL) {
       PyErr_SetString(PyErr_Occurred(),"unable to create a tuple.");
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 0, Py_BuildValue("(ff)", r->point[0],r->point[1]))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(a) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 1, Py_BuildValue("L", r->data))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(b) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }
   } else {
     py_result = Py_BuildValue("");
   }

   $result = py_result;
  }
 
%typemap(out) std::vector<RECORD_2full  >*  {
  std::vector<RECORD_2full >* v = $1;

  PyObject* py_result = PyList_New(v->size());
  if (py_result==NULL) {
    PyErr_SetString(PyErr_Occurred(),"unable to create a list.");
    return NULL;
  }
  std::vector<RECORD_2full  >::const_iterator iter = v->begin();

  for (size_t i=0; i<v->size(); i++, iter++) {
    if (PyList_SetItem(py_result, i, Py_BuildValue("(ff)L", (*iter).point[0],(*iter).point[1], (*iter).data))==-1) {
      PyErr_SetString(PyErr_Occurred(),"(c) when setting element");

      Py_DECREF(py_result);
      return NULL;
    } else {
      //std::cout << "successfully set element " << *iter << std::endl;
    }
  }

  $result = py_result;
 }


////////////////////////////////////////////////////////////////////////////////
// TYPE (float,float,float) -> unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_3full record_t<3, float, unsigned long long> // cf. py-kdtree.hpp

%typemap(in) RECORD_3full::point_t (RECORD_3full::point_t point) {
   if (PyTuple_Check($input)) {
     if (PyArg_ParseTuple($input,"fff", &point[0],&point[1],&point[2])!=0) 
     {
       $1 = point;
     } else {
       PyErr_SetString(PyExc_TypeError,"tuple must contain 3 ints");
       return NULL;
     }

   } else {
     PyErr_SetString(PyExc_TypeError,"expected a tuple.");
     return NULL;
   } 
  }
 
%typemap(in) RECORD_3full (RECORD_3full temp) {
  if (PyTuple_Check($input)) {
    if (PyArg_ParseTuple($input,"(fff)L", &temp.point[0],&temp.point[1],&temp.point[2], &temp.data)!=0) 
    {
      $1 = temp;
    } else {
      PyErr_SetString(PyExc_TypeError,"tuple must have 3 elements: (3 dim float vector, unsigned long long value)");
      return NULL;
    }

  } else {
    PyErr_SetString(PyExc_TypeError,"expected a tuple.");
    return NULL;
  } 
 }

 %typemap(out) RECORD_3full * {
   RECORD_3full * r = $1;
   PyObject* py_result;

   if (r != NULL) {

     py_result = PyTuple_New(2);
     if (py_result==NULL) {
       PyErr_SetString(PyErr_Occurred(),"unable to create a tuple.");
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 0, Py_BuildValue("(fff)", r->point[0],r->point[1],r->point[2]))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(a) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 1, Py_BuildValue("L", r->data))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(b) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }
   } else {
     py_result = Py_BuildValue("");
   }

   $result = py_result;
  }
 
%typemap(out) std::vector<RECORD_3full  >*  {
  std::vector<RECORD_3full >* v = $1;

  PyObject* py_result = PyList_New(v->size());
  if (py_result==NULL) {
    PyErr_SetString(PyErr_Occurred(),"unable to create a list.");
    return NULL;
  }
  std::vector<RECORD_3full  >::const_iterator iter = v->begin();

  for (size_t i=0; i<v->size(); i++, iter++) {
    if (PyList_SetItem(py_result, i, Py_BuildValue("(fff)L", (*iter).point[0],(*iter).point[1],(*iter).point[2], (*iter).data))==-1) {
      PyErr_SetString(PyErr_Occurred(),"(c) when setting element");

      Py_DECREF(py_result);
      return NULL;
    } else {
      //std::cout << "successfully set element " << *iter << std::endl;
    }
  }

  $result = py_result;
 }


////////////////////////////////////////////////////////////////////////////////
// TYPE (float,float,float,float) -> unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_4full record_t<4, float, unsigned long long> // cf. py-kdtree.hpp

%typemap(in) RECORD_4full::point_t (RECORD_4full::point_t point) {
   if (PyTuple_Check($input)) {
     if (PyArg_ParseTuple($input,"ffff", &point[0],&point[1],&point[2],&point[3])!=0) 
     {
       $1 = point;
     } else {
       PyErr_SetString(PyExc_TypeError,"tuple must contain 4 ints");
       return NULL;
     }

   } else {
     PyErr_SetString(PyExc_TypeError,"expected a tuple.");
     return NULL;
   } 
  }
 
%typemap(in) RECORD_4full (RECORD_4full temp) {
  if (PyTuple_Check($input)) {
    if (PyArg_ParseTuple($input,"(ffff)L", &temp.point[0],&temp.point[1],&temp.point[2],&temp.point[3], &temp.data)!=0) 
    {
      $1 = temp;
    } else {
      PyErr_SetString(PyExc_TypeError,"tuple must have 4 elements: (4 dim float vector, unsigned long long value)");
      return NULL;
    }

  } else {
    PyErr_SetString(PyExc_TypeError,"expected a tuple.");
    return NULL;
  } 
 }

 %typemap(out) RECORD_4full * {
   RECORD_4full * r = $1;
   PyObject* py_result;

   if (r != NULL) {

     py_result = PyTuple_New(2);
     if (py_result==NULL) {
       PyErr_SetString(PyErr_Occurred(),"unable to create a tuple.");
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 0, Py_BuildValue("(ffff)", r->point[0],r->point[1],r->point[2],r->point[3]))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(a) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 1, Py_BuildValue("L", r->data))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(b) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }
   } else {
     py_result = Py_BuildValue("");
   }

   $result = py_result;
  }
 
%typemap(out) std::vector<RECORD_4full  >*  {
  std::vector<RECORD_4full >* v = $1;

  PyObject* py_result = PyList_New(v->size());
  if (py_result==NULL) {
    PyErr_SetString(PyErr_Occurred(),"unable to create a list.");
    return NULL;
  }
  std::vector<RECORD_4full  >::const_iterator iter = v->begin();

  for (size_t i=0; i<v->size(); i++, iter++) {
    if (PyList_SetItem(py_result, i, Py_BuildValue("(ffff)L", (*iter).point[0],(*iter).point[1],(*iter).point[2],(*iter).point[3], (*iter).data))==-1) {
      PyErr_SetString(PyErr_Occurred(),"(c) when setting element");

      Py_DECREF(py_result);
      return NULL;
    } else {
      //std::cout << "successfully set element " << *iter << std::endl;
    }
  }

  $result = py_result;
 }


////////////////////////////////////////////////////////////////////////////////
// TYPE (float,float,float,float,float) -> unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_5full record_t<5, float, unsigned long long> // cf. py-kdtree.hpp

%typemap(in) RECORD_5full::point_t (RECORD_5full::point_t point) {
   if (PyTuple_Check($input)) {
     if (PyArg_ParseTuple($input,"fffff", &point[0],&point[1],&point[2],&point[3],&point[4])!=0) 
     {
       $1 = point;
     } else {
       PyErr_SetString(PyExc_TypeError,"tuple must contain 5 ints");
       return NULL;
     }

   } else {
     PyErr_SetString(PyExc_TypeError,"expected a tuple.");
     return NULL;
   } 
  }
 
%typemap(in) RECORD_5full (RECORD_5full temp) {
  if (PyTuple_Check($input)) {
    if (PyArg_ParseTuple($input,"(fffff)L", &temp.point[0],&temp.point[1],&temp.point[2],&temp.point[3],&temp.point[4], &temp.data)!=0) 
    {
      $1 = temp;
    } else {
      PyErr_SetString(PyExc_TypeError,"tuple must have 5 elements: (5 dim float vector, unsigned long long value)");
      return NULL;
    }

  } else {
    PyErr_SetString(PyExc_TypeError,"expected a tuple.");
    return NULL;
  } 
 }

 %typemap(out) RECORD_5full * {
   RECORD_5full * r = $1;
   PyObject* py_result;

   if (r != NULL) {

     py_result = PyTuple_New(2);
     if (py_result==NULL) {
       PyErr_SetString(PyErr_Occurred(),"unable to create a tuple.");
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 0, Py_BuildValue("(fffff)", r->point[0],r->point[1],r->point[2],r->point[3],r->point[4]))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(a) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 1, Py_BuildValue("L", r->data))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(b) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }
   } else {
     py_result = Py_BuildValue("");
   }

   $result = py_result;
  }
 
%typemap(out) std::vector<RECORD_5full  >*  {
  std::vector<RECORD_5full >* v = $1;

  PyObject* py_result = PyList_New(v->size());
  if (py_result==NULL) {
    PyErr_SetString(PyErr_Occurred(),"unable to create a list.");
    return NULL;
  }
  std::vector<RECORD_5full  >::const_iterator iter = v->begin();

  for (size_t i=0; i<v->size(); i++, iter++) {
    if (PyList_SetItem(py_result, i, Py_BuildValue("(fffff)L", (*iter).point[0],(*iter).point[1],(*iter).point[2],(*iter).point[3],(*iter).point[4], (*iter).data))==-1) {
      PyErr_SetString(PyErr_Occurred(),"(c) when setting element");

      Py_DECREF(py_result);
      return NULL;
    } else {
      //std::cout << "successfully set element " << *iter << std::endl;
    }
  }

  $result = py_result;
 }


////////////////////////////////////////////////////////////////////////////////
// TYPE (float,float,float,float,float,float) -> unsigned long long
////////////////////////////////////////////////////////////////////////////////

#define RECORD_6full record_t<6, float, unsigned long long> // cf. py-kdtree.hpp

%typemap(in) RECORD_6full::point_t (RECORD_6full::point_t point) {
   if (PyTuple_Check($input)) {
     if (PyArg_ParseTuple($input,"ffffff", &point[0],&point[1],&point[2],&point[3],&point[4],&point[5])!=0) 
     {
       $1 = point;
     } else {
       PyErr_SetString(PyExc_TypeError,"tuple must contain 6 ints");
       return NULL;
     }

   } else {
     PyErr_SetString(PyExc_TypeError,"expected a tuple.");
     return NULL;
   } 
  }
 
%typemap(in) RECORD_6full (RECORD_6full temp) {
  if (PyTuple_Check($input)) {
    if (PyArg_ParseTuple($input,"(ffffff)L", &temp.point[0],&temp.point[1],&temp.point[2],&temp.point[3],&temp.point[4],&temp.point[5], &temp.data)!=0) 
    {
      $1 = temp;
    } else {
      PyErr_SetString(PyExc_TypeError,"tuple must have 6 elements: (6 dim float vector, unsigned long long value)");
      return NULL;
    }

  } else {
    PyErr_SetString(PyExc_TypeError,"expected a tuple.");
    return NULL;
  } 
 }

 %typemap(out) RECORD_6full * {
   RECORD_6full * r = $1;
   PyObject* py_result;

   if (r != NULL) {

     py_result = PyTuple_New(2);
     if (py_result==NULL) {
       PyErr_SetString(PyErr_Occurred(),"unable to create a tuple.");
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 0, Py_BuildValue("(ffffff)", r->point[0],r->point[1],r->point[2],r->point[3],r->point[4],r->point[5]))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(a) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }

     if (PyTuple_SetItem(py_result, 1, Py_BuildValue("L", r->data))==-1) {
       PyErr_SetString(PyErr_Occurred(),"(b) when setting element");

       Py_DECREF(py_result);
       return NULL;
     }
   } else {
     py_result = Py_BuildValue("");
   }

   $result = py_result;
  }
 
%typemap(out) std::vector<RECORD_6full  >*  {
  std::vector<RECORD_6full >* v = $1;

  PyObject* py_result = PyList_New(v->size());
  if (py_result==NULL) {
    PyErr_SetString(PyErr_Occurred(),"unable to create a list.");
    return NULL;
  }
  std::vector<RECORD_6full  >::const_iterator iter = v->begin();

  for (size_t i=0; i<v->size(); i++, iter++) {
    if (PyList_SetItem(py_result, i, Py_BuildValue("(ffffff)L", (*iter).point[0],(*iter).point[1],(*iter).point[2],(*iter).point[3],(*iter).point[4],(*iter).point[5], (*iter).data))==-1) {
      PyErr_SetString(PyErr_Occurred(),"(c) when setting element");

      Py_DECREF(py_result);
      return NULL;
    } else {
      //std::cout << "successfully set element " << *iter << std::endl;
    }
  }

  $result = py_result;
 }


%include "py-kdtree.hpp"

%template () RECORD_2iull;
%template (KDTree_2Int)   PyKDTree<2, int, unsigned long long>;

%template () RECORD_3iull;
%template (KDTree_3Int)   PyKDTree<3, int, unsigned long long>;

%template () RECORD_4iull;
%template (KDTree_4Int)   PyKDTree<4, int, unsigned long long>;

%template () RECORD_5iull;
%template (KDTree_5Int)   PyKDTree<5, int, unsigned long long>;

%template () RECORD_6iull;
%template (KDTree_6Int)   PyKDTree<6, int, unsigned long long>;

%template () RECORD_2full;
%template (KDTree_2Float)   PyKDTree<2, float, unsigned long long>;

%template () RECORD_3full;
%template (KDTree_3Float)   PyKDTree<3, float, unsigned long long>;

%template () RECORD_4full;
%template (KDTree_4Float)   PyKDTree<4, float, unsigned long long>;

%template () RECORD_5full;
%template (KDTree_5Float)   PyKDTree<5, float, unsigned long long>;

%template () RECORD_6full;
%template (KDTree_6Float)   PyKDTree<6, float, unsigned long long>;

