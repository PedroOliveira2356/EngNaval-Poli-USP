# Otimização de Portfólio sob Retornos Incertos (CVaR)

Baseado no "Exemplo 3" de [`proc_estoc.ipynb`](../../proc_estoc.ipynb).
O notebook original para nesse exemplo antes de definir um objetivo ou
2º estágio concretos (só esboça o 1º estágio e comentários sobre
`LShapedMethod`, que também não existe mais no Pyomo). Aqui
preenchemos essa lacuna com a formulação **padrão da literatura** para
esse tipo de problema: minimização de **CVaR** (Conditional Value at
Risk) de Rockafellar & Uryasev (2000) — um programa estocástico linear
de 2 estágios, o jeito clássico de fazer alocação de portfólio sob risco
em otimização estocástica.

## Problema

Um investidor aloca `PATRIMONIO_INICIAL` entre 4 classes de ativos
(ações, títulos, ouro, FIIs) **antes** de conhecer os retornos do
próximo período. Os retornos são amostrados (2000 cenários, normal
multivariada correlacionada, seed fixa) a partir de retorno médio e
volatilidade anuais de cada ativo. A carteira deve ter retorno esperado
de pelo menos `RETORNO_MINIMO_ESPERADO`, minimizando o risco de cauda
(CVaR a 95%) em vez de maximizar o retorno médio (que levaria trivialmente
a concentrar tudo no ativo de maior retorno esperado).

**1º estágio:** pesos da carteira (`alocacao`) e o VaR auxiliar
(`zeta`), uma variável técnica da formulação de Rockafellar-Uryasev.
**2º estágio:** `excesso`, a perda de cada cenário acima do VaR — a
única variável de recurso deste problema.

## Arquivos

- [`scenario_data.py`](scenario_data.py) — parâmetros dos ativos
  (retorno médio, volatilidade, correlação) e os 2000 cenários de
  retorno amostrados.
- [`reference_model.py`](reference_model.py) — `populate_second_stage`
  monta a variável de excesso de um cenário em função da alocação e do
  zeta (ambos de 1º estágio).
- [`solve_extensive_form.py`](solve_extensive_form.py) — monta a forma
  extensiva (2000 blocos de cenário!) e resolve.

## Rodar

```bash
pip install pyomo highspy
python solve_extensive_form.py
```

## Para explorar

- Mude `ALPHA_CVAR` (ex.: 0.90 vs 0.99) para ver como a carteira fica
  mais ou menos conservadora.
- Mude `RETORNO_MINIMO_ESPERADO` para traçar a fronteira eficiente
  risco×retorno (resolva o modelo para vários valores e plote CVaR vs.
  retorno mínimo exigido).
- A correlação negativa entre ações e títulos em `CORRELACAO` é o que
  torna títulos atrativos como hedge — zere essa correlação e veja a
  alocação em títulos cair.
