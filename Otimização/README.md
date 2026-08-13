# Otimização

Disciplina de Otimização: métodos clássicos 1-D e N-D (MATLAB), programação inteira/linear com Gurobi (Python) e algoritmos evolutivos aplicados a problemas estruturais e logísticos.

## Estrutura

```
Otimização/
├── Opt_1D/          — Bisseção, Seção Áurea, Newton 1-D (MATLAB)
├── Opt_MD/          — Gradiente e Newton multi-dimensional (MATLAB)
├── Projeto Mecânico/ — Treliças 2-D/3-D, flambagem de coluna, GA (MATLAB)
├── Gurobi/          — Exemplos MIP e projetos com Gurobi (Python)
└── TF/              — Trabalho final
```

## Notebooks Python

| Arquivo | Descrição |
|---------|-----------|
| [`EP_otimiza.ipynb`](EP_otimiza.ipynb) | Estabilidade de jangada flutuante: encontra o peso W que mantém o ângulo de rolagem dentro do limite especificado |
| [`SA-Himmelblau-Function.py`](SA-Himmelblau-Function.py) | Simulated Annealing para minimização da função de Himmelblau (quatro mínimos globais) |

---

## Gurobi — Programação Inteira e Linear

| Arquivo | Descrição |
|---------|-----------|
| [`Gurobi/Aula0.ipynb`](Gurobi/Aula0.ipynb) | Introdução ao Gurobi: dois exemplos MIP binários com variáveis, objetivo e restrições |
| [`Gurobi/codigo_projeto.ipynb`](Gurobi/codigo_projeto.ipynb) | **Projeto:** escalonamento de tarefas de embarcações com janelas de tempo (MIP) — dados de Excel |
| [`Gurobi/modelo_Transportes.py`](Gurobi/modelo_Transportes.py) | Problema de transportes clássico (LP) |
| [`Gurobi/Exemplos/PNV-3321 - Ex 2 - Composição de liga.ipynb`](Gurobi/Exemplos/) | Otimização de composição de ligas metálicas (blend) |
| [`Gurobi/Exemplos/PNV-3321 - Ex 3 - Seleção de projeto.ipynb`](Gurobi/Exemplos/) | Seleção de projetos de investimento (MIP binário, orçamento multi-período) |
| [`Gurobi/Exemplos/PNV-3321 - Transporte aéreo - Parte a2.ipynb`](Gurobi/Exemplos/) | Atribuição de frota aérea a rotas (programação inteira) |
| [`Gurobi/Exemplos/airlineplanning.ipynb`](Gurobi/Exemplos/) | Re-planejamento de companhia aérea após distúrbio meteorológico |
| [`Gurobi/Exemplos/battery_scheduling.ipynb`](Gurobi/Exemplos/) | Escalonamento ótimo de carga/descarga de bateria com geração fotovoltaica |

---

## Métodos Clássicos (MATLAB)

| Pasta | Conteúdo |
|-------|----------|
| `Opt_1D/` | Bisseção, Seção Áurea e Newton para otimização escalar |
| `Opt_MD/` | Gradiente (steepest descent) e Newton N-D com busca de linha |
| `Projeto Mecânico/` | Otimização de treliça 2-D/3-D, coluna por flambagem; GA para dimensionamento de seção transversal |

## Conceitos

- Métodos de busca 1-D: bisseção, seção áurea, Newton
- Métodos N-D: gradiente, Newton, busca de linha
- Programação linear (LP) e inteira (MIP) com Gurobi
- Algoritmos Genéticos: seleção, cruzamento, mutação
- Simulated Annealing
- MEF como função de avaliação em otimização estrutural

## Bibliotecas Python

`gurobipy`, `numpy`, `matplotlib`, `scipy`, `openpyxl`
