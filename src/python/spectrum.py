import numpy as np
import matplotlib.pyplot as plt
import scipy
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
file = "../../data/GW150914/h1.data.00.npy"
data = np.load(file)
t = data[0] #time vector
h = data[1] #h: relative variation delta(L)/L

fs = 1024 #sampling frequency in Hz
N = len(h) #nb of data points
#n = t.size #dont know what is that used for
freq = np.fft.rfftfreq(N, 1/fs)


###define the window used for the PSD estimation
#define the number of point for the window (choose arbitrary value this is just to plot the shape)
n_window = 512000
hann_win = np.hanning(n_window)
h_hann = h * hann_win
"""
#plot to check that the window looks good
plt.figure(3)
plt.plot(hann_win)
plt.title('Hann window')
define_plot_resolution()
plt.savefig('Hann_window.png')
"""


#compute the fft
#Renormalise and take module/abs of fft

fft = np.fft.rfft(h)
fft_abs = abs(fft)/np.sqrt(N)

#fft_neg = np.fft.fft(h)[N: int(N/2)-1: -1]
#fft_neg = np.append(np.fft.fft(h)[0], fft_neg)
#fft_neg_abs = abs(fft_neg)/N

fft_hann = np.fft.rfft(h_hann)
fft_hann_abs = abs(fft_hann)/np.sqrt(N)




#Plot the datas
plt.figure(1)
plt.plot(t, h, 'b', label='raw data')
plt.plot(t, h_hann, 'g', label='hann_windowed data')
plt.xlabel("Time [s]")
plt.ylabel("Magnitude of relative compression h")
plt.title('Data')
define_plot_resolution()
plt.legend(loc='best')
plt.show()
plt.savefig('data.png')


#Plot the ffts
plt.figure(1)
plt.loglog(freq,fft_abs, label = 'fft')
#plt.loglog(freq,fft_neg_abs, 'g',  label= "Negative fft")
#plt.loglog(freq,fft_neg_abs-fft_abs, 'y',  label= "difference between Negative fft and fft")
plt.loglog(freq,fft_hann_abs, 'r',  label= "hann-windowed fft")
plt.xlabel("frequency [Hz]")
plt.ylabel("log spectrum magnitude")
plt.title('Hann windowed FFT')
plt.legend()
define_plot_resolution()
plt.show()
plt.savefig('fft.png')


##Compute the PSD (median methode)
sample_nb = 2*fs
freq, psd = scipy.signal.welch(h, fs, nperseg=sample_nb)


#plot the PSD
plt.figure(5)
plt.plot(freq, psd)
plt.xscale('log')
plt.yscale('log')
plt.xlabel("freq [Hz]")
plt.ylabel("amplitude")
plt.title('PSD')
plt.show()
define_plot_resolution()
plt.savefig('PSD.png')

"""

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






























