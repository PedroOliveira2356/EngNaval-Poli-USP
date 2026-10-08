"""
Reference Model do problema do fazendeiro (Birge & Louveaux, cap. 1).

Equivale ao ReferenceModel.py do PySP: define as variaveis e restricoes
de 2o estagio em funcao de uma area plantada (variavel de 1o estagio),
que pode ser a variavel "local" de um modelo de cenario unico
(build_single_scenario_model) ou a variavel COMPARTILHADA entre todos os
cenarios na forma extensiva (ver solve_extensive_form.py). Usar a mesma
instancia de area_plantada em todos os cenarios e exatamente o que impoe
a restricao de nao-antecipatividade (a decisao de plantio e tomada
"aqui-e-agora", antes de a produtividade real ser conhecida).
"""

import pyomo.environ as pyo

from scenario_data import (
    CROPS,
    AREA_TOTAL,
    CUSTO_PLANTIO,
    PRECO_VENDA,
    PRECO_VENDA_EXCEDENTE_BETERRABA,
    PRODUCAO_COTA_BETERRABA,
    PRECO_COMPRA,
    CONSUMO_MINIMO,
    produtividade_cenario,
)


def populate_second_stage(block, nome_cenario, area_plantada):
    """Adiciona ao `block` as variaveis/restricoes de 2o estagio de um
    cenario, em funcao da variavel de 1o estagio `area_plantada` (um
    Var ou Reference indexado por CROPS)."""
    produtividade = produtividade_cenario(nome_cenario)

    block.vendido = pyo.Var(CROPS, domain=pyo.NonNegativeReals)
    block.comprado = pyo.Var(["trigo", "milho"], domain=pyo.NonNegativeReals)
    # beterraba vendida em duas faixas de preco (normal / excedente da cota)
    block.beterraba_vendida_cota = pyo.Var(
        domain=pyo.NonNegativeReals, bounds=(0, PRODUCAO_COTA_BETERRABA)
    )
    block.beterraba_vendida_excedente = pyo.Var(domain=pyo.NonNegativeReals)
    block.vendido["beterraba"].fix(0)  # usamos as duas variaveis de faixa acima

    def producao_total(cultura):
        return area_plantada[cultura] * produtividade[cultura]

    @block.Constraint(["trigo", "milho"])
    def balanco_consumo(blk, cultura):
        # producao + comprado - vendido >= consumo minimo exigido
        return (
            producao_total(cultura) + blk.comprado[cultura] - blk.vendido[cultura]
            >= CONSUMO_MINIMO[cultura]
        )

    block.balanco_beterraba = pyo.Constraint(
        expr=block.beterraba_vendida_cota + block.beterraba_vendida_excedente
        <= producao_total("beterraba")
    )

    custo_compra = sum(
        PRECO_COMPRA[c] * block.comprado[c] for c in ["trigo", "milho"]
    )
    receita_venda = sum(
        PRECO_VENDA[c] * block.vendido[c] for c in ["trigo", "milho"]
    ) + (
        PRECO_VENDA["beterraba"] * block.beterraba_vendida_cota
        + PRECO_VENDA_EXCEDENTE_BETERRABA * block.beterraba_vendida_excedente
    )

    block.receita_venda = pyo.Expression(expr=receita_venda)
    block.custo_compra = pyo.Expression(expr=custo_compra)


def build_single_scenario_model(nome_cenario):
    """Modelo deterministico completo (1o + 2o estagio) para um cenario
    isolado — usado para os calculos de EV (expected value problem) e
    WS (wait-and-see) em solve_extensive_form.py."""
    m = pyo.ConcreteModel(name=f"fazendeiro_{nome_cenario}")

    m.area_plantada = pyo.Var(CROPS, domain=pyo.NonNegativeReals)
    m.restricao_area = pyo.Constraint(
        expr=sum(m.area_plantada[c] for c in CROPS) <= AREA_TOTAL
    )

    populate_second_stage(m, nome_cenario, m.area_plantada)

    custo_plantio = sum(CUSTO_PLANTIO[c] * m.area_plantada[c] for c in CROPS)
    m.lucro = pyo.Expression(
        expr=m.receita_venda - custo_plantio - m.custo_compra
    )
    m.obj = pyo.Objective(expr=m.lucro, sense=pyo.maximize)

    return m
