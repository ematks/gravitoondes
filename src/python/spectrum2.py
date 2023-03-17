import sys

import numpy as np
import matplotlib.pyplot as plt
import scipy

import sys

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

def plot_setup_fft():
    plt.figure(1)
    plt.xlabel("frequency [Hz]")
    plt.ylabel("log spectrum magnitude")
    plt.title('Hann windowed FFT')
    plt.legend()
    define_plot_resolution()

def plot_setup_psd():
    plt.figure(2)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("freq [Hz]")
    plt.ylabel("amplitude")
    plt.title('PSD')
    plt.legend
    define_plot_resolution()

def plot_fft(file, fs=1024, n_window = 512000):

    #load the data (the one in the numpy format)
    data = np.load(file)
    t = data[0] #time vector
    h = data[1] #h: relative variation delta(L)/L

    N = len(h) #nb of data points
    freq = np.fft.rfftfreq(N, 1/fs)

    ###define the window used for the PSD estimation
    #define the number of point for the window (choose arbitrary value this is just to plot the shape)
    hann_win = np.hanning(n_window)
    h_hann = h * hann_win

    fft = np.fft.rfft(h)
    fft_abs = abs(fft)/np.sqrt(N)

    fft_hann = np.fft.rfft(h_hann)
    fft_hann_abs = abs(fft_hann)/np.sqrt(N)

    plt.loglog(freq, fft_abs, label='han_win fft of '+file)

def plot_psd(file, fs=1024):

    #load the data (the one in the numpy format)
    data = np.load(file)
    t = data[0] #time vector
    h = data[1] #h: relative variation delta(L)/L
    N = len(h) #nb of data points

    ##Compute the PSD (median methode)
    sample_nb = 2 * fs
    freq, psd = scipy.signal.welch(h, fs, nperseg=sample_nb)

    plt.plot(freq, np.sqrt(psd))

def psd(file, fs=1024):

    #load the data (the one in the numpy format)
    data = np.load(file)
    t = data[0] #time vector
    h = data[1] #h: relative variation delta(L)/L
    N = len(h) #nb of data points

    ##Compute the PSD (median methode)
    sample_nb = 2 * fs
    freq, psd = scipy.signal.welch(h, fs, nperseg=sample_nb)

    return freq, psd

def psd2(h, fs=1024, T=2):

    ##Compute the PSD (median methode)
    sample_nb = T * fs
    freq, psd = scipy.signal.welch(h, fs, nperseg=sample_nb, average='median')

    return freq, psd

def normalize(x):
    return(x/np.linalg.norm(x))

def main():
    files = ["../../data/GW150914/h1.data.00.npy"]

    #plotting some FFTs
    plot_setup_fft()
    for file in files:
        plot_fft(file)
    plt.show()
    plt.savefig('fft.png')
    plt.close()

    #plotting some PSDs
    plot_setup_psd()
    for file in files:
        plot_psd(file)
    plt.show()
    plt.savefig('PSD.png')

if __name__ == "__main__":
    sys.exit(main())


#plot the PSD

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






























