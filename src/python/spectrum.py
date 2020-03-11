import numpy as np
import matplotlib.pyplot as plt
import ROOT
from scipy.signal import hann 
import copy


def define_plot_resolution():
    """
    This function allow to define the resolution of a matplotlib plot on a way
    wich is device independent. Put this before saving any of your plot to get
    homogeneous resolution.
    """
      
    fig = plt.gcf() # get current figure
    
    DPI = fig.get_dpi()
    fig.set_size_inches(1920.0/float(DPI),1080.0/float(DPI))
    
    return


#This commande turn matplotlib interactive mode off.
#Plot will not be desplayed as long as it is activate
#Note that plot are still saved with it
plt.ioff()

#magic ROOT commande
ROOT.ROOT.EnableImplicitMT()

#point out the root file
root_file = ROOT.TFile("/home/ducoin/gravitational-waves.git/data/GW150914/l1.data.07.root","open")

#get the datas
Tgraph = root_file.Get("data")

#get x and y axis
x_buff = Tgraph.GetX()
y_buff = Tgraph.GetY()

#plot the signal
plt.figure(1)
plt.plot(x_buff,y_buff)
plt.title('signal')
plt.xlabel('gps time [s]')
plt.ylabel('amplitude')
define_plot_resolution()
plt.savefig('signal.png')
#plt.show()
#N = Tgraph.GetN()
#x_buff.SetSize(N)
#y_buff.SetSize(N)

#convert to numpy array (starting from now you can forget that ROOT exist)
x_arr = np.array(x_buff)
y_arr = np.array(y_buff)

np.save('/home/ducoin/gravitational-waves.git/data/GW150914/l1.data.07.npy',np.array([x_arr,y_arr]))


"""
##Compute the FFT
#define the sampling frequency [Hz]
fs = 

#define the frequency array
freq = 


#compute the fft
fft = np.fft.fft(signal)



#keep the "interesting" part of this fft for the following
fft_to_plot=


#Plot the fft
plt.figure(2)
plt.plot(freq,np.log10(fft_to_plot))
plt.xlabel("frequency [Hz]")
plt.ylabel("log spectrum magnitude")
plt.title('FFT')
define_plot_resolution()
plt.savefig('fft.png')
#plt.show()


###define the window used for the PSD estimation
#define the number of point for the window (choose arbitrary value this is just to plot the shape)
n_window = 

hann_win = hann(n_window)

#plot to check that the window looks good
plt.figure(3)
plt.plot(hann_win)
plt.title('Hann window')
define_plot_resolution()
plt.savefig('Hann_window.png')
#plt.show()


##Compute the PSD (median methode)
frequency = 

S_welch = 

#plot the PSD
plt.figure(5)
plt.plot(frequency, S_welch)
plt.xscale('log')
plt.yscale('log')
plt.xlabel("freq [Hz]")
plt.ylabel("amplitude")
plt.title('PSD')
define_plot_resolution()
plt.savefig('PSD.png')
#plt.show()


##Whitening

pos_fft = 

whitened_fft = 

#plot the whitened fft
plt.figure(6)
plt.plot(frequency, whitened_fft)
plt.yscale('log')
plt.xlabel("frequency [Hz]")
plt.ylabel("amplitude")
plt.title('Whitened FFT')
define_plot_resolution()
plt.savefig('Whitened_FFT.png')

"""





























