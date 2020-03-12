import numpy as np
import matplotlib.pyplot as plt



def nextPowerOf2(n): 
    """
    This function return the closest power of 2 bigger than n
    """

    power = 
      
    return power


class spectrogram:
    
    """
    Dedicated class to build a spectrogram with a Q plan methode
    """

    
    def __init__(self,Q,mu_max):
        
        self.Q = Q
        self.mu_max = mu_max
        self.fs = 1024
        
        """
        To be filled
        """
        #The total number of point of the signal
        self.n = 
        
        
        self.freq_range = [20,self.freq[-1]]


    def def_time_range(self,time_range):

        self.time_range = time_range
    
        return


    def Q_bin_numb(self):
        #define the Number of Q bins
        
        
        self.N_q =  
    
        return 


    def freq_bin_numb(self):
        #define the Number of frequency bins
        
        
        self.N_phi =
    
        return 


    def freqtiles_center_array(self):
        """
        This function define the center of each frequency bins and store it in a array
        
        """
            
        self.freq_array = 
        
        return
    
    
    def time_bin_numb(self):
        """
        This function define the number of tiles needed for each frequency bins (stored in a list) 
        
        WARNING: self.N_t is a list

        """
            
        self.N_t = 

        return 
    
    
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
        
        self.Q_plan_matrix  = np.empty(( len(self.Q_plan_matrix_rows), len(self.Q_plan_matrix_rows[0]) ))

        return


    def fill_row_for_demo(self):
        """
        This function fill the Q plan matrix with dummies values just to show its structure
        """
        
        
        #fill the rows with dummies values (0 or 1 alternatively)


        return
            
        
    def fill_matrix(self):  
        """
        This function fill the Q plan matrix with the values in each row
        """        
        

               
        return 


    def plot_matrix(self):
        """
        This function plot the Q plan matrix
        
        Need to be customized
        """
        
        plt.figure(1)
        plt.imshow(self.Q_plan_matrix)
        plt.colorbar()
        plt.savefig('tile dummies values.png')
        return


############ MAIN ################


#Define the Q
Q = 9.21

#define the minimal energy loss at 20%
mu_max = 20/100

spectro = spectrogram(Q,mu_max)

spectro.def_time_range([-0.1,0.1])

spectro.freq_bin_numb()

spectro.freqtiles_center_array()

spectro.time_bin_numb()

spectro.build_Q_plan_row()

spectro.build_Q_plan_matrix()

spectro.fill_row_for_demo()

spectro.fill_matrix()

spectro.plot_matrix()







































