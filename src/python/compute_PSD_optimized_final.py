import numpy as np
import matplotlib.pyplot as plt
import ROOT
from scipy.signal import hann 
import copy
#magic ROOT commande
ROOT.ROOT.EnableImplicitMT()

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

#plot the signal
plt.figure(1)
plt.plot(x_buff,y_buff)
plt.title('signal')
plt.xlabel('gps time [s]')
plt.ylabel('amplitude')
plt.show()
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

#Plot the fft
plt.figure(2)
plt.plot(freq,np.log10(fft_m_real))
plt.xlabel("frequency [Hz]")
plt.ylabel("log spectrum magnitude")
plt.show()


###define the window used for the PSD estimation
#define the number of point for the window
n_window = 100

hann_win = hann(n_window)

#plot to check that the window looks good
plt.figure(3)
plt.plot(hann_win)
plt.title('Hann window')
plt.show()
#define the signal lenght
M = 500 * fs

#define the lenght of the segment
N = 2**(int( np.log(M)/np.log(2) ) -1)

#vectorization on the n computation
n = np.arange(N)

#define the number of segments
#take segment of 10s
#K = 50
K = int( (2*M) /N )-1

#define the shift 
D = int( (M-N)/(K-1) )

#define the pulsation range
omega = (fs/2) * np.linspace(0,1,N/2)

#define the window
hann_win = hann(N)   

#define the scale factor
scale_factor = (1/(N*fs))
#U = (1/N) * np.sum( abs(hann_win)**2 )
#scale_factor = 1/(N*K*U)

S_welch = []

### Median methode

list_for_all_k = np.zeros([K, int(len(n)/2)])

for k in range(K):
    #print("k = {}/{}".format(k,K))
    list_for_given_k = np.array([])
    
    #winwod on the part of the signal to treat at this given k
    #goes from n=0 to n=N
    #compute the windowed signal
    windowed_sig = copy.deepcopy(y_arr)
    windowed_sig[k*D:(N+(k*D))] =  hann_win*windowed_sig[k*D:(N+(k*D))]
    
    #have a look of the differents signal
    windowed_sig_temp = copy.deepcopy(windowed_sig)
    windowed_sig_temp[0:k*D] = 0
    windowed_sig_temp[(N+(k*D)):-1] = 0
    plt.figure(4)
    plt.plot(windowed_sig_temp)
    plt.title('different windowed signals')
    plt.show()
    
    #select only the windowed part of the signal
    windowed_sig = windowed_sig[k*D:(N+(k*D))]
      
    ##compute the main factor
    #using fft
    total = np.fft.fft(windowed_sig)
    
    total = total[0:int(N/2)]
    
    list_for_given_k = abs(total)**2
    
    list_for_all_k[k] += list_for_given_k

list_median = []

for i in range(len(list_for_all_k[0])):
    
    median_i = np.median(list_for_all_k[:,i])
  
    list_median += [median_i]


#S_of_omega = scale_factor * list_for_given_k
S = scale_factor * np.array(list_median)

S_welch += [S]


#plot the PSD
plt.figure(5)
plt.plot(omega, S_welch[0])
plt.xscale('log')
plt.yscale('log')
plt.xlabel("freq [Hz]")
plt.ylabel("amplitude")
plt.title('PSD')
plt.show()



### Mean methode
"""
S_welch2 = []
list_for_all_k = np.zeros(int(len(n)/2))

for k in range(K):
    #print("k = {}/{}".format(k,K))
    list_for_given_k = np.array([])
    
    #winwod on the part of the signal to treat at this given k
    #goes from n=0 to n=N
    #compute the windowed signal
    windowed_sig = copy.deepcopy(y_arr)
    windowed_sig[k*D:(N+(k*D))] =  hann_win*windowed_sig[k*D:(N+(k*D))]
    
    #have a look of the differents signal, uncomment the break following 
    #windowed_sig[0:k*D] = 0
    #windowed_sig[(N+(k*D)):-1] = 0
    #plt.plot(windowed_sig)
    
    windowed_sig = windowed_sig[k*D:(N+(k*D))]
      
    ##compute the main factor ()-1 because array start at 0
    #by hand
    '''
    x_nkD = windowed_sig[n]
    
    imag_list = np.ndarray(len(n), dtype=np.complex128)
    
    imag_list.imag = (-omega[w]* 2*np.pi *n) / N
    
    exp_factor = np.exp( imag_list )
    
    total =  x_nkD * exp_factor
    '''
    
    #using fft
    total = np.fft.fft(windowed_sig)
    
    total = total[0:int(N/2)]
    
    list_for_given_k = abs(total)**2
    
    list_for_all_k += list_for_given_k

#S_of_omega = scale_factor * list_for_given_k
S = scale_factor * list_for_all_k

#break

#S_of_omega = np.nanmedian(S)
S_of_omega = S/N


S_welch2 += [S_of_omega]


#plot the PSD
plt.figure(4)
plt.plot(omega, S_welch[0])
plt.xscale('log')
plt.yscale('log')
plt.xlabel("")
plt.ylabel("")
"""
