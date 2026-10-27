# Relação entre os materiais de "Previsão de Demanda"

Levantamento detalhado dos arquivos nas 3 subpastas (`ARIMA/`, `Atividades/`, `novas/`) e dos dois notebooks soltos na raiz. Para cada exercício/notebook: subtema exato, arquivo(s) de input usado(s) e com quais outros materiais ele se relaciona.

---

## 1. Macro-temas presentes na pasta

| Macro-tema | Arquivos envolvidos |
|---|---|
| **1. Modelos AR / MA / ARMA / ARIMA** (núcleo de "previsão de demanda") | item 2 abaixo |
| **2. Decomposição de séries temporais** (tendência/sazonalidade) | `Decomposição Serie Temporal.ipynb` |
| **3. Estimação e testes de hipótese** (pré-requisito estatístico, não é série temporal) | `Estimacao_Testes_Hipotese.ipynb` |
| **4. Dados reais de atracação de navios** (aplicação prática, mistura fila + estatística descritiva) | `Atividades/Atv1.*` |
| **5. Teoria de filas (DES)** — fora do escopo de "previsão de demanda" | `ARIMA/Atividades_DES.ipynb` |

---

## 2. Macro-tema "AR / MA / ARMA / ARIMA" — segregado por subtópico

### 2.1 Subtópico: AR(p) e MA(q) isolados, ajuste por mínimos quadrados, MSE
- **`ARIMA/ARIMA - Parte 1.ipynb`**
  - Input: série embutida no próprio notebook (array `series`, 75 obs., sem arquivo externo).
  - Conteúdo: ajusta `AutoReg` (AR(2) e AR(3), API antiga/depreciada) e `ARIMA(0,0,1)` (MA(1)) sobre a mesma série; compara erro (MSE) entre AR(2), AR(3) e MA(1).
  - Sem seção teórica (markdown vazio) — é o rascunho de cálculo que origina a seção "1. Modelo Autorregressivo" + "2. Modelo de Média Móvel" do notebook `novas/PNV3421_Aula09_ARIMA.ipynb` (mesmos 75 valores de `series`, mesmos dois modelos AR(2)/AR(3)/MA(1)).
  - **Redundância:** conteúdo e dados idênticos aos itens "1" e "2" de `PNV3421_Aula09_ARIMA.ipynb`.

### 2.2 Subtópico: estacionariedade (teste de Dickey-Fuller) + ACF/PACF em 4 séries de exemplo
- **`ARIMA/ARIMA - Parte 2.ipynb`** — "Modelos Autorregressivos"
  - Input: 4 séries embutidas no notebook (`data1`..`data4`, sem arquivo externo).
  - Exemplo 1 (`data1`, 20 obs., tendência crescente 13,4→44,2): ADF, ACF/PACF.
  - Exemplo 2 (`data2`, ~30 obs., oscilante 2,6–8,3): ADF, ACF/PACF.
  - Exemplo 3 (`data3`, ~30 obs., 6,0–10,9): ADF, ACF/PACF.
  - Exemplo 4 (`data4`, ~140+ obs., preço tipo ação ~25,2–25,5): ADF; diferenciação de 1ª ordem (`df4_d1`); testa várias ordens `ARIMA(p,d,q)`; resíduos; ACF dos resíduos; separação treino/teste.
  - **Relação direta:** `data1`, `data2`, `data3`, `data4` e toda a sequência de análise (ADF → diferenciação → ACF/PACF → candidatos ARIMA → resíduos → treino/teste) são **exatamente os mesmos 4 exemplos** usados nas seções "4. ARMA e Série Estacionária" (`data1`), "7. Exemplo 2: determinar p" (`data2`), "7. Exemplo 3: determinar q" (`data3`) e "7. Exemplo 4: Box-Jenkins completo" (`data4`) do notebook `novas/PNV3421_Aula09_ARIMA.ipynb`.
  - **Redundância:** é o rascunho/versão de aula anterior da metodologia Box-Jenkins completa, hoje consolidada (com texto teórico e explicações) em `PNV3421_Aula09_ARIMA.ipynb`.

