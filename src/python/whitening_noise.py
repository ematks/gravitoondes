import numpy as np
import matplotlib.pyplot as plt
import scipy
import lib_GW


def define_plot_resolution():
    """
    This function allow to define the resolution of a matplotlib plot on a way
    wich is device independent. Put this before saving any of your plot to get
    homogeneous resolution.
    """

    fig = plt.gcf()  # get current figure

    DPI = fig.get_dpi()
    fig.set_size_inches(1920.0 / float(DPI), 1080.0 / float(DPI))

    return

""""
#load the data (the one in the numpy format)
file = "../../data/GW150914/h1.data.00.npy"
file2  =  "../../data/GW150914/l1.data.00.npy"
data = np.load(file)
data2 = np.load(file2)
t_h = data[0] #time vector
h = data[1] #h: relative variation delta(L)/L
"""

#Global PSD of the detector
global_freq_psd, global_psd = lib_GW.make_psd(data)

#Unfold global PSD of the detector
global_psd_unfold, global_freq_unfold = np.append(global_psd[:], np.flip(global_psd[1:])), np.append(global_freq_psd[:], -np.flip(global_freq_psd[1:]))

def sampling(data, fs=1024, T=4 ):
    """
        Function which allows to make T-sized segment of the data with a Tukey window to prevent spectral leakage,
        and return the Fourier transform of the segment

        Parameters
        ----------
        data : 1d array
               signal data
        fs : int
             sampling frequency
             default value = 1024
        T : int
             data segments size
             default value = 4s

        Return
        ----------
    """
    # number of points in the sample
    sample_nb = T * fs
    # nbs_sample = int(len(h)/sample_nb)

    # Extract a sample of T s and apply a Tukey window
    tukey = scipy.signal.windows.tukey(sample_nb)
    sample = h[:sample_nb] * tukey

    return (np.fft.fft(sample),np.fft.fftfreq(sample_nb, 1 / fs))

def whitenning_noise(data, fs=1024):
"""
    Function which returns a whitened signal
    Parameters
    ----------
    data : 1d array
           signal data

    Return
    ----------
    Whitened signal

"""

    fft_sample, freq_sample = sampling(data, fs=1024, T=4)

    #Alignment : interpolate to have the right number of points in PSD
    psd_unfold_interpolator = scipy.interpolate.interp1d(global_freq_unfold, global_psd_unfold)
    psd_unfold_interpolated = psd_unfold_interpolator(freq_sample)

    #Whitened sample in frequency domain
    fft_sample_whitened = fft_sample / np.sqrt(psd_unfold_interpolated/2)

    #check

    #Whitened sample in time domain
    sample_whitened = np.fft.ifft(fft_sample_whitened)

    #PSD of the whitened sample (ignoring the first and last second due to the Tukey window)
    freq_psd_whitened_sample, psd_whitened_sample = lib_GW.make_psd(np.real(sample_whitened[fs:3*fs]))

    #PSD of the non-whitened sample
    freq_psd_sample, psd_sample = lib_GW.make_psd(sample)

    #samples check
    plt.figure(1)
    plt.plot(t_h[:sample_nb], spectrum2.normalize(sample), label='sample', alpha=0.8)
    plt.plot(t_h[fs:fs*3], spectrum2.normalize(sample[fs:fs*3]), label='shortened sample')
    plt.plot(t_h[:sample_nb], spectrum2.normalize(sample_whitened), label='whitened sample', alpha=0.5)
    plt.legend(loc='best')
    plt.title('Samples check')
    plt.show()

    #plot the FFTs and PSD
    plt.figure(2)
    plt.yscale('log')
    plt.plot(freq_sample, spectrum2.normalize(abs(fft_sample)), label='normalised fft sample')
    #plt.plot(freq_unfold,psd_unfold)
    plt.plot(freq_sample,spectrum2.normalize(np.sqrt(psd_unfold_interpolated/2)), label='normalised global psd')
    plt.plot(freq_sample, spectrum2.normalize(abs(fft_sample_whitened)), label='normalised whitened fft sample')
    plt.legend(loc='best')
    plt.title('FFTs, PSD check')
    plt.show()

    print(np.mean(psd_whitened_sample))

    #Plotting the psd of whitened sample to check it
    plt.figure(3)
    plt.plot(freq_psd_whitened_sample, psd_whitened_sample, "g", label="psd of sample whitened signal")
    #plt.plot(freq_psd_sample, np.sqrt(abs(psd_sample)), "r", label="psd of sample signal")
    #plt.plot(freq_l, psd_l, "b", label="l1")
    #plt.plot(t_h_sample,inv_whitened)
    #plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("freq [Hz]")
    plt.ylabel("amplitude")
    plt.legend()

    define_plot_resolution()
    plt.show()

    plt.savefig('PSD.png')
