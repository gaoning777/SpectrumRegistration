all:
	(cd test;make)
	(cd src;make)

clean:
	(cd test;make clean)
	(cd src;make clean)