### 2.3 Subtópico: teoria consolidada — AR, MA, suavização exponencial, estacionariedade, ARIMA(p,d,q), ACF/PACF, Ljung-Box, Box-Jenkins, treino/teste (referência principal)
- **`novas/PNV3421_Aula09_ARIMA.ipynb`** — notebook de apoio à **Aula 09** (`novas/Aula 09.pdf`), usa a API atual do `statsmodels`. Estrutura interna (cada seção é um subtópico):
  1. Modelo AR(p) — mesmos dados/resultado de `ARIMA - Parte 1.ipynb`.
  2. Modelo MA(q) — mesmos dados/resultado de `ARIMA - Parte 1.ipynb`.
  3. Suavização exponencial vs. AR vs. MA (conteúdo exclusivo deste notebook, não presente nos rascunhos).
  4. ARMA e estacionariedade, teste ADF, detrending vs. differencing — usa `data1` de `ARIMA - Parte 2.ipynb`.
  5. ARIMA(p,d,q) e papel do "d" (teoria).
  6. Leitura de ACF/PACF (tabela-resumo AR×MA×ARMA).
  7. Três exemplos de identificação de ordem — `data2` (determinar p), `data3` (determinar q), `data4` (Box-Jenkins completo) — mesmos dados de `ARIMA - Parte 2.ipynb`.
  8. Resíduos e teste de Ljung-Box-Pierce.
  9. Divisão treino/teste, previsão h-passos vs. rolante (walk-forward).
  10. **Exercícios 1 e 2** propostos ao final (dados embutidos no próprio notebook: controle de qualidade / ações de empresa de tecnologia) — **ainda sem solução preenchida** (células marcadas "Sua solução").
  - **Este é o notebook de referência consolidada** do macro-tema AR/MA/ARIMA — os itens 2.1 e 2.2 acima são rascunhos anteriores do mesmo conteúdo.

### 2.4 Subtópico: exercícios resolvidos de ARIMA com dado bruto externo (estacionariedade + diferenciação)
- **`ARIMA/Exercício1.txt`** → **`ARIMA/ARIMA_Ex1.ipynb`**
  - Input: `Exercício1.txt` (coluna `Yt`, ~75 valores entre -2,11 e 2,61 — série centrada em torno de 0, já com "cara" de estacionária).
  - Conteúdo: teste de estacionariedade → conclusão "série original já é estacionária" (d=0); comparação de candidatos; conclusão final: melhor previsão com MA(1) (q=1).
  - Subtópico: identificação de ordem MA em série já estacionária (ordem (0,0,1)).
- **`ARIMA/Exercício2.txt`** → **`ARIMA/ARIMA_Ex2.ipynb`**
  - Input: `Exercício2.txt` (coluna `Yt`, 62 valores crescentes de 222,34 a 281,75 — tendência forte, não estacionária).
  - Conteúdo: usa `auto_arima`; discute mínimo local (1,1,0) vs. mínimo global; força `d=2` e confirma ordem (0,2,1).
  - Subtópico: identificação de ordem com dupla diferenciação (d=2) via busca automática (auto_arima), incluindo a armadilha de mínimo local.
  - **Relação:** ambos aplicam a mesma metodologia do item 2.3 (seção 7/8 do notebook de referência), mas com séries reais de "Exercício1/2.txt" e usando `auto_arima` em vez de busca manual por grade.

### 2.5 Subtópico: exercícios da Aula 07 ainda sem notebook de solução
- **`novas/Aula 07.pdf`** (slides) referenciam:
  - **`novas/07 - Dados Ex 02.txt`** — dados brutos de duas colunas `X` e `Y` (ex.: X=10→220, Y decimais entre 0,5 e 4,1). Pelo formato (uma variável explicativa X e uma resposta Y), parece ser exercício de **regressão/ajuste de tendência** (não ARIMA propriamente), possivelmente ligado a dimensionamento de amostra ou ajuste de curva de demanda vs. tempo/volume.
  - **`novas/07 - Dados Ex 04.xlsx`** (aba única `ex`) — dados do Exercício 04 da Aula 07.
  - **Nenhum destes dois tem notebook de resolução correspondente nesta pasta** — ao contrário do par Exercício1/2.txt + ARIMA_Ex1/2.ipynb (item 2.4), aqui faltam as soluções.
- **`novas/Aula 08.pdf`** — não há nenhum dado (`txt`/`xlsx`) nem notebook vinculado a este slide na pasta; parece ser só material de leitura (possivelmente conteúdo intermediário entre decomposição e ARIMA, ou revisão).

