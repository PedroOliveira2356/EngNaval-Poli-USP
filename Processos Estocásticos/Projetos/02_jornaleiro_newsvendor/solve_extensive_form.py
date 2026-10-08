"""
Resolve o problema do jornaleiro pela forma extensiva (deterministic
equivalent), igual ao projeto 01 mas com um modelo bem mais simples —
bom ponto de partida para quem esta vendo programacao estocastica de 2
estagios pela primeira vez.

Uso:
    python solve_extensive_form.py
"""

import pyomo.environ as pyo

from reference_model import build_single_scenario_model, populate_second_stage
from scenario_data import PRECO_COMPRA, SCENARIOS

SOLVER = "appsi_highs"


def build_extensive_form():
    m = pyo.ConcreteModel(name="jornaleiro_forma_extensiva")

    m.quantidade_comprada = pyo.Var(domain=pyo.NonNegativeReals)

    m.cenarios = pyo.Block(list(SCENARIOS.keys()))
    for nome_cenario in SCENARIOS:
        populate_second_stage(m.cenarios[nome_cenario], nome_cenario, m.quantidade_comprada)

    def lucro_cenario(s):
        return m.cenarios[s].receita_segundo_estagio - PRECO_COMPRA * m.quantidade_comprada

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


def imprimir_solucao(m):
    print(f"=== Quantidade a comprar (1o estagio) ===")
    print(f"  {pyo.value(m.quantidade_comprada):8.2f} unidades")

    print("\n=== Lucro esperado e por cenario ===")
    lucro_esperado = pyo.value(m.obj)
    for nome_cenario, dados in SCENARIOS.items():
        lucro_cenario = pyo.value(m.lucro_por_cenario[nome_cenario])
        print(
            f"  {nome_cenario:6s} (p={dados['probabilidade']:.2f}, "
            f"demanda={dados['demanda']:3d}): lucro = {lucro_cenario:10,.2f}"
        )
    print(f"\n  Lucro esperado (valor otimo do SP) = {lucro_esperado:10,.2f}")
    return lucro_esperado


def valor_esperado_com_informacao_perfeita(solver_name=SOLVER):
    total = 0.0
    for nome_cenario, dados in SCENARIOS.items():
        sub = build_single_scenario_model(nome_cenario)
        pyo.SolverFactory(solver_name).solve(sub, tee=False)
        total += dados["probabilidade"] * pyo.value(sub.lucro)
    return total


if __name__ == "__main__":
    modelo = build_extensive_form()
    pyo.SolverFactory(SOLVER).solve(modelo, tee=False)
    lucro_sp = imprimir_solucao(modelo)

    lucro_ws = valor_esperado_com_informacao_perfeita()
    print("\n=== Comparacao com informacao perfeita (wait-and-see) ===")
    print(f"  Lucro esperado com informacao perfeita: {lucro_ws:10,.2f}")
    print(f"  EVPI (Expected Value of Perfect Information) = {lucro_ws - lucro_sp:10,.2f}")
