import numpy as np
import matplotlib.pyplot as plt
import ROOT
from scipy.signal import hann 
import copy



    


#magic ROOT commande
ROOT.ROOT.EnableImplicitMT

#point out the root file
root_file = ROOT.TFile("/home/ducoin/gravitational-waves.git/data/GW150914/h1.data.00.root","open")
#print("root_file =", root_file)

#get the datas
Tgraph = root_file.Get("data")
#print("Tgraph =", Tgraph)

#get x and y axis
x_buff = Tgraph.GetX()
y_buff = Tgraph.GetY()
#print("x_buff =", x_buff)
#print("y_buff =", y_buff)

#N = Tgraph.GetN()
#x_buff.SetSize(N)
#y_buff.SetSize(N)

#convert to numpy array (starting from now you can forget that ROOT exist)
x_arr = np.array(x_buff)
y_arr = np.array(y_buff)

#define the sampling frequency [Hz]
fs = 1024

#input data
n = x_arr.size

freq = (fs/2) * np.linspace(0,1,n/2)
#freq = np.fft.fftfreq(n)

#fft = np.fft.fft(np.sin(2*np.pi*20*x_arr))
fft = np.fft.fft(y_arr)

fft_real = np.real(fft)
fft_imag = np.imag(fft)

fft_m_real = fft_real[0:int(n/2)]
fft_m_imag = fft_real[0:int(n/2)]

#plt.plot(freq,np.log10(fft_m_real))
#plt.xlabel("frequency [Hz]")
#plt.ylabel("log spectrum magnitude")
#plt.show()


###define the window used for the PSD estimation
#define the number of point for the window
n_window = 100

hann_win = hann(n_window)

#plot to check that the window looks good
#plt.figure(2)
#plt.plot(hann_win)
#plt.show()

#define the signal lenght
M = 500 * fs

#define the lenght of the segment
N = 2**(int( np.log(M)/np.log(2) ) -1)

#define the number of segments
K = int( (2*M) /N )-1

#define the shift 
D = int( (M-N)/(K-1) )

#define the pulsation range
#omega = freq * 2* np.pi
omega = np.arange(0,512,0.5)


#define the window
hann_win = hann(N)   


S_welch = []


for i in range(len(omega)):
    print("i = {}/{}".format(i,len(omega)))
    
    
    
    
    for k in range(K):
        #print("k = {}/{}".format(k,K))
        list_for_given_k = np.array([])
        
        #winwod on the part of the signal to treat at this given k
        #goes from n=0 to n=N
        #compute the windowed signal
        windowed_sig = copy.deepcopy(y_arr)
        windowed_sig[k*D:(N+(k*D))] =  hann_win*windowed_sig[k*D:(N+(k*D))]
        
        #vectorization on the n computation
        n = np.arange(N)
        n = n+1
        
        #compute the main factor ()-1 because array start at 0
        x_nkD = windowed_sig[((n) + (k)*D) -1]
        
        imag_list = np.ndarray(len(n), dtype=np.complex128)
        
        imag_list.imag = -omega[i]*n
        
        exp_factor = np.exp( imag_list )
        
        total =  hann_win * x_nkD * exp_factor
        
        list_for_given_k = abs(total)**2
         
    S_of_omega = np.nanmedian(list_for_given_k)
        
    S_welch += [S_of_omega]
    

"""
for i in range(len(omega)):
    print("i = {}/{}".format(i,len(omega)))
    for k in range(K):
        #print("k = {}/{}".format(k,K))
        list_for_given_k = np.array([])
        
        #winwod on the part of the signal to treat at this given k
        #goes from n=0 to n=N
        #compute the windowed signal
        windowed_sig = copy.deepcopy(y_arr)
        windowed_sig[k*D:(N+(k*D))] =  hann_win*windowed_sig[k*D:(N+(k*D))]
        
        #vectorization on the n computation
        n = np.arange(N)
        n = n+1
        
        #compute the main factor ()-1 because array start at 0
        x_nkD = windowed_sig[((n) + (k)*D) -1]
        
        imag_list = np.ndarray(len(n), dtype=np.complex128)
        
        imag_list.imag = -omega[i]*n
        
        exp_factor = np.exp( imag_list )
        
        total =  hann_win * x_nkD * exp_factor
        
        list_for_given_k = abs(total)**2
         
    S_of_omega = np.nanmedian(list_for_given_k)
        
    S_welch += [S_of_omega]

"""

#plot the PSD
plt.figure(3)
plt.plot(omega, S_welch)








