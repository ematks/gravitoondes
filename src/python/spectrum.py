import numpy as np
import matplotlib.pyplot as plt
import copy

#coucou

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

###define the window used for the PSD estimation
#define the number of point for the window (choose arbitrary value this is just to plot the shape)
n_window = 512000

hann_win = np.hanning(n_window)

#plot to check that the window looks good
plt.figure(3)
plt.plot(hann_win)
plt.title('Hann window')
define_plot_resolution()
plt.savefig('Hann_window.png')

##Compute the FFT
#define the sampling frequency [Hz]
fs = 1024

#define the frequency array
n = x.size
freq = np.fft.rfftfreq(len(y), 1/fs)

#compute the fft
fft_hann = np.fft.rfft(y * hann_win)
N = len(y)
#fft_neg = np.fft.fft(y)[N-1, int(N/2)+1]


#fft_real = np.real(fft)
fft_hann_abs = abs(fft_hann)/N
#fft_neg_abs = abs(fft_neg)/N

#Plot the fft
plt.figure(1)
plt.loglog(freq,fft_hann_abs)
plt.xlabel("frequency [Hz]")
plt.ylabel("log spectrum magnitude")
plt.title('FFT')
define_plot_resolution()
plt.show()
plt.savefig('fft.png')






#Plot the fft
plt.figure(1)
#plt.loglog(freq,fft_abs, label = 'fft')
#plt.loglog(freq,fft_neg_abs, 'g',  label= "neg fft")
plt.loglog(freq,fft_hann_abs, 'r',  label= "hann-windowed")
plt.xlabel("frequency [Hz]")
plt.ylabel("log spectrum magnitude")
plt.title('Hann windowed FFT')
plt.legend()
define_plot_resolution()
plt.show()
plt.savefig('fft.png')


"""
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






























