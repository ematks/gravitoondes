/**
 * @file
 * @brief This program plots the data time series and the data spectrum.
 */
#include <iostream>
#include <fftw3.h>
#include <TFile.h>
#include <TCanvas.h>
#include <TGraph.h>
#include <TH1.h>

using namespace std;

/**
 * @brief This program plots the data time series and the data spectrum.
 * @details The input timeseries "h1.data.03.root" is opened as a TGraph.
 * It is Fourier-transformed with fftw routines.
 * The data vector in the Fourier domain is plotted.
 */
int main (int argc, char* argv[]){

  // load root file
  TFile *myfile = new TFile("../data/GW150914/h1.data.03.root","read");

  // get TGraph data
  TGraph *mytimeseries = (TGraph*)myfile->Get("data");

  // close file
  myfile->Close();

  // cosmetics
  mytimeseries->SetTitle("Hanford time series");
  mytimeseries->GetHistogram()->GetXaxis()->SetNoExponent();
  mytimeseries->GetHistogram()->GetXaxis()->SetTitle("GPS time [s]");
  mytimeseries->GetHistogram()->GetYaxis()->SetTitle("Strain amplitude [-]");

  // create canvas
  TCanvas *mycanvas = new TCanvas("MyCanvas", "MyCanvas", 0, 0, 800, 600);
  mycanvas->cd();
  mycanvas->SetGridx();
  mycanvas->SetGridy();

  // draw graph
  mytimeseries->Draw("APL");

  // print canvas
  mycanvas->Print("myplot_timeseries.png");

  // sampling frequency [Hz]
  int fs = 1024;

  // data total duration [s]
  int duration = 500;

  // number of points
  int N = fs * duration;
  
  // input data
  fftw_complex *in = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
  for(int p=0; p<N; p++){
    in[p][0] = mytimeseries->GetY()[p];// real part
    in[p][1] = 0.0;// imaginary part
  }

  // output data
  fftw_complex *out = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);

  // FFT plan
  fftw_plan p = fftw_plan_dft_1d(N, in, out, FFTW_FORWARD, FFTW_ESTIMATE);

  // perform FFT
  fftw_execute(p);

  // TGraph for spectrum
  TGraph *myspectrum = new TGraph(N/2);
 
  // fill spectrum
  for(int p=0; p<N/2; p++)
    myspectrum->SetPoint(p, (double)p*(double)fs/(double)N, 2*sqrt(out[p][0]*out[p][0]+out[p][1]*out[p][1]));
  
  // plot and save spectrum
  mycanvas->cd();
  myspectrum->Draw("APL");
  mycanvas->SetLogy();
  mycanvas->SetLogx();
  mycanvas->Print("myplot_spectrum.png");

  // cleaning
  fftw_destroy_plan(p);
  fftw_free(in); fftw_free(out);
  delete mytimeseries;
  delete mycanvas;
 
  return 0;
}
