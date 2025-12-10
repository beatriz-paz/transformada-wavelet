import numpy as np
import matplotlib.pyplot as plt
import pywt
from skimage import data, img_as_float

img = img_as_float(data.camera())
wavelet = "db2"

coeffs2 = pywt.wavedec2(img, wavelet=wavelet, level=2)
reconstructed = pywt.waverec2(coeffs2, wavelet)

# Denoising simples
coeffs_f = []
for i, c in enumerate(coeffs2):
    if i == 0:
        coeffs_f.append(c)
    else:
        cH, cV, cD = c
        coeffs_f.append((
            pywt.threshold(cH, 0.05, mode='soft'),
            pywt.threshold(cV, 0.05, mode='soft'),
            pywt.threshold(cD, 0.05, mode='soft')
        ))
img_denoised = pywt.waverec2(coeffs_f, wavelet)

plt.figure(figsize=(10,4))
plt.subplot(1,3,1)
plt.imshow(img, cmap="gray"); plt.title("Original"); plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(reconstructed, cmap="gray"); plt.title("Reconstrução"); plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(img_denoised, cmap="gray"); plt.title("Denoising 2D"); plt.axis("off")

plt.tight_layout()
plt.show()
