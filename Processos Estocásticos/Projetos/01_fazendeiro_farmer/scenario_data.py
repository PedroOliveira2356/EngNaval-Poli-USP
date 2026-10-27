"""
Dados dos cenarios do problema do fazendeiro (Birge & Louveaux, cap. 1).

Equivale ao par ScenarioStructure.dat + ScenarioData/*.dat do PySP antigo:
aqui descrevemos a arvore de cenarios (nomes, probabilidades) e os dados
que variam por cenario (multiplicador de produtividade) em um dict Python,
que e o jeito moderno e simples de fazer isso com Pyomo puro.
"""

CROPS = ["trigo", "milho", "beterraba"]

AREA_TOTAL = 500.0  # acres disponiveis

CUSTO_PLANTIO = {  # $/acre
    "trigo": 150.0,
    "milho": 230.0,
    "beterraba": 260.0,
}

PRODUTIVIDADE_MEDIA = {  # ton/acre em um ano "medio"
    "trigo": 2.5,
    "milho": 3.0,
    "beterraba": 20.0,
}

PRECO_VENDA = {  # $/ton
    "trigo": 170.0,
    "milho": 150.0,
    "beterraba": 36.0,  # ate a cota (PRODUCAO_COTA_BETERRABA)
}

PRECO_VENDA_EXCEDENTE_BETERRABA = 10.0  # $/ton acima da cota
PRODUCAO_COTA_BETERRABA = 6000.0  # ton

PRECO_COMPRA = {  # $/ton (so trigo e milho podem ser comprados no mercado)
    "trigo": 238.0,
    "milho": 210.0,
}

CONSUMO_MINIMO = {  # ton, precisa ser alimentado ao gado ou cumprir contrato
    "trigo": 200.0,
    "milho": 240.0,
}

# Cenarios de produtividade: ruim / medio / bom, cada um com 1/3 de chance,
# multiplicando a PRODUTIVIDADE_MEDIA acima.
SCENARIOS = {
    "ruim": {"probabilidade": 1 / 3, "fator_produtividade": 0.8},
    "medio": {"probabilidade": 1 / 3, "fator_produtividade": 1.0},
    "bom": {"probabilidade": 1 / 3, "fator_produtividade": 1.2},
}


def produtividade_cenario(nome_cenario):
    fator = SCENARIOS[nome_cenario]["fator_produtividade"]
    return {cultura: PRODUTIVIDADE_MEDIA[cultura] * fator for cultura in CROPS}
