INCLUDE_DIR=../include
CXX=g++

PY_INCLUDE_DIR=$(shell python-config --includes)

# CPPFLAGS is used by the default rules. Using "override" and "+="
# allows the user to prepend things to CPPFLAGS on the command line.
override CPPFLAGS += -I$(INCLUDE_DIR) -pedantic -Wno-long-long -Wall -ansi -pedantic

# swig bindings
py-kdtree: _kdtree.so
#	cp _kdtree.so kdtree.py ../../

py-kdtree.i: py-kdtree.i.tmpl py-kdtree.hpp.tmpl gen-swig-hpp.py
	python gen-swig-hpp.py

py-kdtree_wrap.cxx: py-kdtree.i py-kdtree.hpp py-kdtree.i.tmpl py-kdtree.hpp.tmpl
	swig -python -modern -c++ py-kdtree.i

_kdtree.so: py-kdtree_wrap.cxx 
	$(CXX) $(CPPFLAGS) -c py-kdtree_wrap.cxx -I$(PY_INCLUDE_DIR) -I$(INCLUDE_DIR)
	$(CXX) $(CPPFLAGS) -shared  py-kdtree_wrap.o -o _kdtree.so

clean:
	rm -f *.so py-kdtree_wrap.cxx *.o kdtree.py *.pyc py-kdtree.i py-kdtree.hpp

.PHONY: clean

