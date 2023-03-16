import numpy as np
import matplotlib.pyplot as plt
import scipy


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
t_l = data2[0]
l = data2[1]
fs = 1024

sample_nb = 4*fs
tukey = scipy.signal.windows.tukey(sample_nb)

##Compute the PSD (median methode)
freq_h, psd_h = scipy.signal.welch(h, fs, window=tukey, nperseg=sample_nb)
freq_l, psd_l = scipy.signal.welch(l, fs,window=tukey, nperseg=sample_nb)

freq_h_cutoff = np.where(freq_h > 20.0, freq_h, 0)


#plot the PSD
plt.figure(3)
plt.plot(freq_h_cutoff, psd_h, "r", label="h1")
#plt.plot(freq_l, psd_l, "b", label="l1")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("freq [Hz]")
plt.ylabel("amplitude")
plt.title('PSD')
plt.legend()
plt.show()
define_plot_resolution()
plt.savefig('PSD.png')
