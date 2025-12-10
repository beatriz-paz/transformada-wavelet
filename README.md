# Transformada Wavelet

## Objetivo:

- Repositório dedicado para estudar aplicações em Python da transformada Wavalet.

## Plano de estudo:

- Nível 1 — Visual
Fundamentos: o que é wavelet, comparação com Fourier, impulso/resolução tempo-frequência. Visualizar wavelets (Haar, Daubechies, Morlet).

- Nível 2 — DWT básico (1D):
Implementar DWT, reconstrução (IDWT), entender coeficientes (approx / detalhe), níveis de decomposição.

- Nível 3 — Aplicações simples:
Compressão simples, detecção de descontinuidade, filtragem, thresholding para remoção de ruído.

- Nível 4 — Multiresolução & 2D:
DWT em imagens (2D), análise multiescala, denoising de imagem.

- Nível 5 — CWT / Scalogramas:
Continuous Wavelet Transform para análise de sinais não-estacionários (ex.: áudio, ECG).

- Nível 6 — Wavelet Packet, scattering
Wavelet packet decomposition, escolha ótima de bases; introdução ao scattering transform (mais avançado, pode envolver Kymatio).

- Nível 7 — Projeto final: classificação de sinais, compressão e reconstrução de imagens, detecção de falhas em sinais.

## Bibliotecas:

python
```
pip install numpy scipy matplotlib pywavelets scikit-image librosa
```