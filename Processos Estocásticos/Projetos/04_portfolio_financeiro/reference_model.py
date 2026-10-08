"""
Reference Model do problema de otimizacao de portfolio via minimizacao
de CVaR (Rockafellar & Uryasev, 2000).

1o estagio: pesos da carteira (`alocacao`) e o VaR auxiliar (`zeta`).
2o estagio: perda do cenario e sua parte acima do VaR (`excesso`), que e
            o unico "recurso" deste problema.

Formulacao (para alpha = nivel de confianca, ex. 0.95):
    minimizar   zeta + 1/(1-alpha) * E[excesso]
    sujeito a   excesso_s >= perda_s - zeta       para todo cenario s
                excesso_s >= 0
                perda_s = patrimonio_inicial - soma_a alocacao_a * (1+retorno_a,s)
                E[retorno da carteira] >= retorno_minimo_esperado
                soma_a alocacao_a = patrimonio_inicial,  alocacao_a >= 0
"""

import pyomo.environ as pyo

from scenario_data import (
    ATIVOS,
    PATRIMONIO_INICIAL,
    SCENARIOS,
    ALPHA_CVAR,
)


def populate_second_stage(block, nome_cenario, alocacao, zeta):
    retorno = SCENARIOS[nome_cenario]["retorno"]

    patrimonio_final = sum(
        alocacao[a] * (1 + retorno[a]) for a in ATIVOS
    )
    block.perda = pyo.Expression(expr=PATRIMONIO_INICIAL - patrimonio_final)

    block.excesso = pyo.Var(domain=pyo.NonNegativeReals)
    block.define_excesso = pyo.Constraint(expr=block.excesso >= block.perda - zeta)


def build_single_scenario_model(nome_cenario):
    """Modelo completo para um unico cenario de retorno — usado apenas
    para inspecionar o pior/melhor caso isolado (nao faz muito sentido
    minimizar CVaR com 1 cenario so, mas serve para checagem de dados)."""
    m = pyo.ConcreteModel(name=f"portfolio_{nome_cenario}")

    m.alocacao = pyo.Var(ATIVOS, domain=pyo.NonNegativeReals)
    m.orcamento = pyo.Constraint(
        expr=sum(m.alocacao[a] for a in ATIVOS) == PATRIMONIO_INICIAL
    )
    m.zeta = pyo.Var(domain=pyo.Reals)

    populate_second_stage(m, nome_cenario, m.alocacao, m.zeta)

    m.cvar = pyo.Expression(expr=m.zeta + (1 / (1 - ALPHA_CVAR)) * m.excesso)
    m.obj = pyo.Objective(expr=m.cvar, sense=pyo.minimize)

    return m
