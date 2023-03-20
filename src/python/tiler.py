import numpy as np
import matplotlib.pyplot as plt
from math import *


def nextPowerOf2(n: int):
    """
    This function returns the closest power of 2 bigger than n

    If the entered int is negative, returns 0 to show miscontent
    """
    if n < 0:
        print("The entered integer is negative. Cannot compute next opxer of 2")
        return 0
    power = 0
    while n != 0:
        power += 1
        n = n // 2

    return power


class spectrogram:
    """
    Dedicated class to build a spectrogram with a Q plan methode
    """

    def def_time_range(self, time_range):
        """
	    This function is used to define the time range within the class
	    """

        self.time_range = time_range

        return 0

    def Q_bin_numb(self):
        """
        This function is used to define the Number of Q bins
        """

        self.N_q = 1

        return

    def freq_bin_numb(self):
        """
    	This function is used to define the Number of frequency bins
    	"""

        f_nyquist = self.fs / 2.0
        Q = self.Q
        phi_min = self.fs / 4.0 * Q / np.sqrt(11)  # equation 10 in method paper
        phi_max = int(f_nyquist / (1 + np.sqrt(11) / Q))  # equation 11 in method paper

        s_phi = np.sqrt(2 + Q ** 2) / 2 * np.log(phi_max / phi_min)
        self.N_phi = ceil(s_phi / 2 * np.sqrt(self.mu_max / 3))  # equation 21

        return

    def freqtiles_center_array(self):
        """
        This function define the center of each frequency bins and store it in an array
        """

        f_nyquist = self.fs / 2.0
        Q = self.Q
        # these can be inputted as arguments of class
        phi_min = self.fs / 4.0 * Q / np.sqrt(11)  # equation 10 in method paper
        phi_max = int(f_nyquist / (1 + np.sqrt(11) / Q))  # equation 11 in method paper

        self.freq = [phi_min * np.power(phi_max / phi_min, (0.5 + l) / self.N_phi) for l in
                     range(self.N_phi)]  # equation24

        return

    def time_bin_numb(self):
        """
        This function define the number of tiles needed for each frequency bins (stored in a list) 
        
        WARNING: self.N_t is a list
        """

        s_tau = 2 * np.pi * self.freq / Q * 4 * self.fs  # tau range equals 4s for our data
        self.N_t = [nextPowerOf2(s_tau[i] / (2 * np.sqrt(self.mu_max / 3))) for i in range(len(s_tau))] #equation 20

        return

    def __init__(self, Q=8.253, mu_max=0.2, time_range=4, fs=1024):
        # a verifier les initialisations de base, appeler les fcontions
        self.N_q = 1
        self.Q = Q
        self.mu_max = mu_max
        self.fs = fs
        self.def_time_range(self, time_range) #defines self.time_range
        self.freq_bin_numb(self) #defines self.N_phi
        self.time_bin_numb(self) #defines self.N_t
        self.freqtiles_center_array(self) #defines self.freq

        """
        To be filled
        """
        # The total number of point of the signal
        self.n = self.fs * 4  # we are dealing with 4s signals

        self.freq_range = [20, self.freq[-1]]

    def build_Q_plan_row(self):
        """
        This function build a list of empty row, The size of each row 
        correspond to the size needed in the final Q plan 

        self.Q_plan_matrix_rows is a list of array
        """

        Q_plan_matrix_rows = []

        for i in range(len(self.N_t)):
            Q_plan_matrix_rows += [np.empty((self.N_t[i]))]

        self.Q_plan_matrix_rows = Q_plan_matrix_rows

        return

    def build_Q_plan_matrix(self):
        """
        Build a empty matrix with the highest resolution of the Q plan
        """
        # building a square matrix of N_phi * N_tau
        self.Q_plan_matrix = np.empty((len(self.Q_plan_matrix_rows), len(self.Q_plan_matrix_rows[
                                                                             -1])))  # last element of rows is taken to have the maximal resolution which corresponds to the phi_max row

        return

    def tile_coord_to_matrix_coords(self, tile_coord):


        return matrix_coord
    def tile_fill(self, tile_coord, value): #from coord changes the value of the tile

    def tile_content(self, tile_coord): #from coord gives the value of the tile
    def
    def fill_row_for_demo(self):
        """
        This function fill the Q plan matrix with dummies values just to show its structure
        """
        for i in range(len(self.Q_plan_matrix_rows)):
            for j in range(len(self.Q_plan_matrix_rows[i])):
                tile_fill(self,  [i,j])

        # fill the rows with dummies values (0 or 1 alternatively)

        return

    def fill_matrix(self):
        """
        This function fill the Q plan matrix with the values in each row
        """
        # To be done

        return

    def plot_matrix(self):
        """
        This function plot the Q plan matrix
        """
        # Need to be customized

        plt.figure(1)
        plt.imshow(self.Q_plan_matrix)
        plt.colorbar()
        plt.savefig('tile dummies values.png')
        return


############ MAIN ################


# Define the Q
Q = 8.253
time_range = 4
# define the minimal energy loss at 20%
mu_max = 20 / 100

spectro = spectrogram(Q, mu_max, time_range)
#spectro.def_time_range([-0.1, 0.1])
#spectro.freq_bin_numb()
#spectro.freqtiles_center_array()
#spectro.time_bin_numb()
#spectro.build_Q_plan_row()
#spectro.build_Q_plan_matrix()

spectro.fill_row_for_demo()

spectro.fill_matrix()

spectro.plot_matrix()
