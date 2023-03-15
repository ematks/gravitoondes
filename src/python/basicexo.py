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

#define the sampling frequency [Hz]
fs = 1024

#define the duration [s]
duration = 10

#define the number of points
nsamples = fs * duration

#define the time array
time = np.linspace(0,duration,nsamples)

#define frequency of the signal
f1 = 200
sin_ex = np.sin(2*np.pi*f1*time)
gauss_ex = np.exp(-(time-2)**2/(2*0.1**2))
data= gauss_ex


#Plot the fft
plt.figure(1)
plt.plot(time,data)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title('timeserie')
define_plot_resolution()
plt.savefig('myplot_timeseries.png')

# Frequency domain representation

""" Tried to do it by hand, i's a failure for now
FT = np.fft.fft(data)/len(data)           # Normalize amplitude
print(len(FT))
N = len(data)
range_pos = range(0, int(N/2))
FT_pos = FT[range_pos]  # Exclude sampling frequency
range_neg = range(N-1, int(N/2), -1)
FT_neg = FT[range_neg]
FT_neg=np.append(FT[0], FT_neg)


FT_sum = FT_neg - FT_pos
"""

FT=np.fft.rfft(data)

inv_FT = np.fft.irfft(FT)

tpCount = len(data)

values = np.arange(int(tpCount/2)+1)

timePeriod  = tpCount/fs

frequencies = values/timePeriod


#sinus plots
plt.subplot(411)
plt.plot(frequencies,abs(FT))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title('frequency')
define_plot_resolution()

plt.subplot(412)
plt.plot(time,abs(inv_FT))
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title('inv_FT')
define_plot_resolution()

plt.subplot(413)
plt.plot(frequencies,abs(np.real(FT))**2)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title('real_FT')
define_plot_resolution()

plt.subplot(414)
plt.plot(frequencies,abs(np.imag(FT))**2)
plt.xlabel("Frequency")
plt.ylabel("Amplitude")
plt.title('imag_FT')
define_plot_resolution()
plt.savefig('myplot_all.png')


