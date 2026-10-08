# Problema do Jornaleiro (Newsvendor)

Exemplo introdutório de programação estocástica de 2 estágios: um
jornaleiro decide quantas revistas comprar **antes** de saber a demanda
do dia. Revistas não vendidas têm um valor residual (venda com
desconto); demanda não atendida gera uma penalidade de ruptura.

**1º estágio:** quantidade comprada (`quantidade_comprada`).
**2º estágio:** quanto é vendido, quanto sobra e quanto falta, por
cenário de demanda.

## Arquivos

- [`scenario_data.py`](scenario_data.py) — preços e os 3 cenários de
  demanda (baixa/média/alta) com suas probabilidades.
- [`reference_model.py`](reference_model.py) — mesma estrutura do
  projeto do fazendeiro, mas bem mais simples (só 3 variáveis de 2º
  estágio por cenário).
- [`solve_extensive_form.py`](solve_extensive_form.py) — monta a forma
  extensiva e calcula o EVPI.

## Rodar

```bash
pip install pyomo highspy
python solve_extensive_form.py
```

## Resultado esperado

Comprar 100 unidades, com lucro esperado de **$1.150**. Informação
perfeita sobre a demanda valeria $350 a mais por dia (EVPI).

## Para explorar

Tente mudar `CUSTO_FALTA` ou `VALOR_RESIDUAL` em `scenario_data.py` e
observe como a quantidade ótima se desloca para mais perto do cenário de
demanda alta (penalidade de falta maior) ou baixa (valor residual menor).
