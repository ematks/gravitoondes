import numpy as np
import matplotlib.pyplot as plt

def define_plot_resolution():
    """
    This function allow to define the resolution of a matplotlib plot on a way
    which is device independent. Put this before saving any of your plot to get
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

#define the sampling frequency [Hz]
fs = 1024

#define the duration [s]
duration = 10

#define the number of points
nsamples = fs * duration

#define the timeserie amplitude array (filled with a constant for example here)
amplitude = nsamples * [5]

#define the time array
time = np.arange(0,nsamples,1)

#define frequency of the signal
f1 = 200
a2 = np.sin(2*np.pi*f1*time)
print(len(a2))


#Plot the fft
plt.figure(1)
plt.plot(time,a2)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title('timeserie')
define_plot_resolution()
plt.savefig('myplot_timeseries.png')

# Frequency domain representation

FT = np.fft.fft(a2)/len(a2)           # Normalize amplitude
print(len(FT))
FT = FT[range(int(len(a2)/2))]  # Exclude sampling frequency

inv_FT = np.fft.ifft(a2)/len(a2)
inv_FT = inv_FT[range(int(len(a2)/2))]
tpCount = len(a2)

values = np.arange(int(tpCount/2))

timePeriod  = tpCount/fs

frequencies = values/timePeriod

plt.figure(2)
plt.loglog(frequencies,abs(FT))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title('frequency')
define_plot_resolution()
plt.savefig('myplot_frequency.png')

plt.figure(3)
plt.loglog(frequencies,abs(inv_FT)**2)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title('power spectrum')
define_plot_resolution()
plt.savefig('myplot_power.png')


plt.figure(4)
plt.plot(frequencies,abs(np.real(FT))**2)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title('power spectrum')
define_plot_resolution()
plt.savefig('myplot_real.png')

plt.figure(5)
plt.plot(frequencies,abs(np.imag(FT))**2)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title('power spectrum')
define_plot_resolution()
plt.savefig('myplot_imag.png')


