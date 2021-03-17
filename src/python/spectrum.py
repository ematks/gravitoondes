import numpy as np
import matplotlib.pyplot as plt
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

#load the data (the one in the numpy format)
data = np.load("../../data/GW150914/h1.data.00.npy")
x = data[0]
y = data[1]

##Compute the FFT
#define the sampling frequency [Hz]
fs = 1024

#define the frequency array
n = x.size
freq = (fs/2) * np.linspace(0,1,int(n/2))

#compute the fft
fft = np.fft.fft(y)

#keep the real part of this fft
fft_to_plot = fft

fft_real = np.real(fft)
fft_real = abs(fft)

fft_m_real = fft_real[0:int(n/2)]

#Plot the fft
plt.figure(1)
plt.plot(freq,np.log10(fft_m_real))
plt.xlabel("frequency [Hz]")
plt.ylabel("log spectrum magnitude")
plt.title('FFT')
define_plot_resolution()
plt.savefig('fft.png')



"""
###define the window used for the PSD estimation
#define the number of point for the window (choose arbitrary value this is just to plot the shape)
n_window = 

hann_win = np.hanning(n_window)

#plot to check that the window looks good
plt.figure(3)
plt.plot(hann_win)
plt.title('Hann window')
define_plot_resolution()
plt.savefig('Hann_window.png')



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






























