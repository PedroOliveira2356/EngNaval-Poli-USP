"""
Dados do problema de otimizacao de portfolio sob retornos incertos
(baseado no "Exemplo 3" de proc_estoc.ipynb).

O esboco original do notebook monta um modelo de 1o estagio (alocacao
inicial) mas nunca chega a definir um 2o estagio / objetivo concretos
(so comentarios sobre L-Shaped e um callback de exemplo). Aqui
preenchemos essa lacuna com a formulacao padrao da literatura para esse
tipo de problema: **minimizacao de CVaR (Conditional Value at Risk) de
Rockafellar & Uryasev**, que e exatamente um programa estocastico de 2
estagios linear (1o estagio = pesos da carteira; 2o estagio = variaveis
auxiliares de perda por cenario).

Os cenarios de retorno sao amostrados (seed fixa, reprodutivel) de uma
normal multivariada correlacionada, em vez de poucos cenarios discretos
— tipico em otimizacao de portfolio, onde se usa um numero grande de
amostras para aproximar a distribuicao de perdas.
"""

import numpy as np

ATIVOS = ["Acoes", "Titulos", "Ouro", "ImoveisFII"]

PATRIMONIO_INICIAL = 1_000_000.0  # $

# Retorno esperado anual (mu) e volatilidade anual (sigma) de cada ativo.
RETORNO_MEDIO = {
    "Acoes": 0.08,
    "Titulos": 0.04,
    "Ouro": 0.03,
    "ImoveisFII": 0.06,
}
VOLATILIDADE = {
    "Acoes": 0.20,
    "Titulos": 0.05,
    "Ouro": 0.15,
    "ImoveisFII": 0.10,
}

# Matriz de correlacao entre ativos (ordem: Acoes, Titulos, Ouro, ImoveisFII).
# Titulos tende a ser descorrelacionado/negativamente correlacionado com
# Acoes (efeito "flight to quality"); Ouro e defensivo; FII acompanha
# parcialmente o mercado de acoes.
CORRELACAO = np.array(
    [
        [1.00, -0.20, -0.10, 0.30],
        [-0.20, 1.00, 0.10, 0.00],
        [-0.10, 0.10, 1.00, 0.10],
        [0.30, 0.00, 0.10, 1.00],
    ]
)

N_CENARIOS = 2000
_SEED = 7

ALPHA_CVAR = 0.95  # nivel de confianca do CVaR (ex.: pior 5% dos cenarios)
RETORNO_MINIMO_ESPERADO = 0.06  # restricao: retorno esperado >= 6% a.a.


def _gerar_cenarios_retorno():
    ativos = ATIVOS
    mu = np.array([RETORNO_MEDIO[a] for a in ativos])
    sigma = np.array([VOLATILIDADE[a] for a in ativos])
    cov = np.outer(sigma, sigma) * CORRELACAO

    rng = np.random.default_rng(_SEED)
    amostras = rng.multivariate_normal(mean=mu, cov=cov, size=N_CENARIOS)

    # retorno minimo de -100% (nao faz sentido perder mais que o investido)
    amostras = np.maximum(amostras, -0.999)

    return {
        f"cenario_{i + 1}": {
            "probabilidade": 1.0 / N_CENARIOS,
            "retorno": {a: float(amostras[i, j]) for j, a in enumerate(ativos)},
        }
        for i in range(N_CENARIOS)
    }


SCENARIOS = _gerar_cenarios_retorno()
