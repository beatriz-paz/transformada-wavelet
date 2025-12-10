import numpy as np
import matplotlib.pyplot as plt
import pywt

# --- sinal com ruído ---
t = np.linspace(0,1,1024)
sig = np.sin(40*np.pi*t)
sig[300:310] += 3          # descontinuidade artificial
sig += 0.5*np.random.randn(len(t))

wavelet = "db4"
coeffs = pywt.wavedec(sig, wavelet, level=4)

# --- threshold universal ---
sigma = np.median(np.abs(coeffs[-1]))/0.6745
uth = sigma * np.sqrt(2*np.log(len(sig)))

coeffs_f = [coeffs[0]] + [pywt.threshold(c, uth, mode='soft') for c in coeffs[1:]]
sig_denoised = pywt.waverec(coeffs_f, wavelet)

# --- compressão simples (zera coeficientes pequenos) ---
coeffs_c = [np.where(np.abs(c)>0.2, c, 0) for c in coeffs]
sig_compressed = pywt.waverec(coeffs_c, wavelet)

# plot
plt.figure(figsize=(10,8))
plt.subplot(3,1,1)
plt.plot(sig); plt.title("Sinal com ruído e descontinuidade")

plt.subplot(3,1,2)
plt.plot(sig_denoised); plt.title("Denoising (thresholding)")

plt.subplot(3,1,3)
plt.plot(sig_compressed); plt.title("Compressão (coeficientes pequenos zerados)")
plt.tight_layout()
plt.show()
