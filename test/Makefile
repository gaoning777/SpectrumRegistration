# Set up basic variables:
CC         = g++
CFLAGS     = -c -Wall -O2 -mtune=native 
LDFLAGS    =

# List of sources:
SOURCES1    = nano_test.cpp
OBJECTS1    = $(SOURCES1:.cpp=.o)

# Name of executable target:
EXECUTABLE1 = nano_test

all: $(SOURCES) $(EXECUTABLE1)
	
$(EXECUTABLE1): $(OBJECTS1)
	$(CC) $(LDFLAGS) $(OBJECTS1) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm *.o $(EXECUTABLE1)
