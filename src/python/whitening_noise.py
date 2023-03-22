import numpy as np
import matplotlib.pyplot as plt
import scipy
import lib_GW
import sys

import PSD_generator

#Global PSD of the detector (Hanford)
global_freq_psd, global_psd = PSD_generator.global_freq,  PSD_generator.global_psd_h

#Unfold global PSD of the detector
global_psd_unfold = np.append(global_psd[:], np.flip(global_psd[1:]))
global_freq_unfold = np.append(global_freq_psd[:], -np.flip(global_freq_psd[1:]))


def whitening_noise(h, fs=1024, T=4, return_whitened_psd=False, fft_psd_plot=False):
    """
    Function which returns a whitened signal
    Parameters
    ----------
    h : (1d array)
           signal data

    T: (int)
        period used to define welch method's sampling bits, expressed in seconds

    Return
    ----------
    Whitened signal
    :type fs: object
    """
    sample_nb = T * fs
    # nbs_sample = int(len(h)/sample_nb)

    # Extract a sample of T s and apply a Tukey window
    tukey = scipy.signal.windows.tukey(sample_nb)
    sample = h[:sample_nb] * tukey

    fft_sample, freq_sample = np.fft.fft(sample), np.fft.fftfreq(sample_nb, 1 / fs)

    #Alignment : interpolate to have the right number of points in PSD
    psd_unfold_interpolator = scipy.interpolate.interp1d(global_freq_unfold, global_psd_unfold)
    psd_unfold_interpolated = psd_unfold_interpolator(freq_sample)

    #Whitened sample in frequency domain
    fft_sample_whitened = fft_sample / np.sqrt(psd_unfold_interpolated/2)

    # Whitened sample in time domain
    sample_whitened = np.fft.ifft(fft_sample_whitened)

    #check
    if fft_psd_plot:
        # plot the FFTs and PSD
        plt.figure(2)
        plt.yscale('log')
        plt.plot(freq_sample, lib_GW.normalize(abs(fft_sample)), label='normalised fft sample')
        #plt.plot(freq_unfold,psd_unfold)
        plt.plot(freq_sample, lib_GW.normalize(np.sqrt(psd_unfold_interpolated / 2)), label='normalised global psd')
        plt.plot(freq_sample, lib_GW.normalize(abs(fft_sample_whitened)), label='normalised whitened fft sample')
        plt.legend(loc='best')
        plt.title('FFTs, PSD check')
        plt.show()

    """ 
    #PSD of the non-whitened sample
    freq_psd_sample, psd_sample = lib_GW.make_psd(sample)
    """
    if return_whitened_psd:  # PSD of the whitened sample (ignoring the first and last second due to the Tukey window)
        return lib_GW.make_psd(np.real(sample_whitened[fs:3*fs]))
    else:
        return sample_whitened


def main():
    # load the data (the one in the numpy format)
    files_h = PSD_generator.npy_files_h

    data = np.load(files_h[0])

    t = data[0]  # time vector
    h = data[1]  # h: relative variation delta(L)/L

    sample_whitened = whitening_noise(h, fs=1024, T=4)
    freq_psd_whitened_sample, psd_whitened_sample = whitening_noise(h, fs=1024, T=4, return_whitened_psd=True)

    T = 4
    fs = 1024
    sample_nb = T * fs
    sample = h[:sample_nb]
    # samples check
    plt.figure(1)
    plt.plot(t[:sample_nb], lib_GW.normalize(sample), label='sample', alpha=0.8)
    plt.plot(t[fs:fs * 3], lib_GW.normalize(sample[fs:fs * 3]), label='shortened sample')
    plt.plot(t[:sample_nb], lib_GW.normalize(sample_whitened), label='whitened sample', alpha=0.5)
    plt.legend(loc='best')
    plt.title('Samples check')
    plt.show()

    # Plotting the psd of whitened sample to check it
    plt.figure(3)
    plt.plot(freq_psd_whitened_sample, psd_whitened_sample, "g", label="psd of sample whitened signal")
    # plt.plot(freq_psd_sample, np.sqrt(abs(psd_sample)), "r", label="psd of sample signal")
    # plt.plot(freq_l, psd_l, "b", label="l1")
    # plt.plot(t_h_sample,inv_whitened)
    # plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("freq [Hz]")
    plt.ylabel("amplitude")
    plt.legend()

    lib_GW.define_plot_resolution()
    plt.show()

    plt.savefig('PSD.png')


if __name__ == "__main__":
    sys.exit(main())
