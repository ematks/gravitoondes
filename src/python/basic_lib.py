import numpy as np
import matplotlib.pyplot as plt

def basic_plot(file, fs = 1024, time_window=10000):
    """
    This function plots the start of a time series data file

    It shows and saves the figure in mybasicplot_timeseries.png
    """
    #to add: use a data path
    #DATA_PATH = pathlib.Path(__file__).parents[1] / "data"

    nb_points = fs * time_window

    data = np.load(file)
    data = data[0:nb_points]

    time, amplitude = data[0], data[1]

    # Plot the fft
    plt.figure(1)
    plt.plot(time, amplitude)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.title('timeserie')
    DPI = fig.get_dpi()
    fig.set_size_inches(1920.0/float(DPI),1080.0/float(DPI))

    plt.savefig('mybasicplot_timeseries.png')
    fig = plt.gcf() # get current figure
    plt.show()
    return
    
file = "data/GW150914/h1.data.00.npy"

basic_plot(file)