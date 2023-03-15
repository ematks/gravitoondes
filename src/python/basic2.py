import pathlib
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

DATA_PATH = pathlib.Path(__file__).parents[1] / "data"

file = "data/GW150914/h1.data.00.npy"

data = np.load(file)

Dt = 10000 #time in seconds
fs = 1024
nb_points= fs * Dt
data = data[0:nb_points]

#Plot the fft
plt.figure(1)
plt.plot(time,amplitude)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title('timeserie')
define_plot_resolution()
plt.savefig('myplot_timeseries.png')