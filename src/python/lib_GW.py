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

def make_psd(h, fs=1024, T=2):
    """
This function computes the psd of some data h, using median-summing welch method and hann window
    Parameters
    ----------
    h : (ndarray)
        the data usde to compute the psd
    fs : (int)
        sampling frequency of h, default = 1024
    T: (int)
        period used to define welch method's sampling bits, expressed in seconds

    Returns
    -------
    freq : (ndarray{fs})
        range of frequencies associated to h
    psd: (ndarray{fs/2})
        power spectral density of h
    """
    sample_nb = T * fs
    freq, psd = scipy.signal.welch(h, fs, nperseg=sample_nb, average='median')

    return freq, psd

def normalize(x):
    """
    Parameters
    ----------
    x: (ndarray)
        array to normalise

    Returns
    -------
    norm_x: (ndarray{len(x)})
        normalised x array
    """
    norm_x = x/np.linalg.norm(x)
    return norm_x

def main():
    """
    Main fucntion to test the psd function
    """

    file_example = "../../data/GW150914/h1.data.00.npy"

    data=np.load(file_example)
    h = data[1]
    freq, psd = make_psd(h)

    plt.figure(3)
    plt.plot(freq, psd, "g", label="psd of "+file_example)
    plt.yscale('log')
    plt.xlabel("freq [Hz]")
    plt.ylabel("amplitude")
    plt.legend()

    plt.show()


if __name__ == "__main__":
    sys.exit(main())































