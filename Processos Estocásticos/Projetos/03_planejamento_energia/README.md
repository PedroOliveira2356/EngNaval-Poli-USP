# Planejamento de Capacidade de Geração de Energia

Baseado no "Exemplo 2" de [`proc_estoc.ipynb`](../../proc_estoc.ipynb).
O notebook original monta o modelo usando a API do PySP
(`phsolverserver`, `PHSolverServer`, etc.) que foi **removida** do
Pyomo — esse código não roda mais. Aqui reimplementamos o mesmo problema
com a forma extensiva, como nos demais projetos desta pasta.

## Problema

Uma concessionária precisa decidir, **antes** de conhecer a demanda, a
disponibilidade eólica e os custos de combustível futuros, quanta
capacidade instalar de 4 fontes (carvão, gás, nuclear, eólica). Depois,
para cada cenário, precisa despachar a geração hora a hora (24h) para
atender a demanda ao menor custo operacional possível.

**1º estágio:** capacidade instalada de cada fonte (`capacidade`),
limitada por `CAPACIDADE_MAXIMA`, com custo `CUSTO_CAPACIDADE` ($/MW).
**2º estágio:** geração hora a hora (`geracao[g,t]`), por cenário —
restrita à capacidade instalada (e à disponibilidade eólica, no caso da
fonte eólica) e ao atendimento da demanda horária.

## Arquivos

- [`scenario_data.py`](scenario_data.py) — gera 5 cenários (seed fixa)
  de demanda horária, disponibilidade eólica horária e custo de
  combustível por fonte.
- [`reference_model.py`](reference_model.py) — `populate_second_stage`
  monta o despacho de um cenário em função de uma capacidade externa.
- [`solve_extensive_form.py`](solve_extensive_form.py) — monta a forma
  extensiva e calcula o EVPI.

## Rodar

```bash
pip install pyomo highspy
python solve_extensive_form.py
```

## Para explorar

- Aumente `N_CENARIOS` em `scenario_data.py` para ver o custo esperado
  convergir.
- Mude os `CUSTO_CAPACIDADE` para ver como o mix ótimo de fontes se
  desloca (ex.: eólica mais barata → mais capacidade instalada apesar da
  intermitência).
