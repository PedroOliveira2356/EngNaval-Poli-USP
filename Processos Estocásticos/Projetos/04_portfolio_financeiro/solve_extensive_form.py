"""
Resolve a otimizacao de portfolio (minimizacao de CVaR) pela forma
extensiva: milhares de cenarios de retorno, cada um contribuindo com uma
variavel de excesso (2o estagio), todos amarrados as mesmas variaveis de
1o estagio (alocacao da carteira e o VaR auxiliar zeta).

Uso:
    python solve_extensive_form.py
"""

import pyomo.environ as pyo

from reference_model import populate_second_stage
from scenario_data import (
    ATIVOS,
    PATRIMONIO_INICIAL,
    RETORNO_MINIMO_ESPERADO,
    ALPHA_CVAR,
    SCENARIOS,
)

SOLVER = "appsi_highs"


def build_extensive_form():
    m = pyo.ConcreteModel(name="portfolio_forma_extensiva")

    m.alocacao = pyo.Var(ATIVOS, domain=pyo.NonNegativeReals)
    m.zeta = pyo.Var(domain=pyo.Reals)  # VaR auxiliar, tambem de 1o estagio

    m.orcamento = pyo.Constraint(
        expr=sum(m.alocacao[a] for a in ATIVOS) == PATRIMONIO_INICIAL
    )

    retorno_esperado_ativo = {
        a: sum(
            SCENARIOS[s]["probabilidade"] * SCENARIOS[s]["retorno"][a]
            for s in SCENARIOS
        )
        for a in ATIVOS
    }
    m.restricao_retorno_minimo = pyo.Constraint(
        expr=sum(retorno_esperado_ativo[a] * m.alocacao[a] for a in ATIVOS)
        >= RETORNO_MINIMO_ESPERADO * PATRIMONIO_INICIAL
    )

    m.cenarios = pyo.Block(list(SCENARIOS.keys()))
    for nome_cenario in SCENARIOS:
        populate_second_stage(m.cenarios[nome_cenario], nome_cenario, m.alocacao, m.zeta)

    m.cvar = pyo.Expression(
        expr=m.zeta
        + (1 / (1 - ALPHA_CVAR))
        * sum(
            SCENARIOS[s]["probabilidade"] * m.cenarios[s].excesso for s in SCENARIOS
        )
    )
    m.obj = pyo.Objective(expr=m.cvar, sense=pyo.minimize)

    return m


def imprimir_solucao(m):
    print("=== Alocacao otima da carteira (1o estagio) ===")
    for a in ATIVOS:
        valor = pyo.value(m.alocacao[a])
        print(f"  {a:12s}: $ {valor:12,.2f}  ({100 * valor / PATRIMONIO_INICIAL:5.1f}%)")

    retorno_esperado = sum(
        SCENARIOS[s]["probabilidade"]
        * sum(
            pyo.value(m.alocacao[a]) * SCENARIOS[s]["retorno"][a] for a in ATIVOS
        )
        for s in SCENARIOS
    ) / PATRIMONIO_INICIAL

    print(f"\n  Retorno esperado da carteira: {100 * retorno_esperado:5.2f}% a.a.")
    print(f"  VaR ({int(100*ALPHA_CVAR)}%)  (zeta): $ {pyo.value(m.zeta):12,.2f}")
    print(f"  CVaR ({int(100*ALPHA_CVAR)}%) (objetivo): $ {pyo.value(m.obj):12,.2f}")
    print(
        "  (CVaR = perda media esperada, condicionada aos "
        f"{int(100 * (1 - ALPHA_CVAR))}% piores cenarios)"
    )


if __name__ == "__main__":
    modelo = build_extensive_form()
    resultado = pyo.SolverFactory(SOLVER).solve(modelo, tee=False)
    imprimir_solucao(modelo)
