all:
	gcc -c -O2 -D_REENTRANT -D_GNU_SOURCE -Wall -Wno-unused -fno-strict-aliasing -DBASE_THREADSAFE -I. ning-server.c
	g++ -o zeromq ning-server.o zeromq.cpp -std=c++11 -Wl,--start-group -lpthread -lm -lrt -lcrypt -luuid -I/usr/local/include -L/usr/local/lib -lczmq -lzmq -Wl,--end-group -L.
	gcc -c -O2 -D_REENTRANT -D_GNU_SOURCE -Wall -Wno-unused -fno-strict-aliasing -DBASE_THREADSAFE -I. ning-client.c
	gcc -O2 -D_REENTRANT -D_GNU_SOURCE -Wall -Wno-unused -fno-strict-aliasing -DBASE_THREADSAFE ning-client.o -o ning-client -Wl,--start-group -lpthread -lm -lrt -lcrypt -luuid -I/usr/local/include -L/usr/local/lib -lczmq -lzmq -Wl,--end-group -L.

clean:
	rm *.o
	rm ning-client
	rm zeromq
