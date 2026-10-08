"""
Dados do problema do jornaleiro (newsvendor), um exemplo introdutorio de
programacao estocastica de 2 estagios: so uma decisao de 1o estagio
(quantidade a comprar) e uma unica fonte de incerteza (demanda).
"""

PRECO_COMPRA = 10.0  # $/unidade, pago antes de conhecer a demanda
PRECO_VENDA = 25.0  # $/unidade vendida
VALOR_RESIDUAL = 2.0  # $/unidade, sobra vendida com desconto (salvage value)
CUSTO_FALTA = 5.0  # $/unidade de demanda nao atendida (penalidade de ruptura)

# Cenarios discretos de demanda, cada um com sua probabilidade.
SCENARIOS = {
    "baixa": {"probabilidade": 0.25, "demanda": 50},
    "media": {"probabilidade": 0.50, "demanda": 100},
    "alta": {"probabilidade": 0.25, "demanda": 150},
}
