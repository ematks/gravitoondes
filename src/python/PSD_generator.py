import lib_GW
import os
import numpy as np

"""
Ce fichier permet  de générer une PSD globale à partir de l'ensemble de données présent dans le dossier GW150914

Elle est stockée dans la variable Global_PSD, qui pourra être importée dans d'autres fichiers; global_freq contient la bande de fréquence de la psd
"""

path = '../../data/GW150914/'

files = os.listdir(path)
npy_files_h = []
npy_files_l = []
for file in files:
    if file.endswith('.npy') and file.startswith('h1'):
        npy_files_h.append(file)
    elif file.endswith('.npy') and file.startswith('h1'):
        npy_files_l.append(file)


#this should be a function, will be soon hopefully
fs = 1024
psd_sum=[0 for i in range(fs+1)]

for file in npy_files_h:
    data = np.load(path+file)
    global_freq, psd = spectrum2.psd2(data[1], fs)
    psd_sum += psd

global_PSD_h = psd_sum/len(npy_files_h)

#faut il melanger les deceteurs, probalbement pas