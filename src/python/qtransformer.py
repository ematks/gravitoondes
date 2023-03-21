from tiler import spectrogram
import numpy as np
import math

def V_coeff(self, x_fft):
    """
    Function that calculates V

    Parameters
    ----------
    m__time_coord: (int)
        tile coordinate in the tile time axis
    l__phi_coord: (int)
        tile coordinate in the frequency axis
    x_fft: (array)
        whitened fourier transformed data
    spectro: (spectrogram)
        the spectrogram we are evaluating the q-transform coefficient in

    Returns
    -------
    V: (list)
        list of v coefficent for all frequencies row
    """

    N = len(x_fft)

    V = []
    for l__phi_coord in range(len(spectro.freq)):
        w_l = spectro.W[l__phi_coord]
        M_l = len(w_l)
        N_tau = spectro.N_t[l__phi_coord]
        p_l = spectro.freq[l__phi_coord] * N / spectro.fs  # N/fs = T
        v_l = []
        for k in range(N_tau):
            if k < (M_l+1)/2:
                v = x_fft[k + p_l] * w_l[k] * np.exp(2 * 1j * np.pi  * k / N_tau)
            elif (M_l + 1)/2 <= k < N_tau - (M_l - 1)/2:
                v = 0
            elif N_tau - (M_l - 1)/2 <= k:
                v = -x_fft[k + N - N_tau + p_l] * w_l[k +N -N_tau] * np.exp(2 * 1j * np.pi  * k / N_tau)

            v_l += N_tau / N *v
        V += [v_l]
    self.V = V
    return