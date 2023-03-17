import spectrum2
import os

path = '../../data/GW150914'
files = os.listdir(path)
for file in files:
    if 'root' in file:
        files.remove(file)
fs = 1024

psds=[]
for file in files:
    freq, psd = spectrum2.psd2(file[1], 1/fs)

    psds = np.append(psd)

#penser  normaliser