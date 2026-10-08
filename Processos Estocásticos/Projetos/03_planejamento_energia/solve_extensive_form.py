"""
Resolve o planejamento de capacidade de geracao de energia pela forma
extensiva: investimento (1o estagio) compartilhado por todos os
cenarios de demanda/vento/custo de combustivel, com despacho horario
(2o estagio) especifico de cada cenario.

Uso:
    python solve_extensive_form.py
"""

import pyomo.environ as pyo

from reference_model import build_single_scenario_model, populate_second_stage
from scenario_data import GERADORES, CAPACIDADE_MAXIMA, CUSTO_CAPACIDADE, SCENARIOS

SOLVER = "appsi_highs"


def build_extensive_form():
    m = pyo.ConcreteModel(name="energia_forma_extensiva")

    m.capacidade = pyo.Var(GERADORES, domain=pyo.NonNegativeReals)

    @m.Constraint(GERADORES)
    def limite_capacidade(m, g):
        return m.capacidade[g] <= CAPACIDADE_MAXIMA[g]

    m.cenarios = pyo.Block(list(SCENARIOS.keys()))
    for nome_cenario in SCENARIOS:
        populate_second_stage(m.cenarios[nome_cenario], nome_cenario, m.capacidade)

    custo_investimento = sum(CUSTO_CAPACIDADE[g] * m.capacidade[g] for g in GERADORES)

    m.custo_por_cenario = pyo.Expression(
        list(SCENARIOS.keys()),
        rule=lambda m, s: custo_investimento + m.cenarios[s].custo_operacional,
    )

    m.obj = pyo.Objective(
        expr=sum(
            SCENARIOS[s]["probabilidade"] * m.custo_por_cenario[s] for s in SCENARIOS
        ),
        sense=pyo.minimize,
    )

    return m


def imprimir_solucao(m):
    print("=== Capacidade instalada (1o estagio, MW) ===")
    for g in GERADORES:
        print(f"  {g:8s}: {pyo.value(m.capacidade[g]):8.2f}")

    print("\n=== Custo total esperado e por cenario ===")
    custo_esperado = pyo.value(m.obj)
    for nome_cenario, dados in SCENARIOS.items():
        custo_cenario = pyo.value(m.custo_por_cenario[nome_cenario])
        print(
            f"  {nome_cenario:12s} (p={dados['probabilidade']:.2f}): "
            f"custo = {custo_cenario:14,.2f}"
        )
    print(f"\n  Custo total esperado (valor otimo do SP) = {custo_esperado:14,.2f}")
    return custo_esperado


def valor_esperado_com_informacao_perfeita(solver_name=SOLVER):
    total = 0.0
    for nome_cenario, dados in SCENARIOS.items():
        sub = build_single_scenario_model(nome_cenario)
        pyo.SolverFactory(solver_name).solve(sub, tee=False)
        total += dados["probabilidade"] * pyo.value(sub.custo_total)
    return total


if __name__ == "__main__":
    modelo = build_extensive_form()
    pyo.SolverFactory(SOLVER).solve(modelo, tee=False)
    custo_sp = imprimir_solucao(modelo)

    custo_ws = valor_esperado_com_informacao_perfeita()
    print("\n=== Comparacao com informacao perfeita (wait-and-see) ===")
    print(f"  Custo esperado com informacao perfeita: {custo_ws:14,.2f}")
    print(f"  EVPI (Expected Value of Perfect Information) = {custo_sp - custo_ws:14,.2f}")
