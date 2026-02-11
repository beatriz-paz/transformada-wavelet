import numpy as np
import matplotlib.pyplot as plt
from pywt import WaveletPacket

# -----------------------------
# GERAÇÃO DO SINAL
# -----------------------------

# Vetor de tempo de 0 a 1 segundo com 2048 amostras
# Quanto mais pontos, melhor a resolução temporal
t = np.linspace(0, 1, 2048)

# Sinal composto por:
# - uma senoide de baixa frequência (20 Hz → 40π rad/s)
# - uma senoide de alta frequência (70 Hz → 140π rad/s)
#   que só aparece após t > 0.5 (mudança espectral no tempo)
sig = np.sin(40 * np.pi * t) + 0.5 * np.sin(140 * np.pi * t) * (t > 0.5)

# Adiciona ruído branco gaussiano ao sinal
# Isso simula um cenário mais realista de medição
sig += 0.3 * np.random.randn(len(t))


# -----------------------------
# WAVELET PACKET TRANSFORM (WPT)
# -----------------------------

# Cria o objeto WaveletPacket
# data      → sinal de entrada
# wavelet   → wavelet mãe (Daubechies de ordem 4)
# mode      → tratamento de borda (symmetric evita distorções)
# maxlevel  → profundidade máxima da decomposição
wp = WaveletPacket(
    data=sig,
    wavelet='db4',
    mode='symmetric',
    maxlevel=4
)

# Obtém todos os nós do nível 4
# order='freq' organiza os nós por ordem crescente de frequência
nodes = wp.get_level(4, order='freq')


# -----------------------------
# VISUALIZAÇÃO DOS NÓS
# -----------------------------

plt.figure(figsize=(12, 6))

# Percorre os 8 primeiros nós (sub-bandas)
# Cada nó representa uma faixa de frequência diferente
for i, n in enumerate(nodes[:8]):
    plt.subplot(4, 2, i + 1)
    
    # Dados do nó (coeficientes da wavelet packet)
    plt.plot(n.data)
    
    # Caminho do nó na árvore (ex: 'aaaa', 'aaad', etc.)
    plt.title(f"Nó: {n.path}")

plt.tight_layout()
plt.show()


# -----------------------------
# SCATTERING TRANSFORM (KYMATIO)
# -----------------------------

try:
    # Importa a implementação da Scattering Transform 1D
    from kymatio.numpy import Scattering1D

    # Cria o objeto Scattering
    # J     → número de escalas (define invariância temporal)
    # shape → tamanho do sinal de entrada
    scattering = Scattering1D(
        J=6,
        shape=sig.shape[0]
    )

    # Aplica a Scattering Transform ao sinal
    # O resultado são coeficientes estáveis e invariantes a pequenas translações
    Sx = scattering(sig)

    # Exibe a dimensão do vetor de características gerado
    print("Scattering shape:", Sx.shape)

except:
    # Caso a biblioteca não esteja instalada
    print("Kymatio não instalado. Instale com: pip install kymatio")
