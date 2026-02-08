import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ==================================================
# 1. DEFINIÇÃO DO SINAL NÃO ESTACIONÁRIO
# ==================================================
# Frequência de amostragem (Hz)
fs = 1024

# Vetor de tempo (1 segundo)
t = np.linspace(0, 1, fs, endpoint=False)

# Sinal não estacionário:
# 50 Hz na primeira metade
# 120 Hz na segunda metade
sig = np.sin(2 * np.pi * 50 * t) * (t < 0.5) + \
      np.sin(2 * np.pi * 120 * t) * (t >= 0.5)

# ==================================================
# 2. WAVELET DE MORLET (FORMA NO TEMPO)
# ==================================================
# Vetor de tempo local para visualização da wavelet
tw = np.linspace(-1, 1, fs)

# Parâmetro da Morlet (compromisso tempo-frequência)
w = 6

# Wavelet de Morlet no domínio do tempo
morlet_wavelet = signal.morlet2(M=len(tw), s=1, w=w)

# ==================================================
# 3. PARÂMETROS DA CWT
# ==================================================
# Escalas analisadas
# Escala pequena  -> altas frequências
# Escala grande   -> baixas frequências
scales = np.arange(1, 128)

# Cálculo da Transformada Wavelet Contínua
# Resultado: matriz [escala x tempo]
cwt_coeffs = signal.cwt(sig, signal.morlet2, scales, w=w)

# ==================================================
# 4. VISUALIZAÇÃO DOS RESULTADOS
# ==================================================
plt.figure(figsize=(13, 10))

# --------------------------------------------------
# FIGURA 1 — SINAL NO DOMÍNIO DO TEMPO
# --------------------------------------------------
plt.subplot(3, 1, 1)
plt.plot(t, sig, color='black')
plt.axvline(0.5, color='red', linestyle='--',
            label='Mudança espectral (50 Hz → 120 Hz)')
plt.title("Sinal não estacionário no domínio do tempo")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# --------------------------------------------------
# FIGURA 2 — WAVELET DE MORLET NO TEMPO
# --------------------------------------------------
plt.subplot(3, 1, 2)
plt.plot(tw, np.real(morlet_wavelet), label='Parte real')
plt.plot(tw, np.imag(morlet_wavelet), linestyle='--', label='Parte imaginária')
plt.title("Wavelet de Morlet no domínio do tempo")
plt.xlabel("Tempo (normalizado)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# --------------------------------------------------
# FIGURA 3 — SCALOGRAMA (CWT)
# --------------------------------------------------
plt.subplot(3, 1, 3)
plt.imshow(
    np.abs(cwt_coeffs),
    extent=[0, 1, scales[-1], scales[0]],
    cmap='jet',
    aspect='auto'
)

plt.colorbar(label="Magnitude dos coeficientes wavelet")
plt.title("Scalograma – Transformada Wavelet Contínua (Morlet)")
plt.xlabel("Tempo (s)")
plt.ylabel("Escala")

plt.tight_layout()
plt.show()
