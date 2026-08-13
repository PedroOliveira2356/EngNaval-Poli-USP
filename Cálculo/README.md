# Cálculo

Notebooks didáticos para visualização interativa dos conceitos de Cálculo I e II.

## Conteúdo

| Arquivo | Descrição |
|---------|-----------|
| [`calculo1.ipynb`](calculo1.ipynb) | Limites, derivadas (reta tangente) e integrais — funções configuráveis com NumPy, Matplotlib e SymPy |
| [`calculo2.ipynb`](calculo2.ipynb) | Cálculo em várias variáveis: superfícies, derivadas parciais, gradiente, Taylor, plano tangente, pontos críticos e Lagrange |

## Cálculo 1 — Funções de uma variável

- Cálculo de limites com avaliação simbólica (SymPy)
- Derivação numérica e simbólica, visualização da reta tangente
- Integração numérica com representação gráfica da área sob a curva
- Sólido de revolução: volume por integração e visualização 3-D

## Cálculo 2 — Funções de várias variáveis

Sete seções, cada uma com visualizações geradas por Matplotlib (3-D estático) e Plotly (3-D interativo para rotação). A função padrão é `x**2 - y**2` (sela), mas qualquer expressão em `x` e `y` pode ser usada editando `expr_str` na célula de configuração.

| Seção | Tópico |
|-------|--------|
| 1 | Superfícies e curvas de nível |
| 2 | Derivadas parciais e diferenciabilidade |
| 3 | Vetor gradiente e campo de direções |
| 4 | Polinômio de Taylor de 2ª ordem e erro de aproximação |
| 5 | Plano tangente e derivada direcional em função do ângulo |
| 6 | Classificação de pontos críticos via discriminante $D = f_{xx}f_{yy} - f_{xy}^2$ |
| 7 | Máximos e mínimos com restrições — Multiplicadores de Lagrange |

## Bibliotecas

`numpy`, `matplotlib`, `sympy`, `plotly` (opcional para gráficos interativos)
