import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pywt

# ==================================================
# 1. SINAL NÃO ESTACIONÁRIO
# ==================================================
fs = 1024
t = np.linspace(0, 1, fs, endpoint=False)

sig = np.sin(2*np.pi*50*t)*(t < 0.5) + \
      np.sin(2*np.pi*120*t)*(t >= 0.5)

# ==================================================
# 2. CWT (CONTÍNUA)
# ==================================================
scales = np.arange(1, 128)
w = 6

cwt_coeffs = signal.cwt(sig, signal.morlet2, scales, w=w)

# ==================================================
# 3. DWT (DISCRETA)
# ==================================================
wavelet = 'db4'
level = 4

coeffs = pywt.wavedec(sig, wavelet, level=level)

# ==================================================
# 4. VISUALIZAÇÃO
# ==================================================
plt.figure(figsize=(14, 10))

# -------------------------
# Figura 1 – Sinal
# -------------------------
plt.subplot(3, 1, 1)
plt.plot(t, sig, color='black')
plt.axvline(0.5, color='red', linestyle='--')
plt.title("Sinal não estacionário no tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.grid(True)

# -------------------------
# Figura 2 – CWT
# -------------------------
plt.subplot(3, 1, 2)
plt.imshow(
    np.abs(cwt_coeffs),
    extent=[0, 1, scales[-1], scales[0]],
    cmap='jet',
    aspect='auto'
)
plt.colorbar(label="|Coeficientes Wavelet|")
plt.title("CWT – Scalograma (análise contínua tempo–escala)")
plt.xlabel("Tempo (s)")
plt.ylabel("Escala")

# -------------------------
# Figura 3 – DWT
# -------------------------
plt.subplot(3, 1, 3)

offset = 0
for i, c in enumerate(coeffs):
    plt.plot(c + offset, label=f"Nível {i}")
    offset += np.max(np.abs(c)) * 1.2

plt.title("DWT – Coeficientes por nível (análise multiresolução)")
plt.xlabel("Amostras")
plt.ylabel("Amplitude (offset visual)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
