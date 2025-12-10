import numpy as np
import matplotlib.pyplot as plt
import pywt

# sinal sintético
t = np.linspace(0, 1, 1024)
sig = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)
sig += 0.3*np.random.randn(len(t))

wavelet = "db4"
level = 4

# decompor
coeffs = pywt.wavedec(sig, wavelet, level=level)
cA, details = coeffs[0], coeffs[1:]

# reconstruir
rec = pywt.waverec(coeffs, wavelet)

# plot
plt.figure(figsize=(10,8))
plt.subplot(3,1,1)
plt.plot(sig); plt.title("Sinal original")

plt.subplot(3,1,2)
plt.plot(rec); plt.title("Reconstrução (IDWT)")

plt.subplot(3,1,3)
for i, d in enumerate(details):
    plt.plot(d, label=f"Detalhe D{level-i}")
plt.legend()
plt.title("Coeficientes de detalhe")
plt.tight_layout()
plt.show()
