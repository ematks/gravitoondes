import numpy as np
import matplotlib.pyplot as plt
import ROOT
#magic ROOT commande
ROOT.ROOT.EnableImplicitMT()

#point out the root file
root_file = ROOT.TFile("/home/ducoin/gravitational-waves.git/data/GW150914/h1.data.00.root","open")
#print("root_file =", root_file)

#get the datas
Tgraph = root_file.Get("data")
#print("Tgraph =", Tgraph)

#get x and y axis
x_buff = Tgraph.GetX()
y_buff = Tgraph.GetY()
#print("x_buff =", x_buff)
#print("y_buff =", y_buff)

#N = Tgraph.GetN()
#x_buff.SetSize(N)
#y_buff.SetSize(N)

#convert to numpy array (starting from now you can forget that ROOT exist)
x_arr = np.array(x_buff)
y_arr = np.array(y_buff)

#define the sampling frequency [Hz]
fs = 1024

#input data
n = x_arr.size

freq = (fs/2) * np.linspace(0,1,n/2)
#freq = np.fft.fftfreq(n)

#fft = np.fft.fft(np.sin(2*np.pi*20*x_arr))
fft = np.fft.fft(y_arr)

fft_real = np.real(fft)
fft_imag = np.imag(fft)

fft_m_real = fft_real[0:int(n/2)]
fft_m_imag = fft_real[0:int(n/2)]

plt.plot(freq,np.log10(fft_m_real))
plt.xlabel("frequency [Hz]")
plt.ylabel("spectrum magnitude")




