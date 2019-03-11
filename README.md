# GravitationalWaves

## Contributors
[Florent Robinet](mailto:robinet@lal.in2p3.fr)

## Scope of the project

This project is about impementing some basic algorithms used to search for gravitational waves in the data of interferometric detectors, such as the LIGO and Virgo detectors. To test the code, we will use the data set associated to the first detection of a gravitational wave event in LIGO detectors: GW150914. This event originated from the merger of a binary black hole system.

This project is divided into two parts:
- The first part is about developing a code to process the LIGO strain time series. This idea is to implement some basic technics in signal processing such as noise estimation, noise whitening, and short Fourier transforms. The final result will be to plot the spectrogram of GW150914 to visualize the gravitational-wave signal.
- The second part of the project is about performing the data analysis which led to the discovery of GW150914. Starting from a list of triggers from the two LIGO detectors, a coincident analysis must be developed as well as a noise estimation. 

## Documentation

- [GW150914 discovery paper](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.116.061102)
- [Method note](./doc/method/signal.pdf): the signal analysis is presented in a short note.
- [ROOT](https://root.cern/) libraries are used as a tool box to perform analyses. See also the [C++ class documentation](https://root.cern.ch/doc/master/index.html)
- Fourier transforms are performed with [FFTW](http://www.fftw.org/). See also the [documentation](http://www.fftw.org/fftw3_doc/).
- [qsort algorithm](http://www.cplusplus.com/reference/cstdlib/qsort/)

## Data sets

- `./data/GW150914/?1.data.root`: LIGO time series data, sampled at 1024 Hz) around the time of GW150914 (GPS = 1126256640 to 1126260736). Hanford (H1) and Livingston (L1) data are saved separately in ROOT files as [TGraph](https://root.cern.ch/doc/master/classTGraph.html) object.

## Project 1: GW150914 spectrogram

![H1-GW150914-spectrogram](./doc/images/H1-GW150914-spectrogram.png "GW150914 spectrogram in LIGO-Hanford data.")

- use the LIGO time series data in `./data/GW150914/?1.data.root`
- play with FFTW to Fourier-transform the time series
  - plot the full array of coefficients after the Fourier transform.
  - plot the entire data set in a single graph and compute the spectrum.
- compute the power spectrum density (PSD) using a robust estimator
- whiten the time series
- tile the time-frequency plane
- develop a function to compute the bisquare window for each tile
- project the data onto each time-frequency tile and compute the SNR
- plot the final result

## Project 2: GW150914 detection

To be completed

