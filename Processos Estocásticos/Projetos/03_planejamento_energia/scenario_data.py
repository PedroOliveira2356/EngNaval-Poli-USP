"""
Dados do problema de planejamento de capacidade de geracao de energia
(baseado no "Exemplo 2" de proc_estoc.ipynb).

1o estagio: quanta capacidade instalar de cada fonte (investimento).
2o estagio: quanto gerar, hora a hora, para atender a demanda, dado o
            cenario de demanda / disponibilidade eolica / custo de
            combustivel realizado.

Os cenarios sao gerados de forma deterministica (seed fixa) para que o
exemplo seja reprodutivel sem depender de estado aleatorio externo.
"""

import numpy as np

GERADORES = ["Carvao", "Gas", "Nuclear", "Eolica"]
HORAS = list(range(1, 25))  # 24 horas do dia

CUSTO_CAPACIDADE = {  # $/MW instalado (custo de investimento anualizado)
    "Carvao": 1000.0,
    "Gas": 800.0,
    "Nuclear": 3000.0,
    "Eolica": 1200.0,
}

CAPACIDADE_MAXIMA = {  # MW, limite superior de capacidade instalavel
    "Carvao": 500.0,
    "Gas": 400.0,
    "Nuclear": 300.0,
    "Eolica": 200.0,
}

N_CENARIOS = 5
_SEED = 42


def _gerar_cenarios():
    rng = np.random.default_rng(_SEED)
    cenarios = {}

    for s in range(N_CENARIOS):
        nome = f"cenario_{s + 1}"

        # Demanda: padrao diario senoidal (pico a tarde) + ruido log-normal.
        demanda_base = [
            500 + 300 * np.sin(2 * np.pi * (t - 9) / 24) for t in HORAS
        ]
        demanda = {
            t: max(0.0, d * rng.lognormal(mean=0.0, sigma=0.12))
            for t, d in zip(HORAS, demanda_base)
        }

        # Disponibilidade eolica: padrao senoidal (mais vento a noite) * ruido beta.
        disponibilidade_eolica = {
            t: float(
                np.clip(
                    (0.6 + 0.3 * np.sin(2 * np.pi * (t - 3) / 24))
                    * rng.beta(a=2, b=2)
                    * 1.3,
                    0.0,
                    1.0,
                )
            )
            for t in HORAS
        }

        # Custo de combustivel ($/MWh), constante ao longo do dia no cenario.
        custo_combustivel = {
            "Carvao": float(rng.uniform(20, 30)),
            "Gas": float(rng.uniform(40, 60)),
            "Nuclear": float(rng.uniform(5, 10)),
            "Eolica": 0.0,
        }

        cenarios[nome] = {
            "probabilidade": 1.0 / N_CENARIOS,
            "demanda": demanda,
            "disponibilidade_eolica": disponibilidade_eolica,
            "custo_combustivel": custo_combustivel,
        }

    return cenarios


SCENARIOS = _gerar_cenarios()
