import numpy as np
import matplotlib.pyplot as plt
import pywt
from skimage import data, img_as_float

# -------------------------------------------------
# Carregamento da imagem
# -------------------------------------------------

# Carrega imagem de teste (grayscale) e converte para float [0,1]
img = img_as_float(data.camera())

# -------------------------------------------------
# Adição de ruído (ESSENCIAL para ver diferenças)
# -------------------------------------------------

# Define intensidade do ruído (quanto maior, mais visível o efeito)
noise_std = 0.1

# Gera ruído gaussiano com média 0 e desvio padrão definido
noise = noise_std * np.random.randn(*img.shape)

# Soma o ruído à imagem original
img_noisy = img + noise

# Garante que os valores permaneçam no intervalo válido [0,1]
img_noisy = np.clip(img_noisy, 0, 1)

# -------------------------------------------------
# Lista de wavelets para teste
# -------------------------------------------------

wavelets = [
    "haar",
    "db2", "db4",
    "sym2", "sym4",
    "coif1", "coif3"
]

# -------------------------------------------------
# Menu iterativo
# -------------------------------------------------

while True:
    print("\n=== MENU DE WAVELETS ===")
    for i, w in enumerate(wavelets):
        print(f"{i} - {w}")
    print("x - sair")

    escolha = input("\nEscolha a wavelet: ")

    # Encerra o programa
    if escolha.lower() == "x":
        print("Encerrando...")
        break

    # Validação da entrada
    if not escolha.isdigit() or int(escolha) >= len(wavelets):
        print("Opção inválida. Tente novamente.")
        continue

    wavelet = wavelets[int(escolha)]
    print(f"\nWavelet selecionada: {wavelet}")

    # -------------------------------------------------
    # Decomposição Wavelet 2D
    # -------------------------------------------------

    # Aplica a Transformada Wavelet Discreta 2D
    # level=2 -> duas escalas (mais detalhe + mais suavização)
    # A decomposição separa:
    # - aproximação (baixa frequência)
    # - detalhes horizontais, verticais e diagonais
    coeffs2 = pywt.wavedec2(img_noisy, wavelet=wavelet, level=2)

    # Reconstrução SEM alterar coeficientes
    # Serve como referência (imagem ruidosa reconstruída)
    reconstructed = pywt.waverec2(coeffs2, wavelet)

    # -------------------------------------------------
    # Denoising por thresholding wavelet
    # -------------------------------------------------

    coeffs_f = []  # armazenará os coeficientes filtrados

    for i, c in enumerate(coeffs2):

        # i == 0 → coeficientes de aproximação (baixa frequência)
        # Mantidos intactos para preservar a estrutura global da imagem
        if i == 0:
            coeffs_f.append(c)

        # Demais níveis → coeficientes de detalhe (alta frequência)
        else:
            cH, cV, cD = c

            # Aplica thresholding soft:
            # - coeficientes pequenos (ruído) são reduzidos
            # - coeficientes grandes (bordas) são preservados
            coeffs_f.append((
                pywt.threshold(cH, 0.15, mode='soft'),
                pywt.threshold(cV, 0.15, mode='soft'),
                pywt.threshold(cD, 0.15, mode='soft')
            ))

    # Reconstrói a imagem a partir dos coeficientes filtrados
    img_denoised = pywt.waverec2(coeffs_f, wavelet)

    # -------------------------------------------------
    # Visualização dos resultados
    # -------------------------------------------------

    plt.figure(figsize=(12,4))

    # Imagem original (sem ruído)
    plt.subplot(1,4,1)
    plt.imshow(img, cmap="gray")
    plt.title("Original")
    plt.axis("off")

    # Imagem com ruído
    plt.subplot(1,4,2)
    plt.imshow(img_noisy, cmap="gray")
    plt.title("Com ruído")
    plt.axis("off")

    # Reconstrução wavelet (sem denoising)
    plt.subplot(1,4,3)
    plt.imshow(reconstructed, cmap="gray")
    plt.title(f"Reconstrução ({wavelet})")
    plt.axis("off")

    # Imagem após denoising wavelet
    plt.subplot(1,4,4)
    plt.imshow(img_denoised, cmap="gray")
    plt.title(f"Denoising ({wavelet})")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
