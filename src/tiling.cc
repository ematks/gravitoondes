#include "tiling.h"

Tiling::Tiling(const int aNfrequencyRows,
	       const double aFrequencyMin, const double aFrequencyMax,
	       const double aTimeMin, const double aTimeMax){
  Nt=100;
  tile_map = new TH2D("tile_map", "Spectrogram",
		      Nt, aTimeMin, aTimeMax,
		      aNfrequencyRows, aFrequencyMin, aFrequencyMax);
  tile_map->SetStats(0);
  tile_map->GetXaxis()->SetNoExponent();
  tile_map->GetXaxis()->SetTitle("Time [s]");
  tile_map->GetYaxis()->SetTitle("Frequency [Hz]");
  tile_map->GetZaxis()->SetTitle("SNR [-]");

  // fill the tiling structure (default)
  for(int bx=1; bx<=Nt; bx++)
    for(int by=1; by<=GetNBands(); by++)
      tile_map->SetBinContent(bx, by, bx+by);
}

Tiling::~Tiling(){
  delete tile_map;
}
