import lib_GW
import os
import numpy as np

"""
Ce fichier permet  de générer une PSD globale à partir de l'ensemble de données présent dans le dossier GW150914

Elle est stockée dans la variable Global_PSD, qui pourra être importée dans d'autres fichiers; global_freq contient la bande de fréquence de la psd
"""

#constitute the Hanford and Livingston lists of numpy files, npy_files_h and npy_files_l
path = '../../data/GW150914/'
files = os.listdir(path)
npy_files_h = []
npy_files_l = []
for file in files:
    if file.endswith('.npy') and file.startswith('h1'):
        npy_files_h.append(file)
    elif file.endswith('.npy') and file.startswith('l1'):
        npy_files_l.append(file)


#this should be a function, will be soon hopefully
def make_global_psd(files, fs= 1024):
    psd_sum=[0 for i in range(fs+1)] #initiate an array in which sum the files psds

    for file in files:
        data = np.load(path+file)
        global_freq, psd = spectrum2.psd2(data[1], fs)
        psd_sum += psd

    global_PSD = psd_sum/len(files))
    return global_PSD

global_psd_h = make_global_psd(npy_files_h)
global_psd_l = make_global_psd(npy_files_l)