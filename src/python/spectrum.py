import numpy as np
import matplotlib.pyplot as plt
import scipy


def define_plot_resolution():
    """
    This function allow to define the resolution of a matplotlib plot on a way
    which is device independent. Put this before saving any of your plot to get
    homogeneous resolution.
    """

    fig = plt.gcf()  # get current figure

    dpi = fig.get_dpi()
    fig.set_size_inches(1920.0 / float(dpi), 1080.0 / float(dpi))

    return


# This command turn matplotlib interactive mode off.
# Plot will not be displayed as long as it is activated
# Note that plot are still saved with it
plt.ioff()

# load the data (the one in the numpy format)
file = "../../data/GW150914/h1.data.00.npy"
file2 = "../../data/GW150914/l1.data.00.npy"
data = np.load(file)
data2 = np.load(file2)
t_h = data[0]  # time vector
h = data[1]  # h: relative variation delta(L)/L
t_l = data2[0]
l = data2[1]

fs = 1024  # sampling frequency in Hz
N = len(h)  # nb of data points
# n = t.size #dont know what is that used for
freq = np.fft.rfftfreq(N, 1 / fs)

###define the window used for the PSD estimation
# define the number of point for the window (choose arbitrary value this is just to plot the shape)
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

# compute the fft
# Re-normalize and take module/abs of fft

fft_h = np.fft.rfft(h)
fft_abs_h = abs(fft_h) / np.sqrt(N)

fft_l = np.fft.rfft(l)
fft_abs_l = abs(fft_l) / np.sqrt(N)

# fft_neg = np.fft.fft(h)[N: int(N/2)-1: -1]
# fft_neg = np.append(np.fft.fft(h)[0], fft_neg)
# fft_neg_abs = abs(fft_neg)/N

fft_hann_h = np.fft.rfft(h_hann)
fft_hann_abs_h = abs(fft_hann_h) / np.sqrt(N)

fft_hann_l = np.fft.rfft(h_hann)
fft_hann_abs_l = abs(fft_hann_l) / np.sqrt(N)

# Plot the datas
plt.figure(1)
plt.plot(t_h, h, 'b', label='raw data')
plt.plot(t_h, h_hann, 'g', label='hann_windowed data')
plt.xlabel("Time [s]")
plt.ylabel("Magnitude of relative compression h")
plt.title('Data')
define_plot_resolution()
plt.legend(loc='best')
plt.savefig('data.png')

# Plot the ffts
plt.figure(2)
plt.loglog(freq, fft_abs_h, label='fft')
# plt.loglog(freq,fft_neg_abs, 'g',  label= "Negative fft")
# plt.loglog(freq,fft_neg_abs-fft_abs, 'y',  label= "difference between Negative fft and fft")
plt.loglog(freq, fft_hann_abs_h, 'r', label="hann-windowed fft")
plt.xlabel("frequency [Hz]")
plt.ylabel("log spectrum magnitude")
plt.title('Hann windowed FFT')
plt.legend()
define_plot_resolution()
plt.savefig('fft.png')

#Compute the PSD (median methode)
sample_nb = 2 * fs
freq_h, psd_h = scipy.signal.welch(h, fs, nperseg=sample_nb, average='median')
freq_l, psd_l = scipy.signal.welch(l, fs, nperseg=sample_nb, average='median')

# plot the PSD
plt.figure(3)
plt.plot(freq_h, psd_h, "r", label="h1")
plt.plot(freq_l, psd_l, "b", label="l1")
plt.xlim(20.0, 512.0)
plt.xscale('log')
plt.yscale('log')
plt.xlabel("freq [Hz]")
plt.ylabel("amplitude")
plt.title('PSD')
plt.legend()
plt.show()
define_plot_resolution()
plt.savefig('PSD.png')
