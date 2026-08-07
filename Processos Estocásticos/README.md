# Processos Estocásticos

Modelagem e análise de processos estocásticos aplicados a dados portuários e séries temporais: cadeias de Markov, modelos ARIMA e análise exploratória.

## Conteúdo

| Arquivo | Descrição |
|---------|-----------|
| [`proc_estoc.ipynb`](proc_estoc.ipynb) | Introdução a bibliotecas de programação estocástica (PySP/Pyomo, PyMC) e cadeias de Markov com exemplo de locação de veículos |
| [`ARIMA - Parte 1.ipynb`](ARIMA%20-%20Parte%201.ipynb) | Ajuste de modelos AR(2) e AR(3) a uma série temporal; cálculo de valores ajustados e MSE comparativo |
| [`ARIMA - Parte 2.ipynb`](ARIMA%20-%20Parte%202.ipynb) | Modelos ARIMA completos: teste ADF de estacionariedade, ACF/PACF, seleção de ordem e diagnóstico de resíduos (Ljung-Box) |
| [`Atv1.ipynb`](Atv1.ipynb) | **Dados reais:** análise exploratória estatística dos tempos de atracação de embarcações no Porto de São Sebastião (dataset ANTAQ) |
| [`Atv2.ipynb`](Atv2.ipynb) | Seleção automática do melhor ARIMA por grid-search em (p,d,q) via AIC e previsão de duas séries temporais |
| `2024TemposAtracacao.xlsx` | Dataset ANTAQ — tempos de atracação (entrada de dados para Atv1) |
| `Atv2.xlsx` | Séries temporais para modelagem em Atv2 |

## Atividade 1 — Porto de São Sebastião

Análise exploratória completa do dataset real de tempos de atracação da ANTAQ: distribuição dos tempos por tipo de carga, sazonalidade, estatísticas descritivas e visualizações.

## Atividade 2 — Seleção de Modelos ARIMA

Grid-search sobre combinações de ordens $(p, d, q)$ minimizando o AIC, teste de Ljung-Box para validar ausência de autocorrelação nos resíduos e previsão out-of-sample.

## Conceitos

- Cadeias de Markov: matriz de transição, estado estacionário
- Estacionariedade e teste ADF (Augmented Dickey-Fuller)
- Funções de autocorrelação (ACF) e autocorrelação parcial (PACF)
- Modelos AR, MA, ARMA, ARIMA
- Critério de informação de Akaike (AIC)
- Teste de Ljung-Box para diagnóstico de resíduos

## Bibliotecas

`statsmodels`, `pandas`, `numpy`, `matplotlib`, `scipy`, `openpyxl`
