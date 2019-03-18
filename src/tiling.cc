#include "tiling.h"

Tiling::Tiling(const int aNfrequencyRows,
	       const double aFrequencyMin, const double aFrequencyMax,
	       const double aTimeMin, const double aTimeMax){

  QPrime = 8.5 / sqrt(11.0);

  // frequency bins
  double *fbins = new double [aNfrequencyRows+1];
  for(int f=0; f<aNfrequencyRows+1; f++)
    fbins[f]=aFrequencyMin*pow(10.0,f*log10(aFrequencyMax/aFrequencyMin)/(double)aNfrequencyRows);

  // number of time bins
  Nt = new int [aNfrequencyRows];
  Nt[0]=4;
  Nt[1]=4;
  Nt[2]=7;
  Nt[3]=16;
  Nt[4]=32;

  // histogram definition
  tile_map = new TH2D("tile_map", "Spectrogram",
		      Nt[aNfrequencyRows-1], aTimeMin, aTimeMax,
		      aNfrequencyRows, fbins);
  delete fbins;
    
  tile_map->SetStats(0);
  tile_map->GetXaxis()->SetNoExponent();
  tile_map->GetXaxis()->SetTitle("Time [s]");
  tile_map->GetYaxis()->SetTitle("Frequency [Hz]");
  tile_map->GetZaxis()->SetTitle("SNR [-]");
  //tile_map->GetZaxis()->SetRangeUser(0,1025);

  // band variables
  bandMultiple       = new int       [GetNBands()];
  bandFFT            = new fftw_plan [GetNBands()];
  bandin             = new fftw_complex* [GetNBands()];
  bandout            = new fftw_complex* [GetNBands()];
  bandWindow_r       = new double*   [GetNBands()];
  bandWindow_i       = new double*   [GetNBands()];
  bandWindowSize     = new int       [GetNBands()];

  // fill band structures
  double windowargument;
  double winnormalization;
  double ifftnormalization;
  double delta_f;// Connes window 1/2-width
  int k, end;
  for(int f=0; f<GetNBands(); f++){
    bandMultiple[f]=tile_map->GetXaxis()->GetNbins()/Nt[f];
    delta_f=GetBandFrequency(f)/QPrime;
    bandWindowSize[f] = 2 * (int)floor(delta_f*(GetTimeMax()-GetTimeMin())) + 1;
    bandWindow_r[f]   = new double [bandWindowSize[f]];
    bandWindow_i[f]   = new double [bandWindowSize[f]];
    bandin[f] = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * Nt[f]);
    bandout[f] = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * Nt[f]);
    bandFFT[f] = fftw_plan_dft_1d(Nt[f], bandin[f], bandout[f], FFTW_BACKWARD, FFTW_ESTIMATE);

    ifftnormalization = 1.0 / (GetTimeMax()-GetTimeMin());
    winnormalization  = sqrt(315.0*QPrime/128.0/GetBandFrequency(f));

    // bisquare window
    end=(bandWindowSize[f]+1)/2;
    for(k=0; k<end; k++){
      windowargument=2.0*(double)k/(double)(bandWindowSize[f] - 1);
      bandWindow_r[f][k] = winnormalization*ifftnormalization*(1.0-windowargument*windowargument)*(1.0-windowargument*windowargument)*TMath::Cos(TMath::Pi()*(double)k/(double)Nt[f]);// bisquare window (1-x^2)^2 and phase shift
      bandWindow_i[f][k] = winnormalization*ifftnormalization*(1.0-windowargument*windowargument)*(1.0-windowargument*windowargument)*TMath::Sin(TMath::Pi()*(double)k/(double)Nt[f]);// bisquare window (1-x^2)^2 and phase shift
    }
    // do not save 0s in the center
    end=bandWindowSize[f];
    for(; k<end; k++){
      windowargument=2.0*(double)(k-end)/(double)(bandWindowSize[f] - 1);
      bandWindow_r[f][k] = -winnormalization*ifftnormalization*(1.0-windowargument*windowargument)*(1.0-windowargument*windowargument)*TMath::Cos(TMath::Pi()*(double)(k-bandWindowSize[f]+Nt[f])/(double)Nt[f]);// bisquare window (1-x^2)^2 and phase shift
      bandWindow_i[f][k] = -winnormalization*ifftnormalization*(1.0-windowargument*windowargument)*(1.0-windowargument*windowargument)*TMath::Sin(TMath::Pi()*(double)(k-bandWindowSize[f]+Nt[f])/(double)Nt[f]);// bisquare window (1-x^2)^2 and phase shift
    }

  }

}

Tiling::~Tiling(){
for(int f=0; f<GetNBands(); f++){
  delete bandWindow_r[f];
  delete bandWindow_i[f];
  fftw_free(bandin[f]);
  fftw_free(bandout[f]);
  fftw_destroy_plan(bandFFT[f]);
 }
 delete tile_map;
 delete Nt;
 delete bandMultiple;
 delete bandWindow_r;
 delete bandWindow_i;
 delete bandWindowSize;
 delete bandin;
 delete bandout;
 delete bandFFT;
   
}

void Tiling::ProjectData(fftw_complex *aDataFft){
}

void Tiling::SetTileContent(const int aFrequencyIndex,
			    const int aTimeIndex,
			    const double aContent){
  
  int binstart=(aTimeIndex*bandMultiple[aFrequencyIndex])+1;
  int binstop=binstart+bandMultiple[aFrequencyIndex];
  //cout<<aFrequencyIndex<<" "<<aTimeIndex<<" "<<aContent<<" "<<binstart<<" "<<binstop<<endl;
  for(int b=binstart; b<binstop; b++)
    tile_map->SetBinContent(b,aFrequencyIndex+1,aContent);
  
  return;
}
