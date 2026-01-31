import numpy as np
import matplotlib.pyplot as plt
import pywt

# -----------------------------
# Criação do sinal
# -----------------------------
t = np.linspace(0, 1, 1024)
sig = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)
sig += 0.3*np.random.randn(len(t))

# -----------------------------
# Parâmetros
# -----------------------------
wavelets = ["db4", "sym4", "coif3", "haar"]
level = 4

# -----------------------------
# Loop por wavelet
# -----------------------------
for wavelet in wavelets:

    # Decomposição
    coeffs = pywt.wavedec(sig, wavelet, level=level)
    rec = pywt.waverec(coeffs, wavelet)
    rec = rec[:len(sig)]

    details = coeffs[1:]

    # -------------------------
    # Figura da wavelet atual
    # -------------------------
    plt.figure(figsize=(12, 7))
    plt.suptitle(f"Análise Wavelet DWT – {wavelet}", fontsize=14)

    # Sinal original
    ax1 = plt.subplot(3, 1, 1)
    ax1.plot(sig)
    ax1.set_title("Sinal original")
    ax1.set_ylabel("Amplitude")

    # Reconstrução
    ax2 = plt.subplot(3, 1, 2)
    ax2.plot(rec)
    ax2.set_title("Reconstrução (IDWT)")
    ax2.set_ylabel("Amplitude")

    # Detalhes
    ax3 = plt.subplot(3, 1, 3)
    for i, d in enumerate(details):
        ax3.plot(d, label=f"D{level-i}")
    ax3.set_title("Coeficientes de detalhe")
    ax3.set_xlabel("Amostras")
    ax3.set_ylabel("Amplitude")
    ax3.legend(fontsize=8)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
