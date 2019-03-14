#include <iostream>
#include "tiling.h"

using namespace std;

int main (int argc, char* argv[]){

  // tiling structure
  Tiling *T = new Tiling(10, 16, 500, 1236580000, 1236580010);

  // draw tiling
  TCanvas *mycanvas = new TCanvas("MyCanvas", "MyCanvas", 0, 0, 800, 600);
  mycanvas->cd();
  mycanvas->SetGridx();
  mycanvas->SetGridy();
  T->Draw();
  mycanvas->Print("./my_spectrogram.png");

  delete mycanvas;
  delete T;
  return 0;
}
