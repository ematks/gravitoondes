CXX          = g++ -Wno-deprecated -Wall -fPIC
CXXFLAGS     = $(shell $(ROOTSYS)/bin/root-config --cflags) -I.
ROOT_LIBS    = $(shell $(ROOTSYS)/bin/root-config --glibs)
FFTW_LIBS    = -L/usr/lib/x86_64-linux-gnu -lfftw3

SPECTRUM_EXE      = spectrum.exe
SPECTRUM_OBJS     = spectrum.o

all: $(SPECTRUM_EXE)

%.o : ../src/%.cc
	$(CXX) -c $< $(CXXFLAGS)

$(SPECTRUM_EXE) : $(SPECTRUM_OBJS)
	$(CXX) $^  -g -o $@ $(CXXFLAGS) $(ROOT_LIBS) $(FFTW_LIBS)

clean :
	- rm -f *Dict.* *.o *.so *.exe

