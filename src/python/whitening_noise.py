import numpy as np
import matplotlib.pyplot as plt
import scipy

import spectrum2
import PSD_generator
from spectrum2 import psd

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

#load the data (the one in the numpy format)
file = "../../data/GW150914/h1.data.00.npy"
file2  =  "../../data/GW150914/l1.data.00.npy"
data = np.load(file)
data2 = np.load(file2)
t_h = data[0] #time vector
h = data[1] #h: relative variation delta(L)/L

fs = 1024

T = 4 #period of sample in seconds
sample_nb = T*fs
tukey = scipy.signal.windows.tukey(sample_nb)

#nbs_sample = int(len(h)/sample_nb)

sample = h[:sample_nb] * tukey #sample de 4s
fft_sample = np.fft.fft(sample)
freq_sample = np.fft.fftfreq(len(sample), 1/fs)

global_freq_psd, global_psd = PSD_generator.global_freq, PSD_generator.global_PSD_h

global_psd_unfold, global_freq_unfold = np.append(global_psd[:], np.flip(global_psd[1:])), np.append(global_freq_psd[:], -np.flip(global_freq_psd[1:]))
psd_unfold_interpolator = scipy.interpolate.interp1d(global_freq_unfold, global_psd_unfold)
psd_unfold_interpolated = psd_unfold_interpolator(freq_sample)

fft_sample_whitened = fft_sample / np.sqrt(psd_unfold_interpolated/2)

#check
sample_whitened = np.fft.ifft(fft_sample_whitened)

freq_psd_whitened_sample, psd_whitened_sample = spectrum2.psd2(np.real(sample_whitened[fs:3*fs]), T=2)
freq_psd_sample, psd_sample = spectrum2.psd2(sample, T=2)

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
