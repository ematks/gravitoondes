#ifndef __tiling__
#define __tiling__

#include "TCanvas.h"
#include "TH2D.h"

using namespace std;

class Tiling {

 public:

  // constructor
  Tiling(const int aNfrequencyRows,
	 const double aFrequencyMin, const double aFrequencyMax,
	 const double aTimeMin, const double aTimeMax);

  // destructor
  virtual ~Tiling();

  // returns the time range
  inline double GetTimeRange(void){
    return tile_map->GetXaxis()->GetBinUpEdge(tile_map->GetNbinsX())-tile_map->GetXaxis()->GetBinLowEdge(1); 
  };

  // returns the minimum time
  inline double GetTimeMin(void){ 
    return tile_map->GetXaxis()->GetBinLowEdge(1); 
  };

  // returns the maximum time
  inline double GetTimeMax(void){ 
    return tile_map->GetXaxis()->GetBinUpEdge(tile_map->GetNbinsX()); 
  };

  // returns the minimum frequency
  inline double GetFrequencyMin(void){ 
    return tile_map->GetYaxis()->GetBinLowEdge(1);
  };

  // returns the maximum frequency
  inline double GetFrequencyMax(void){ 
    return tile_map->GetYaxis()->GetBinUpEdge(tile_map->GetNbinsY()); 
  };

  // returns the number of frequency bands
  inline int GetNBands(void){ 
    return tile_map->GetNbinsY();
  };

  // returns the frequency start of a band
  inline double GetBandStart(const int aBandIndex){ 
    return tile_map->GetYaxis()->GetBinLowEdge(aBandIndex+1);
  };

  // returns the frequency end of a band
  inline double GetBandEnd(const int aBandIndex){ 
    return tile_map->GetYaxis()->GetBinUpEdge(aBandIndex+1);
  };

  // returns the band width
  inline double GetBandWidth(const int aBandIndex){ 
    return tile_map->GetYaxis()->GetBinWidth(aBandIndex+1);
  };

  // draw the tiling structure
  inline void Draw(void){
    return tile_map->Draw("COLZ");
  }

 private:

  TH2 *tile_map; // tiling histogram
  int Nt;        // number of time bins

};

#endif
