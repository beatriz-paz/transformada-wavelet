# Análise Wavelet Discreta (DWT)

## Sumário

- [Introdução](#introdução)
- [Implementar DWT](#implementar-DWT)
- [Reconstrução (IDWT)](#reconstrução-(IDWT))
- [Entendendo os Coeficientes](#entendendo-os-coeficientes)
- [Diferentes Wavelets Mãe](#diferentes-wavelets-mãe)
- [Conclusão](#conclusão)

## Introdução

A DWT é uma técnica matemática que decompõe sinais em componentes de diferentes frequências (aproximação e detalhes). Para obtermos a Transformada Wavelet Discreta (DWT), os parâmetros de translação e escalonamento são discretizados. Já a variável independente, o tempo, permanece contínua (FARIAS, 2008).

A DWT fornece um conjunto de coeficientes que correspondem a pontos bidimensionais do deslocamento do sinal analisado. Essa grade é indexada por dois números inteiros: m, relacionado ao escalonamento, e n, relacionado à translação.

Vale lembrar que, neste contexto, escalonamento significa a compressão e a dilatação do sinal, enquanto a translação determina a localização da wavelet no tempo.

O código dwt_basico.py apresenta um experimento aplicado da análise wavelet discreta. O sinal analisado é composto pela soma de duas componentes senoidais de 50 Hz e 120 Hz, às quais foi adicionado ruído gaussiano branco. O sinal possui 1024 amostras em um intervalo de 1 segundo, caracterizando um sinal discreto no tempo. A presença de ruído simula condições reais de aquisição de sinais.

## Implementar DWT

### Decomposição Wavelet

Para a análise, utilizou-se a wavelet Daubechies de ordem 4 (db4), escolhida por sua excelente capacidade de representar sinais não estacionários e sua compactação no domínio do tempo. A decomposição foi executada até o nível 4, gerando dois tipos de coeficientes:

- Coeficientes de Aproximação (cA): Representam as componentes de baixa frequência e a estrutura global (a "tendência") do sinal.

- Coeficientes de Detalhe (D1 a D4): Capturam variações em diferentes faixas de frequência:

    - D1: Associado às frequências mais altas e ao ruído.
    - D4: Associado a variações mais lentas e suaves.

Essa estrutura exemplifica o princípio da **análise multirresolução**, que permite observar o sinal simultaneamente em diferentes escalas e níveis de detalhamento.

## Reconstrução (IDWT)

Utilizando os coeficientes obtidos na decomposição, aplicou-se a Transformada Wavelet Inversa (IDWT) para realizar a reconstrução do sinal. Observa-se que o resultado é praticamente idêntico ao sinal original, o que confirma que a DWT é um método reversível e sem perdas, desde que todos os coeficientes sejam preservados durante o processo.

## Entendendo os Coeficientes

A visualização dos coeficientes de detalhe revela que:

-  ruído concentra-se prioritariamente nos níveis de menor escala (D1);

- As componentes senoidais distribuem-se pelos níveis intermediários e superiores (D2 a D4);

- A energia do sinal oscila conforme a escala, refletindo a contribuição de cada faixa de frequência ao longo do tempo.

Essa característica torna a DWT ideal para aplicações como a **remoção de ruído (denoising)**, a compressão de dados e a **análise tempo-frequência** de sinais não estacionários.

## Diferentes Wavelets Mãe

Ao analisar os gráficos gerados por diferentes wavelets-mãe, nota-se que, embora a reconstrução do sinal seja praticamente idêntica ao original em todos os casos, surgem diferenças sutis nos coeficientes de detalhe. Isso ocorre porque cada wavelet possui propriedades matemáticas distintas como suavidade, simetria e comprimento do filtro, que influenciam a distribuição da energia do sinal entre as escalas.

- **Haar:** Por ser descontínua e ter suporte curto, gera coeficientes com transições abruptas e picos concentrados. É altamente sensível a variações rápidas, mas descreve sinais suaves (como senoides) de forma "serrilhada".

- **Daubechies (db4):** Produz coeficientes mais suaves e organizados. Graças aos seus momentos nulos, representa melhor sinais contínuos, distribuindo a energia de forma equilibrada sem introduzir oscilações artificiais.

- **Symlet (sym4):** Apresenta desempenho similar à Daubechies, mas com maior simetria. Isso reduz distorções de fase, resultando em coeficientes de detalhe mais regulares, especialmente em níveis intermediários.

- **Coiflet (coif3):** Gera coeficientes ainda mais suaves e bem distribuídos, especialmente em baixas frequências. Seus momentos nulos — presentes tanto na wavelet quanto na função de escala — favorecem uma representação fiel da estrutura global do sinal.

Em suma, embora a reconstrução final seja perfeita em todos os modelos, a **escolha da wavelet-mãe altera a forma como o sinal é "enxergado"**. Essa sensibilidade é crucial em tarefas como denoising, compressão e extração de características, onde a morfologia da wavelet impacta diretamente o desempenho.

## Conclusão

Os resultados demonstram que a Transformada Wavelet Discreta (DWT) permite uma representação eficiente do sinal em múltiplas escalas, preservando simultaneamente as informações temporais e espectrais. Além disso, a reconstrução fiel do sinal evidencia a robustez da técnica, reforçando sua aplicabilidade em problemas práticos de processamento digital de sinais.