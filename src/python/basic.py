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

#load the data (the one in the numpy format)
data = np.load("../../data/GW150914/h1.data.00.npy")
x = data[0]
y = data[1]


#Plot the fft
plt.figure(1)
plt.plot(x,y)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title('timeserie')
define_plot_resolution()
plt.savefig('myplot_timeseries.png')