### 2.6 Subtópico: ARIMA aplicado a dados reais, com busca automática de melhor modelo (grid search por AIC)
- **`Atividades/Atv2.xlsx`** (aba `Sheet1`, duas séries temporais) → **`Atividades/Atv2.ipynb`**
  - Conteúdo: função própria `find_best_arima(series, p_range, d_range, q_range)` que testa todas as combinações de (p,d,q) e escolhe a de menor AIC, usando `adfuller`, `acf`, `pacf`. Carrega e indexa as duas séries da planilha com datas a partir de 2020-01-01.
  - Subtópico: automação da metodologia Box-Jenkins (equivalente em espírito ao `auto_arima` do item 2.4, mas implementado manualmente com grid search).
  - **Relação:** reaplica a metodologia do item 2.3/2.4, porém sobre um conjunto de dados avaliativo próprio (atividade), não sobre os exemplos de aula.

---

## 3. Macro-tema "Decomposição de séries temporais" (não é ARIMA)

- **`Decomposição Serie Temporal.ipynb`**
  - Input: séries sintéticas geradas no próprio notebook (sem arquivo externo), 60 observações mensais (2021-01 a 2025-12).
  - Subtópicos, em ordem:
    1. Criação de eixo temporal mensal.
    2. Construção de série **aditiva** (tendência linear + sazonalidade + ruído).
    3. Decomposição aditiva (`seasonal_decompose`, `model="additive"`, período 12).
    4. Construção de série **multiplicativa** (tendência × fator sazonal).
    5. Decomposição multiplicativa (`model="multiplicative"`).
    6. Comparação das componentes sazonais aditiva vs. multiplicativa.
    7. Transformação logarítmica de série multiplicativa (para tratá-la como aditiva em log).
  - **Sem overlap de conteúdo** com os notebooks de AR/MA/ARIMA — é pré-requisito conceitual (entender tendência/sazonalidade antes de modelar os resíduos com ARIMA), mas tecnicamente independente.

---

## 4. Macro-tema "Estimação e Testes de Hipótese" (fundamentação estatística, não é série temporal)

- **`Estimacao_Testes_Hipotese.ipynb`** — material de apoio a aula distinta (não há PDF correspondente nesta pasta). Subtópicos:
  1. Fundamentos da inferência (ponto de partida: processo exponencial simulado — tempo entre chegadas).
  2. Estimação pontual da média + Teorema do Limite Central (TLC) + erro padrão.
  3. Intervalos de confiança: variância conhecida (IC com Z) → Exemplo "tempo de estudo"; dimensionamento de amostra → Exemplo "baterias"; variância desconhecida (IC com t de Student) → Exemplo "consumo de combustível"; comparação empírica Z vs. t por simulação.
  4. Testes de hipótese: região crítica/erro tipo I e II → Exemplo "consumo de combustível"; confirmação de α por Monte Carlo; teste unilateral → Exemplo "fila de votação"; p-valor → exemplo genérico.
  5. Síntese estimação vs. teste de hipótese.
  6. **3 exercícios propostos resolvidos** (dados embutidos no texto do próprio notebook, sem arquivo externo): (1) teste bilateral de média com σ conhecido; (2) teste de regulagem de máquina (diâmetro de peça); (3) salário de estagiários (TLC com n grande).
  - **Isolado:** não compartilha dados nem metodologia com os notebooks de ARIMA/decomposição — é pré-requisito de estatística geral (amostragem, não processos estocásticos temporais).

---

## 5. Macro-tema "Dados reais de atracação de navios"

- **`Atividades/Atv1.xlsx`** (abas `2024Atracacao` e `Nomes`) → **`Atividades/Atv1.ipynb`**
  - Conteúdo: filtra `Complexo Portuário == "São Sebastião"`; identifica colunas (ex.: "Data Chegada"); calcula 4 tempos operacionais — **fila**, **pré-operação**, **operação**, **pós-operação** — cada um com: estatísticas gerais, detecção de outliers, boxplot, histograma, testes de aderência (a alguma distribuição teórica).
  - Subtópico: estatística descritiva aplicada + testes de aderência de distribuição (não é modelagem ARIMA nem decomposição) — mais próximo do macro-tema de estimação/testes (item 4) do que de séries temporais, mas usa dados portuários reais em vez de simulação.
  - **Sem relação direta** com os demais notebooks de ARIMA, exceto o uso comum de `statsmodels`/testes estatísticos.

