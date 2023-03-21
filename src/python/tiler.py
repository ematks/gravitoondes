import numpy as np
import matplotlib.pyplot as plt
from math import *
import sys

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

    return 2**power


class spectrogram:
    """
    Dedicated class to build a spectrogram with a Q plan methode
    """

    def def_time_range(self, time_range):
        """
	    This function is used to define the time range within the class
	    """

        self.time_range = time_range

        return

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
        #self.phi_min = Q / np.sqrt(11)  # equation 10 in method paper
        self.phi_min = 1.31303 #hardcoded
        self.phi_max = f_nyquist / (1 + np.sqrt(11) / Q)  # equation 11 in method paper

        s_phi = np.sqrt(2 + Q ** 2) / 2 * np.log(self.phi_max / self.phi_min)
        N_phi_tempo = s_phi / (2 * np.sqrt(self.mu_max / 3))
        self.N_phi = ceil(N_phi_tempo)  # equation 21

        return

    def freqtiles_center_array(self):
        """
        This function define the center of each frequency bins and store it in an array
        """

        f_nyquist = self.fs / 2.0
        Q = self.Q
        # these can be inputted as arguments of class

        self.freq = [self.phi_min * np.power(self.phi_max / self.phi_min, (0.5 + l) / self.N_phi) for l in range(self.N_phi)]  # equation24

        return

    def time_bin_numb(self):
        """
        This function define the number of tiles needed for each frequency bins (stored in a list) 
        
        WARNING: self.N_t is a list
        """

        s_tau = [2 * np.pi * self.freq[i]/ self.Q * self.time_range for i in range(len(self.freq))]  # tau range equals 4s for our data
        self.N_t = [nextPowerOf2(s_tau[i] / (2 * np.sqrt(self.mu_max / 3))) for i in range(len(s_tau))]  # equation 20

        return

    def build_Q_plan_row(self):
        """
        This function build a list of empty row, The size of each row
        correspond to the size needed in the final Q plan

        self.Q_plan_matrix_rows is a list of array
        """

        Q_plan_matrix_rowss = []

        for i in range(len(self.N_t)):
            Q_plan_matrix_rowss += [np.zeros(self.N_t[i])]

        self.Q_plan_matrix_rows = Q_plan_matrix_rowss

        return

    def build_Q_plan_matrix(self):
        """
        Build a empty matrix with the highest resolution of the Q plan
        """
        # building a square matrix of N_phi * N_tau
        self.Q_plan_matrix = np.zeros((len(self.Q_plan_matrix_rows), len(self.Q_plan_matrix_rows[-1])))
        # last element of rows is taken to have the maximal resolution which corresponds to the phi_max row

        return


    def __init__(self, Q=8.253, mu_max=0.2, time_range=4, fs=1024):
        # a verifier les initialisations de base, appeler les fcontions
        self.Q_plan_matrix_rows = [[]]
        self.Q_plan_matrix = [[]]
        self.N_q = 1
        self.Q = Q
        self.mu_max = mu_max
        self.fs = fs
        self.phi_min = 1.0
        self.phi_max = 1.0
        self.def_time_range(time_range)  # defines self.time_range
        self.freq_bin_numb()  # defines self.N_phi
        self.freqtiles_center_array()  # defines self.freq
        self.time_bin_numb()  # defines self.N_t


        """
        To be filled
        """
        # The total number of point of the signal
        self.n = self.fs * 4  # we are dealing with 4s signals

        self.freq_range = [20, self.freq[-1]]

        self.build_Q_plan_row()
        self.build_Q_plan_matrix()


    def tile_coord_to_matrix_coords(self, tile_coord):
        [i, j] = tile_coord  # please note that (i,j) coordinates for the tiles correspond to increasing phi and tau
        # where (k,l) coordinates for the matrix correspond to decreasing phi and increasing tau
        N_t = self.N_t
        tile_size = int(N_t[-1] / N_t[i])
        matrix_coords = [[self.N_phi - i - 1, m] for m in range(tile_size * j, tile_size * (j + 1))]
        return matrix_coords  # returns a list of doubles correponding to the matrix coordnates in the (i,j) tile

    def tile_fill(self, tile_coord, value):  # from tile coord changes the value of the tile in the matrix
        for [k,l] in self.tile_coord_to_matrix_coords(tile_coord):
            self.Q_plan_matrix[k,l] = value

    def tile_content(self, tile_coord):  # from tile coord gives the value of the tile
        return self.Q_plan_matrix[self.tile_coord_to_matrix_coords(tile_coord)[0]]


    def fill_row_for_demo(self):
        """
        This function fill the Q plan matrix with dummies values just to show its structure
        """
        for i in range(len(self.Q_plan_matrix_rows)):
            for j in range(len(self.Q_plan_matrix_rows[i])):
                self.tile_fill([i, j], j%2)
        # fill the rows with dummies values (0 or 1 alternatively)

        return

    def fill_matrix(self, tile_values):
        """
        This function fill the Q plan matrix with the values in each row
        """
        # To be done
        for i in range(tile_values):
            for j in range(len(tile_values[i])):
                self.tile_fill([i,j], values[i,j])
        return

    def plot_matrix(self):
        """
        This function plot the Q plan matrix
        """
        # Need to be customized

        plt.figure(1)
        plt.imshow(self.Q_plan_matrix, aspect =  'auto', interpolation=None, extent=[0, self.time_range, self.freq_range[0], self.freq_range[1]])
        plt.colorbar()
#        plt.xscale('log')
        plt.yscale('log')
        plt.ylabel("Frequency [Hz]")
        plt.xlabel("Time [s]")
        plt.savefig('tile dummies values.png')
        return

    def window(self):
        w = []
        for l in range(len(self.freq)):
            w_l= []
            M_l = int(2* self.freq[l]*np.sqrt(11)/self.Q * self.time_range)

            for k in range(0, (M_l+1)/2 ):
                w_l = np.append(w_l, (1-(2*k/(M_l-1))**2)**2)
            for k in range((M_l+1)/2, M_l):
                w_l = np.append(w_l, (1-(2*(k-M_l)/(M_l-1))**2)**2)
            W_b = np.linalg.norm(w_l)
            w = np.append(w, W_b*w_l)
        self.W = w
        return





def main():
    ############ MAIN ################


    # Define the Q
    Q = 8.25
    time_range = 4
    mu_max = 20 / 100     # define the minimal energy loss at 20%

    spectro = spectrogram(Q, mu_max, time_range)

    spectro.fill_row_for_demo()
#    spectro.tile_fill([42,1000],2.0)
    #spectro.fill_matrix()

    spectro.plot_matrix()
    plt.show()

if __name__ == "__main__":
    sys.exit(main())
