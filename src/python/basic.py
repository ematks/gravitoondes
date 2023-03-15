import numpy as np
import matplotlib.pyplot as plt

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


#Plot the fft
plt.figure(1)
plt.plot(time,amplitude)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title('timeserie')
define_plot_resolution()
plt.savefig('myplot_timeseries.png')

#basic biche pt2

