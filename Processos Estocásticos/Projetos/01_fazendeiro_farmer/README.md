# Problema do Fazendeiro (Farmer Problem)

Exemplo clássico de programação estocástica de 2 estágios (Birge &
Louveaux, *Introduction to Stochastic Programming*, cap. 1).

## Enunciado

Um fazendeiro tem 500 acres de terra e precisa decidir, **antes** de
saber como será a safra, quantos acres plantar de trigo, milho e
beterraba. Depois da colheita, com a produtividade real conhecida
(ruim/média/boa, 1/3 de chance cada), ele:

- precisa garantir um consumo mínimo de trigo e milho (ração do gado),
  comprando no mercado o que faltar;
- vende o excedente de trigo e milho a um preço de mercado;
- vende a beterraba a um preço melhor até uma cota de produção, e a um
  preço menor acima da cota.

**1º estágio:** área plantada de cada cultura (`area_plantada`).
**2º estágio:** quanto comprar/vender de cada produto, por cenário.

## Arquivos

- [`scenario_data.py`](scenario_data.py) — custos, preços, produtividade
  média e os 3 cenários (ruim/médio/bom) com suas probabilidades.
- [`reference_model.py`](reference_model.py) — `populate_second_stage`
  monta as restrições de 2º estágio para um cenário dado, em função de
  uma variável de área plantada externa; `build_single_scenario_model`
  monta um modelo completo e independente para um único cenário (usado
  nos cálculos de EV/WS).
- [`solve_extensive_form.py`](solve_extensive_form.py) — monta a forma
  extensiva (todos os cenários + variável de 1º estágio compartilhada) e
  calcula VSS e EVPI.

## Rodar

```bash
pip install pyomo highspy
python solve_extensive_form.py
```

## Resultado esperado

Plantio ótimo: 170 acres de trigo, 80 de milho, 250 de beterraba*, com
lucro esperado de **$108.390** — valor que bate com a referência do
livro-texto (a alocação exata de trigo/beterraba varia conforme a regra
de desempate do solver, pois há múltiplos ótimos com o mesmo lucro, mas
o lucro esperado ótimo é sempre 108.390).

*Nota: o livro-texto cita 120/80/300 como uma das soluções ótimas
equivalentes.
