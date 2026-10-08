"""
Reference Model do problema do jornaleiro (newsvendor).

Mesma ideia do projeto 01 (fazendeiro), mas com um modelo bem mais
simples: 1 variavel de 1o estagio (quantidade comprada) e 3 variaveis de
2o estagio por cenario (vendido, sobra, falta).
"""

import pyomo.environ as pyo

from scenario_data import (
    PRECO_COMPRA,
    PRECO_VENDA,
    VALOR_RESIDUAL,
    CUSTO_FALTA,
    SCENARIOS,
)


def populate_second_stage(block, nome_cenario, quantidade_comprada):
    demanda = SCENARIOS[nome_cenario]["demanda"]

    block.vendido = pyo.Var(domain=pyo.NonNegativeReals, bounds=(0, demanda))
    block.sobra = pyo.Var(domain=pyo.NonNegativeReals)
    block.falta = pyo.Var(domain=pyo.NonNegativeReals)

    block.balanco_estoque = pyo.Constraint(
        expr=block.vendido + block.sobra == quantidade_comprada
    )
    block.balanco_demanda = pyo.Constraint(
        expr=block.vendido + block.falta == demanda
    )

    block.receita_segundo_estagio = pyo.Expression(
        expr=PRECO_VENDA * block.vendido
        + VALOR_RESIDUAL * block.sobra
        - CUSTO_FALTA * block.falta
    )


def build_single_scenario_model(nome_cenario):
    m = pyo.ConcreteModel(name=f"jornaleiro_{nome_cenario}")

    m.quantidade_comprada = pyo.Var(domain=pyo.NonNegativeReals)
    populate_second_stage(m, nome_cenario, m.quantidade_comprada)

    m.lucro = pyo.Expression(
        expr=m.receita_segundo_estagio - PRECO_COMPRA * m.quantidade_comprada
    )
    m.obj = pyo.Objective(expr=m.lucro, sense=pyo.maximize)

    return m
