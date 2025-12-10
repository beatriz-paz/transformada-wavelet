import numpy as np
import matplotlib.pyplot as plt
import pywt

# --- VISUALIZAR WAVELETS DISCRETAS ---
wavelets = ["haar", "db2", "db4", "sym4", "coif1"]

plt.figure(figsize=(10, 8))
for i, w in enumerate(wavelets):
    wavelet = pywt.Wavelet(w)
    phi, psi, x = wavelet.wavefun(level=5)  # função escala e wavelet
    plt.subplot(len(wavelets), 1, i+1)
    plt.plot(x, psi)
    plt.title(f"Wavelet {w}")
plt.tight_layout()
plt.show()

# --- COMPARAÇÃO TEMPO-FREQUÊNCIA ---
import scipy.signal as sg

t = np.linspace(0,1,1024)
s = np.sin(2*np.pi*50*t) * (t > 0.5)  # sinal muda ao longo do tempo

# STFT (Fourier local)
f, tt, Zxx = sg.stft(s, fs=1024)

# CWT (usando Morlet)
widths = np.arange(1, 128)
cwt_mat = sg.cwt(s, sg.morlet2, widths, w=5)

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.imshow(np.abs(Zxx), aspect='auto', origin='lower')
plt.title("STFT (Janela Fixa)")

plt.subplot(1,2,2)
plt.imshow(np.abs(cwt_mat), aspect='auto', origin='lower')
plt.title("CWT (Wavelet Morlet)")

plt.tight_layout()
plt.show()