---

## 6. Fora do escopo "Previsão de Demanda"

- **`ARIMA/Atividades_DES.ipynb`** — apesar de estar na pasta `ARIMA/`, o conteúdo (exercícios 2, 5, 6, 8) é de **teoria de filas / simulação de eventos discretos (DES)**: comparação de taxas de atendimento vs. número de postos, filas M/M/c aplicadas a atracação de navios em berços, cálculo de número médio de navios na fila, tempo médio no sistema, probabilidades de ocupação. **Não usa ARIMA nem séries temporais** — está mal classificado na pasta.

---

## 7. Tabela-síntese: exercício → subtópico → input

| Arquivo (resolução) | Subtópico exato | Input (dado bruto) |
|---|---|---|
| `ARIMA/ARIMA - Parte 1.ipynb` | AR(2)/AR(3) e MA(1), MSE | série embutida (75 obs.) — rascunho de `PNV3421_Aula09_ARIMA.ipynb` §1–2 |
| `ARIMA/ARIMA - Parte 2.ipynb` | ADF + ACF/PACF em 4 séries, Box-Jenkins no Exemplo 4 | `data1..data4` embutidos — rascunho de `PNV3421_Aula09_ARIMA.ipynb` §4,7 |
| `novas/PNV3421_Aula09_ARIMA.ipynb` | Teoria completa AR/MA/suavização/ARIMA/ACF-PACF/Ljung-Box/treino-teste (referência) | dados embutidos (mesmos de Parte 1 e 2) + 2 exercícios finais sem solução |
| `ARIMA/ARIMA_Ex1.ipynb` | Identificação MA(1) em série estacionária (d=0) | `ARIMA/Exercício1.txt` |
| `ARIMA/ARIMA_Ex2.ipynb` | Identificação (0,2,1) via auto_arima, armadilha de mínimo local | `ARIMA/Exercício2.txt` |
| *(sem notebook)* | Exercício 02 da Aula 07 (provável regressão/tendência X→Y) | `novas/07 - Dados Ex 02.txt` |
| *(sem notebook)* | Exercício 04 da Aula 07 | `novas/07 - Dados Ex 04.xlsx` (aba `ex`) |
| `Atividades/Atv2.ipynb` | Busca automática de melhor ARIMA (grid search por AIC) | `Atividades/Atv2.xlsx` (aba `Sheet1`, 2 séries) |
| `Atividades/Atv1.ipynb` | Estatística descritiva + testes de aderência (tempos de fila/pré-operação/operação/pós-operação) | `Atividades/Atv1.xlsx` (abas `2024Atracacao`, `Nomes`) |
| `Decomposição Serie Temporal.ipynb` | Decomposição aditiva/multiplicativa + transformação log | série sintética embutida |
| `Estimacao_Testes_Hipotese.ipynb` | TLC, IC (Z e t), dimensionamento de amostra, testes de hipótese (bi/unilateral), p-valor | exemplos embutidos no texto |
| `ARIMA/Atividades_DES.ipynb` | Teoria de filas (M/M/c), fora do escopo ARIMA | dados embutidos (exercícios de aula de filas) |

---

## 8. Observações finais
- Os únicos pares **dado bruto + solução** completos são: `Exercício1.txt`↔`ARIMA_Ex1.ipynb`, `Exercício2.txt`↔`ARIMA_Ex2.ipynb`, `Atv1.xlsx`↔`Atv1.ipynb`, `Atv2.xlsx`↔`Atv2.ipynb`.
- Os dados da Aula 07 (`07 - Dados Ex 02.txt`, `07 - Dados Ex 04.xlsx`) estão **sem solução** nesta pasta.
- Os três notebooks de teoria AR/MA/ARIMA (`ARIMA - Parte 1`, `ARIMA - Parte 2`, `PNV3421_Aula09_ARIMA`) tratam, célula a célula, dos **mesmos dados e subtópicos em grau crescente de completude** — não é apenas repetição temática genérica, é o mesmo exemplo numérico revisitado.
- `Decomposição Serie Temporal.ipynb` e `Estimacao_Testes_Hipotese.ipynb` não se repetem entre si nem com nenhum outro notebook — cada um cobre um subtema estatístico próprio e isolado.
