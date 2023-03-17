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
        npy_files_h.append(path+file)
    elif file.endswith('.npy') and file.startswith('l1'):
        npy_files_l.append(path+file)


#this should be a function, will be soon hopefully
def make_global_psd(files, fs= 1024):
    """
    Parameters
    ----------
    file: (list)
        list of strings that should refer to the path of files fromw which the global psd will eb computed from
    fs: (int)
         sampling frequency of files data, default = 1024

    Returns
    -------
    global_freq: (ndarray)
        frequencies realted to the psds
    global_psd: (ndarray)
        mean psd computed from list of files
    """
    psd_sum=[0 for i in range(fs+1)] #initiate an array in which sum the files psds

    for file in files:
        data = np.load(file)
        global_freq, psd = lib_GW.make_psd(data[1], fs)
        psd_sum += psd

    global_psd = psd_sum/len(files)
    return global_freq, global_psd

global_freq, global_psd_h = make_global_psd(npy_files_h)
o, global_psd_l = make_global_psd(npy_files_l)