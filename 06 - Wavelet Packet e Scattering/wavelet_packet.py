import numpy as np
import matplotlib.pyplot as plt
from pywt import WaveletPacket

# sinal
t = np.linspace(0,1,2048)
sig = np.sin(40*np.pi*t) + 0.5*np.sin(140*np.pi*t)*(t>0.5)
sig += 0.3*np.random.randn(len(t))

# Wavelet Packet
wp = WaveletPacket(data=sig, wavelet='db4', mode='symmetric', maxlevel=4)
nodes = wp.get_level(4, order='freq')

plt.figure(figsize=(12,6))
for i, n in enumerate(nodes[:8]):
    plt.subplot(4,2,i+1)
    plt.plot(n.data)
    plt.title(f"Nó: {n.path}")
plt.tight_layout()
plt.show()

# --------- SCATTERING TRANSFORM (Kymatio) ----------
try:
    from kymatio.numpy import Scattering1D

    scattering = Scattering1D(J=6, shape=sig.shape[0])
    Sx = scattering(sig)

    print("Scattering shape:", Sx.shape)
except:
    print("Kymatio não instalado. Instale com: pip install kymatio")
