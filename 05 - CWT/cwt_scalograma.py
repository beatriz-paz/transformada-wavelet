import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# sinal exemplo
fs = 1024
t = np.linspace(0,1,fs)
sig = np.sin(2*np.pi*50*t)*(t<0.5) + np.sin(2*np.pi*120*t)*(t>=0.5)

widths = np.arange(1, 128)

# CWT com Morlet
cwt_mat = signal.cwt(sig, signal.morlet2, widths, w=6)

plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(t, sig); plt.title("Sinal")

plt.subplot(2,1,2)
plt.imshow(np.abs(cwt_mat), extent=[0,1,1,128],
           cmap='jet', aspect='auto', origin='lower')
plt.title("Scalograma (CWT - Morlet)")
plt.ylabel("Escala")
plt.xlabel("Tempo")

plt.tight_layout()
plt.show()
