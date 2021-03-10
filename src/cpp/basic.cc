/**
 * @file
 * @brief This program plots a data time series.
 */
#include <iostream>
#include <fftw3.h>
#include <TFile.h>
#include <TCanvas.h>
#include <TGraph.h>
#include <TH1.h>

using namespace std;

/**
 * @brief This program plots a data time series.
 */
int main (int argc, char* argv[]){

  // sampling frequency in Hz
  const int sampling_frequency = 1024;

  // duration of data segment [s]
  const int duration = 10;

  // number of points (samples)
  int nsamples = sampling_frequency * duration;
  
  // define a time series (array of double)
  double *x = new double [nsamples];

  // create a TGraph
  TGraph *mytimeseries = new TGraph(nsamples);

  // fill data vector (constant value)
  double time_x;
  for(int i=0; i<nsamples; i++){
    x[i] = 5.0;
    time_x = (double)i/(double)sampling_frequency;
    mytimeseries->SetPoint(i, time_x, x[i]);
  }

  // create canvas
  TCanvas *mycanvas = new TCanvas("MyCanvas", "MyCanvas", 0, 0, 800, 600);
  mycanvas->cd();
  mycanvas->SetGridx();
  mycanvas->SetGridy();

  // draw graph
  mytimeseries->Draw("APL");
  mytimeseries->GetHistogram()->GetXaxis()->SetTitle("Time [s]");
  mytimeseries->GetHistogram()->GetYaxis()->SetTitle("Amplitude");

  // print canvas
  mycanvas->Print("myplot_timeseries.png");

  // cleaning
  delete x;
  delete mytimeseries;
  delete mycanvas;
 
  return 0;
}
