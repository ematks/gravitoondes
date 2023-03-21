from tiler import spectrogram
import numpy as np

def qtransform_coeff(m__time_coord, l__phi_coord, x_fft, spectro: spectrogram):
    """
    Function that calculates q-transform coefficients for give m__time_coord, l__phi_coord coordinates

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
    X: (float)
        q-transform coefficient
    """

    N = len(x)
    N_tau = spectro.N_t[l__phi_coord]
    p_l = spectro.freq[l__phi_coord] * N/spectro.fs # N/fs = T

    w_l = spectro.W
    M_l = len(w_l)

    X = 0
    for k in range(N_tau):
        if k < (M_l+1)/2:
            v_l = x_fft[k + p_l] * w_l[k] * np.exp(2 * j * np.pi  * k / N_tau)
        elif (M_l + 1)/2 <= k < N_tau - (M_l - 1)/2:
            v_l = 0
        elif N_tau - (M_l - 1)/2 <= k:
            v_l = -x_fft[k + N - N_tau + p_l] * w_l[k +N -N_tau] * np.exp(2 * j * np.pi  * k / N_tau)

        X += spectro.fs / N * v_l * np.exp(2 * j * np.pi * m__time_coord * k / N_tau)

    return X