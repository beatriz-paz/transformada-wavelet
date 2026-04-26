import numpy as np
import matplotlib.pyplot as plt
import pywt

# ==================================================
# 1. SINAL NÃO ESTACIONÁRIO
# ==================================================
fs = 1024
t = np.linspace(0, 1, fs, endpoint=False)

sig = np.sin(2*np.pi*50*t)*(t < 0.5) + \
      np.sin(2*np.pi*120*t)*(t >= 0.5)

# ==================================================
# 2. FFT (Transformada de Fourier)
# ==================================================
fft_vals = np.fft.fft(sig)
freqs = np.fft.fftfreq(len(sig), 1/fs)

mask = freqs >= 0
freqs = freqs[mask]
fft_vals = np.abs(fft_vals[mask])

# ==================================================
# 3. CWT (Wavelet com frequência controlada)
# ==================================================
# definir faixa de frequências de interesse
frequencias = np.linspace(1, 200, 150)

# converter frequência -> escala
scales = pywt.central_frequency('morl') * fs / frequencias

# calcular CWT
coeffs, _ = pywt.cwt(sig, scales, 'morl', sampling_period=1/fs)

# ==================================================
# 4. PLOT
# ==================================================
plt.figure(figsize=(14, 10))

# -------------------------
# Sinal
# -------------------------
plt.subplot(3, 1, 1)
plt.plot(t, sig)
plt.axvline(0.5, linestyle='--', label='Mudança de frequência')
plt.title("Sinal não estacionário")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# -------------------------
# FFT
# -------------------------
plt.subplot(3, 1, 2)
plt.plot(freqs, fft_vals)

plt.axvline(50, linestyle='--', label='50 Hz')
plt.axvline(120, linestyle='--', label='120 Hz')

plt.xlim(0, 200)
plt.title("Transformada de Fourier (FFT)")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)

# -------------------------
# CWT (Wavelet)
# -------------------------
plt.subplot(3, 1, 3)

plt.imshow(
    np.abs(coeffs),
    extent=[0, 1, frequencias[-1], frequencias[0]],
    aspect='auto',
    cmap='jet'
)

plt.colorbar(label="Magnitude")
plt.title("Transformada Wavelet (CWT)")
plt.xlabel("Tempo (s)")
plt.ylabel("Frequência (Hz)")

plt.tight_layout()
plt.show()

# ==================================================
# 4. DWT (Transformada Wavelet Discreta)
# ==================================================
coeffs = pywt.wavedec(sig, 'db4', level=4)

# ==================================================
# 5. PLOT DWT
# ==================================================
plt.figure(figsize=(12, 6))

for i, c in enumerate(coeffs):
    plt.subplot(len(coeffs), 1, i+1)
    plt.plot(c)
    
    if i == 0:
        plt.title("Aproximação (A4)")
    else:
        plt.title(f"Detalhe (D{len(coeffs)-i})")
    
    plt.ylabel("Amplitude")
    plt.grid(True)

plt.xlabel("Amostras")
plt.tight_layout()
plt.show()