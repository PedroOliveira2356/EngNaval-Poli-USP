# Projetos de Programação Estocástica

### O que é Programação Estocástica?
- Otimização com parâmetros incertos
- Decisões em múltiplos estágios
- Cenários para representar a incerteza
- **Decisões aqui-e-agora** vs **decisions wait-and-see**

### Tipos de Problemas que PySP aborda:
1. **Two-stage stochastic programming** (2-SP)
2. **Multi-stage stochastic programming** (M-SP)
3. **Chance-constrained programming**
4. **Robust optimization** (até certo ponto)
5. **Stochastic dynamic programming**

Projetos completos de programação estocástica de dois estágios em Pyomo.
O problema do fazendeiro (projeto 01) é um clássico adicional da literatura, incluído como primeiro exemplo didático.

> **Nota sobre PySP:** o notebook introduz o PySP (`ReferenceModel.py` +
> `ScenarioStructure.dat` + `ScenarioData/*.dat` + `runph.py` rodando
> Progressive Hedging). O PySP foi **descontinuado** e removido do Pyomo
> moderno — o sucessor oficial é o pacote [`mpi-sppy`](https://github.com/Pyomo/mpi-sppy).
> Os projetos abaixo seguem a mesma ideia conceitual (modelo de
> referência + dados por cenário), mas usando Pyomo puro e resolvendo o
> problema pela **forma extensiva** (deterministic equivalent): um único
> modelo com uma variável de 1º estágio compartilhada entre cópias das
> restrições de 2º estágio, uma por cenário. Isso é exato e simples de
> entender; vale a pena migrar para `mpi-sppy` (ou Progressive Hedging)
> apenas quando o número de cenários fica grande demais para caber na
> forma extensiva.

## Projetos

| Pasta | Problema | Nível |
|---|---|---|
| [`01_fazendeiro_farmer/`](01_fazendeiro_farmer/) | Problema do fazendeiro (Birge & Louveaux) — decidir área plantada de 3 culturas antes de saber a produtividade da safra | Intermediário (3 cenários, recurso com compra/venda e faixas de preço) |
| [`02_jornaleiro_newsvendor/`](02_jornaleiro_newsvendor/) | Newsvendor — decidir quanto comprar antes de saber a demanda | Introdutório (3 cenários, recurso simples) |
| [`03_planejamento_energia/`](03_planejamento_energia/) | Planejamento de capacidade de geração — investir em 4 fontes antes de saber demanda/vento/custo de combustível | Intermediário (5 cenários, despacho horário em 24 períodos) |
| [`04_portfolio_financeiro/`](04_portfolio_financeiro/) | Otimização de portfólio sob retornos incertos — minimização de CVaR (Rockafellar-Uryasev) | Avançado (2000 cenários amostrados, retornos correlacionados) |

## Estrutura de cada projeto

```
projeto/
├── scenario_data.py          # dados determinísticos + cenários e probabilidades
├── reference_model.py        # variáveis/restrições de 2o estágio (função de "populate_second_stage")
├── solve_extensive_form.py   # monta a forma extensiva e resolve (+ métricas EVPI/VSS)
└── ScenarioData/              # reservado para dados externos por cenário, se desejar
```

## Como rodar

Requer `pyomo` e um solver de PL. É usado o solver livre **HiGHS**
(pacote `highspy`, sem necessidade de licença); o projeto já roda com
`appsi_highs`. Se preferir o Gurobi (já listado no `requirements.txt` do
repositório), troque a constante `SOLVER` no topo de cada
`solve_extensive_form.py` para `"gurobi"`.

```bash
pip install pyomo highspy
cd 01_fazendeiro_farmer
python solve_extensive_form.py
```

## Conceitos cobertos

- **Forma extensiva (deterministic equivalent):** uma única instância
  Pyomo com variáveis de 1º estágio compartilhadas e um bloco de
  variáveis/restrições de 2º estágio por cenário.
- **Não-antecipatividade:** garantida "by construction" ao usar a mesma
  variável de 1º estágio em todos os blocos de cenário, em vez de
  variáveis duplicadas ligadas por restrições extras.
- **EV (Expected Value problem):** resolver só com o cenário médio e
  avaliar o plano resultante contra todos os cenários.
- **VSS (Value of Stochastic Solution):** quanto se ganha por resolver o
  problema estocástico em vez de usar o plano do EV.
- **WS (Wait-and-See):** resolver cada cenário separadamente, como se a
  incerteza fosse revelada antes da decisão.
- **EVPI (Expected Value of Perfect Information):** quanto valeria saber
  o cenário com antecedência (WS − SP).
