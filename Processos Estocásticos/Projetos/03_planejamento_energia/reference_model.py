"""
Reference Model do planejamento de capacidade de geracao de energia.

Mesmo padrao dos outros projetos: `populate_second_stage` monta as
variaveis/restricoes de despacho (2o estagio) para um cenario, em funcao
de uma variavel de capacidade (1o estagio) externa.
"""

import pyomo.environ as pyo

from scenario_data import GERADORES, HORAS, CAPACIDADE_MAXIMA, SCENARIOS


def populate_second_stage(block, nome_cenario, capacidade):
    dados = SCENARIOS[nome_cenario]
    demanda = dados["demanda"]
    disponibilidade_eolica = dados["disponibilidade_eolica"]
    custo_combustivel = dados["custo_combustivel"]

    block.geracao = pyo.Var(GERADORES, HORAS, domain=pyo.NonNegativeReals)

    @block.Constraint(HORAS)
    def atende_demanda(blk, t):
        return sum(blk.geracao[g, t] for g in GERADORES) >= demanda[t]

    @block.Constraint(GERADORES, HORAS)
    def limite_geracao(blk, g, t):
        if g == "Eolica":
            return blk.geracao[g, t] <= capacidade[g] * disponibilidade_eolica[t]
        return blk.geracao[g, t] <= capacidade[g]

    block.custo_operacional = pyo.Expression(
        expr=sum(
            custo_combustivel[g] * block.geracao[g, t]
            for g in GERADORES
            for t in HORAS
        )
    )


def build_single_scenario_model(nome_cenario):
    """Modelo completo (investimento + despacho) para um unico cenario —
    usado nos calculos de EV (cenario medio) e WS (wait-and-see)."""
    m = pyo.ConcreteModel(name=f"energia_{nome_cenario}")

    m.capacidade = pyo.Var(GERADORES, domain=pyo.NonNegativeReals)

    @m.Constraint(GERADORES)
    def limite_capacidade(m, g):
        return m.capacidade[g] <= CAPACIDADE_MAXIMA[g]

    populate_second_stage(m, nome_cenario, m.capacidade)

    from scenario_data import CUSTO_CAPACIDADE

    m.custo_investimento = pyo.Expression(
        expr=sum(CUSTO_CAPACIDADE[g] * m.capacidade[g] for g in GERADORES)
    )
    m.custo_total = pyo.Expression(expr=m.custo_investimento + m.custo_operacional)
    m.obj = pyo.Objective(expr=m.custo_total, sense=pyo.minimize)

    return m
