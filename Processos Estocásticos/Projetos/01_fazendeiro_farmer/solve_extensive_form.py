"""
Resolve o problema do fazendeiro como um programa estocastico de dois
estagios, pela "forma extensiva" (deterministic equivalent): um unico
modelo Pyomo com uma copia das variaveis de 2o estagio por cenario,
todas penduradas na MESMA variavel de 1o estagio (area plantada).

Equivale ao que o runph.py do PySP fazia via Progressive Hedging, so que
aqui resolvemos o problema inteiro de uma vez com um solver de PL/MILP
comum (PySP foi descontinuado; o sucessor oficial e o pacote mpi-sppy).

Uso:
    python solve_extensive_form.py
"""

import pyomo.environ as pyo

from reference_model import build_single_scenario_model, populate_second_stage
from scenario_data import CROPS, AREA_TOTAL, CUSTO_PLANTIO, SCENARIOS

SOLVER = "appsi_highs"  # solver livre (HiGHS). Troque por "gurobi" se preferir.


def build_extensive_form():
    m = pyo.ConcreteModel(name="fazendeiro_forma_extensiva")

    # Variavel de 1o estagio: unica, compartilhada por todos os cenarios
    # (e isso que garante a nao-antecipatividade da decisao de plantio).
    m.area_plantada = pyo.Var(CROPS, domain=pyo.NonNegativeReals)
    m.restricao_area = pyo.Constraint(
        expr=sum(m.area_plantada[c] for c in CROPS) <= AREA_TOTAL
    )

    m.cenarios = pyo.Block(list(SCENARIOS.keys()))
    for nome_cenario in SCENARIOS:
        populate_second_stage(m.cenarios[nome_cenario], nome_cenario, m.area_plantada)

    custo_plantio = sum(CUSTO_PLANTIO[c] * m.area_plantada[c] for c in CROPS)

    def lucro_cenario(nome_cenario):
        bloco = m.cenarios[nome_cenario]
        return bloco.receita_venda - custo_plantio - bloco.custo_compra

    m.lucro_por_cenario = pyo.Expression(
        list(SCENARIOS.keys()), rule=lambda m, s: lucro_cenario(s)
    )

    m.obj = pyo.Objective(
        expr=sum(
            SCENARIOS[s]["probabilidade"] * m.lucro_por_cenario[s] for s in SCENARIOS
        ),
        sense=pyo.maximize,
    )

    return m


def resolver(modelo, solver_name=SOLVER):
    solver = pyo.SolverFactory(solver_name)
    resultado = solver.solve(modelo, tee=False)
    return resultado


def imprimir_solucao(m):
    print("=== Plantio de 1o estagio (acres) ===")
    for c in CROPS:
        print(f"  {c:10s}: {pyo.value(m.area_plantada[c]):8.2f}")

    print("\n=== Lucro esperado e por cenario ===")
    lucro_esperado = pyo.value(m.obj)
    for nome_cenario, dados in SCENARIOS.items():
        lucro_cenario = pyo.value(m.lucro_por_cenario[nome_cenario])
        print(
            f"  {nome_cenario:6s} (p={dados['probabilidade']:.2f}): "
            f"lucro = {lucro_cenario:12,.2f}"
        )
    print(f"\n  Lucro esperado (valor otimo do SP) = {lucro_esperado:12,.2f}")
    return lucro_esperado


def valor_esperado_solucao_media(solver_name=SOLVER):
    """
    Resolve o problema deterministico usando so o cenario 'medio' (Expected
    Value problem), fixa o plantio obtido, e reavalia o lucro esperado real
    sob os 3 cenarios. Serve para calcular o VSS (Value of Stochastic
    Solution) = lucro_esperado(SP) - lucro_esperado(plantio fixado no EV).
    """
    ev_model = build_single_scenario_model("medio")
    pyo.SolverFactory(solver_name).solve(ev_model, tee=False)
    plantio_ev = {c: pyo.value(ev_model.area_plantada[c]) for c in CROPS}

    m = build_extensive_form()
    for c in CROPS:
        m.area_plantada[c].fix(plantio_ev[c])
    pyo.SolverFactory(solver_name).solve(m, tee=False)

    return plantio_ev, pyo.value(m.obj)


def valor_esperado_com_informacao_perfeita(solver_name=SOLVER):
    """
    Resolve cada cenario de forma independente (wait-and-see) e tira a
    media ponderada. Serve para calcular o EVPI (Expected Value of Perfect
    Information) = lucro_esperado(wait-and-see) - lucro_esperado(SP).
    """
    total = 0.0
    for nome_cenario, dados in SCENARIOS.items():
        sub = build_single_scenario_model(nome_cenario)
        pyo.SolverFactory(solver_name).solve(sub, tee=False)
        total += dados["probabilidade"] * pyo.value(sub.lucro)
    return total


if __name__ == "__main__":
    modelo = build_extensive_form()
    resolver(modelo)
    lucro_sp = imprimir_solucao(modelo)

    plantio_ev, lucro_ev = valor_esperado_solucao_media()
    print("\n=== Comparacao com a solucao 'Expected Value' (so cenario medio) ===")
    print(f"  Plantio EV: {plantio_ev}")
    print(f"  Lucro esperado real usando o plantio do EV: {lucro_ev:12,.2f}")
    print(f"  VSS (Value of Stochastic Solution) = {lucro_sp - lucro_ev:12,.2f}")

    lucro_ws = valor_esperado_com_informacao_perfeita()
    print("\n=== Comparacao com informacao perfeita (wait-and-see) ===")
    print(f"  Lucro esperado com informacao perfeita: {lucro_ws:12,.2f}")
    print(f"  EVPI (Expected Value of Perfect Information) = {lucro_ws - lucro_sp:12,.2f}")
