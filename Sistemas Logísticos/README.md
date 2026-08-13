# Sistemas Logísticos

Três atividades de roteamento de veículos com complexidade crescente: do CVRP clássico ao VRPTW com instâncias de benchmark Solomon.

## Conteúdo

| Arquivo | Problema | Abordagem |
|---------|----------|-----------|
| [`Tarefa 1/Ex1.ipynb`](Tarefa%201/Ex1.ipynb) | CVRP — Capacitated VRP | Google OR-Tools com matriz de distâncias a partir de coordenadas |
| [`Tarefa 2/Ex2.ipynb`](Tarefa%202/Ex2.ipynb) | VRP com heurística | Heurística de economias Clarke-Wright |
| [`Tarefa 3/Ex3.ipynb`](Tarefa%203/Ex3.ipynb) | VRPTW — VRP com Janelas de Tempo | Heurística de inserção de Solomon (paralela) |

---

## Tarefa 1 — CVRP com OR-Tools

Lê coordenadas e demandas de clientes de `dadosEx1.xlsx`, monta a matriz de distâncias euclidianas, define a capacidade dos veículos e resolve o CVRP com o solver de roteamento do Google OR-Tools. Exibe as rotas otimizadas e a distância total.

## Tarefa 2 — Heurística de Clarke-Wright

Implementa o algoritmo de economias de Clarke-Wright: calcula a economia $s_{ij} = d_{0i} + d_{0j} - d_{ij}$ para cada par de clientes, ordena as economias em ordem decrescente e funde rotas enquanto a capacidade permitir. Dados em `dadosEx2.xlsx`.

## Tarefa 3 — VRPTW com Inserção de Solomon

Lê a instância benchmark Solomon `R111.txt` (100 clientes com janelas de tempo e demandas), implementa a heurística de inserção paralela de Solomon e gera rotas viáveis respeitando capacidade e janelas de tempo. Execução paralela via `concurrent.futures`.

## Conceitos

- Problema de Roteamento de Veículos com Capacidade (CVRP)
- Heurística construtiva de economias (Clarke-Wright, 1964)
- VRPTW: restrições de janelas de tempo [a, b] por cliente
- Heurística de inserção de Solomon (I1): critério de inserção de menor custo
- Instâncias de benchmark Solomon (classe R1)

## Bibliotecas

`ortools`, `numpy`, `pandas`, `matplotlib`, `openpyxl`, `concurrent.futures`
