# Set up basic variables:
CC         = g++
CFLAGS     = -c -Wall -O2 -mtune=native 
LDFLAGS    =

# List of sources:
SOURCES1    = nano_auto_import.cpp
OBJECTS1    = $(SOURCES1:.cpp=.o)
SOURCES2    = lib_auto_import.cpp
OBJECTS2    = $(SOURCES2:.cpp=.o)


# Name of executable target:
EXECUTABLE1 = nano_auto_import
EXECUTABLE2 = lib_auto_import

all: $(SOURCES) $(EXECUTABLE1) $(EXECUTABLE2)
	
$(EXECUTABLE1): $(OBJECTS1)
	$(CC) $(LDFLAGS) $(OBJECTS1) -o $@

$(EXECUTABLE2): $(OBJECTS2)
	$(CC) $(LDFLAGS) $(OBJECTS2) -o $@


.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm *.o $(EXECUTABLE1) $(EXECUTABLE2)
