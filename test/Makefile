CXX          = g++ -Wno-deprecated -Wall -fPIC
CXXFLAGS     = $(shell $(ROOTSYS)/bin/root-config --cflags) -I../src/
LDFLAGS	     = -shared
ROOT_LIBS    = $(shell $(ROOTSYS)/bin/root-config --glibs)
FFTW_LIBS    = -L/usr/lib/x86_64-linux-gnu -lfftw3

SPECTRUM_EXE      = spectrum.exe
SPECTRUM_OBJS     = spectrum.o

OBJECTS        = tiling.o
TARGET         = libtiling.so

TILER_EXE      = tiler.exe
TILER_OBJS     = tiler.o

all: $(TARGET) $(SPECTRUM_EXE) $(TILER_EXE)

%.o : ../src/%.cc
	$(CXX) -c $< $(CXXFLAGS)

$(TARGET) : $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $@ $(LDFLAGS) $(ROOT_LIBS)

$(SPECTRUM_EXE) : $(SPECTRUM_OBJS)
	$(CXX) $^  -g -o $@ $(CXXFLAGS) $(ROOT_LIBS) $(FFTW_LIBS)

$(TILER_EXE) : $(TILER_OBJS)
	$(CXX) $^  -g -o $@ $(CXXFLAGS) -L. -ltiling $(ROOT_LIBS) $(FFTW_LIBS)

clean :
	- rm -f *Dict.* *.o *.so *.exe

