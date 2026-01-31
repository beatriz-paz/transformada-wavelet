import numpy as np
import matplotlib.pyplot as plt
import pywt

# --- VISUALIZAR WAVELETS (ψ(t)) DISCRETAS NO TEMPO ---

# Essas wavelets são muito usadas em compressão, filtragem e análise multirresolução
wavelets = ["haar", "db2", "db4", "sym4", "coif1"]

plt.figure(figsize=(10, 8)) # cria uma figura de 10pol por 8pol de altura.
for i, w in enumerate(wavelets):
    wavelet = pywt.Wavelet(w) # cria um objeto Wavalet
    phi, psi, x = wavelet.wavefun(level=5)  # função escala e wavelet
    '''
        phi   → função escala φ(t)
        psi   → função wavelet ψ(t)
        x     → eixo de tempo/amostra
        level → indica o nível de resolução (quanto maior, mais suave e detalhada a função)

        Conceitualmente:
            φ(t) → representa aproximação (baixa frequência)
            ψ(t) → representa detalhes (alta frequência)
    '''
    # Divide a figura em: len(wavelets) linhas e 1 coluna
    plt.subplot(len(wavelets), 1, i+1)
    plt.plot(x, psi)
    plt.title(f"Wavelet {w}")
plt.tight_layout()
plt.show()

# --- COMPARAÇÃO TEMPO-FREQUÊNCIA, JANELA FIXA (STFT) COM JANELA ADAPTATIVA (CWT) ---

import scipy.signal as sg

# Cria um vetor de tempo: de 0 a 1 segundo com 1024 amostras
t = np.linspace(0,1,1024)
s = np.sin(2*np.pi*50*t) * (t > 0.5)  # sinal muda ao longo do tempo

# STFT (Fourier local)
f, tt, Zxx = sg.stft(s, fs=1024)

# CWT (usando Morlet)
widths = np.arange(1, 128)
'''
widths define as escalas da wavelet:
    Escala pequena → alta frequência
    Escala grande → baixa frequência
'''

cwt_mat = sg.cwt(s, sg.morlet2, widths, w=5)
'''
Parâmetros:
    s → sinal
    sg.morlet2 → wavelet de Morlet
    widths → escalas
    w=5 → parâmetro da Morlet (nº de oscilações)

Retorna uma matriz:
    linhas → escalas
    colunas → tempo
'''

plt.figure(figsize=(12,6))

# --- STFT ---
ax1 = plt.subplot(1,2,1)
ax1.imshow(np.abs(Zxx), aspect='auto', origin='lower')
ax1.set_title("STFT (Janela Fixa)")
ax1.set_xlabel("Tempo")
ax1.set_ylabel("Frequência")
'''
    np.abs(Zxx) → magnitude (descarta fase)
    imshow → imagem tempo-frequência
    aspect='auto' → escala automática
    origin='lower' → frequências baixas embaixo
'''
# --- CWT ---
ax2 = plt.subplot(1,2,2)
ax2.imshow(np.abs(cwt_mat), aspect='auto', origin='lower')
ax2.set_title("CWT (Wavelet Morlet)")
ax2.set_xlabel("Tempo")
ax2.set_ylabel("Frequência")

plt.tight_layout()
plt.show()