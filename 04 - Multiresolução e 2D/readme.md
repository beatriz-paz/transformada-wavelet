# DWT em imagens (2D)

## Imagem e normalização

O código do programa __dwt_img.py__ começa carregando uma imagem em tons de cinza e convertendo seus valores para o intervalo [0,1]. Essa conversão é importante porque a transformada wavelet trabalha com operações matemáticas contínuas. Manter os pixels em ponto flutuante evita erros numéricos e garante que a decomposição e a reconstrução funcionem corretamente.

## Adição de ruído

Antes de aplicar a wavelet, é adicionado ruído gaussiano à imagem. Esse passo é essencial para entender o real efeito das wavelets. Em imagens limpas, a aplicação da transformada e a reconstrução produzem praticamente a mesma imagem, independentemente da wavelet usada. Com o ruído, surgem componentes de alta frequência que permitem observar como cada wavelet se comporta ao separar informação útil de interferência.

## Decomposição wavelet 2D

A transformada wavelet discreta 2D divide a imagem em diferentes escalas. Em cada nível de decomposição, a imagem é separada em uma parte de **baixa frequência, chamada aproximação**, e três partes de **alta frequência, chamadas detalhes horizontais**, verticais e diagonais. A aproximação representa a estrutura global da imagem, enquanto os detalhes concentram bordas, texturas e ruído.

Essa análise em múltiplas resoluções é o grande diferencial da wavelet em relação à transformada de Fourier, pois **permite localizar frequências no espaço da imagem**.

## Reconstrução da imagem

Após a decomposição, é reconstruído a imagem sem modificar os coeficientes. Isso serve para mostrar que wavelets ortogonais possuem a propriedade de reconstrução perfeita. Ou seja, decompor e reconstruir não altera a imagem original, apenas a representa de outra forma no domínio wavelet.

## Denoising com thresholding

A remoção de ruído é feita diretamente nos coeficientes wavelet. O princípio é simples: 

- **coeficientes de pequena magnitude geralmente correspondem a ruído**, enquanto **coeficientes maiores representam bordas e estruturas reais da imagem**. O thresholding soft reduz suavemente os coeficientes pequenos e preserva os grandes, evitando distorções abruptas.

- Os coeficientes de aproximação não são filtrados porque concentram a maior parte da energia da imagem. Alterá-los causaria perda de informação visual importante.

## Influência da wavelet escolhida

Cada wavelet representa bordas e detalhes de maneira diferente. 
- A **Haar** é simples e tende a gerar efeitos em blocos;
- As **Daubechies** equilibram suavização e preservação de bordas;
- As **Symlets** reduzem distorções e produzem transições mais suaves;
- As **Coiflets** preservam melhor detalhes finos. 

Essas diferenças aparecem com mais clareza quando há ruído na imagem e quando o threshold é suficientemente forte.

OBS.: falando do threshold, uma analogia para compreensão de sua aplicação nesse contesto seria como imaginar o threshold como uma peneira, sendo:
- Buracos grandes  → tudo passa (threshold fraco)
- Buracos médios   → só o que importa passa (threshold bom)
- Buracos pequenos → quase nada passa (threshold forte demais)

## Menu interativo e comparação prática

O menu interativo que aparece ao executar o programa permite testar várias wavelets mantendo o mesmo cenário de ruído e filtragem. Isso ajuda a entender que a wavelet não muda a imagem por si só, mas muda a forma como a informação é distribuída nos coeficientes. Como consequência, o processo de denoising apresenta resultados diferentes para cada base wavelet.

## Ideia central das wavelets

Wavelets permitem analisar imagens e sinais ao mesmo tempo no espaço e na frequência, em múltiplas escalas. Elas são especialmente eficazes para tarefas como remoção de ruído, compressão e extração de características. O programa __dwt_img.py__ mostra, de forma prática, como uma imagem é decomposta, tratada e reconstruída, consolidando os conceitos fundamentais.