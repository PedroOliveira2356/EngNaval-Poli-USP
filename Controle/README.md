# Sistemas de Controle

Projeto de controladores para veículo autônomo subaquático (AUV) LAUV, com modelagem dinâmica, análise de estabilidade e síntese de controladores clássicos.

## Conteúdo

| Arquivo | Descrição |
|---------|-----------|
| [`Projeto_LAUV.ipynb`](Projeto_LAUV.ipynb) | Modelagem e controle do LAUV: alocação de polos (controle de profundidade) e controle proporcional de rumo |
| `Listas_exs/` | Scripts MATLAB de exercícios sobre resposta temporal de sistemas de 1ª ordem |

## Projeto LAUV

O notebook cobre o ciclo completo de projeto:

1. **Modelagem** — equações de movimento linearizadas para os modos de profundidade e rumo
2. **Análise** — resposta em frequência, diagrama de Bode, margem de estabilidade
3. **Síntese** — projeto por alocação de polos para o controlador de profundidade; controlador P para rumo
4. **Validação** — simulação da resposta ao degrau com `scipy.signal` e `control`

## Bibliotecas

`control`, `scipy`, `sympy`, `numpy`, `matplotlib`
