# Cálculo

Notebooks didáticos para visualização interativa dos conceitos de Cálculo I e II.

## Conteúdo

| Arquivo | Descrição |
|---------|-----------|
| [`calculo1.ipynb`](calculo1.ipynb) | Limites, derivadas (reta tangente) e integrais — funções configuráveis com NumPy, Matplotlib e SymPy |
| [`calculo2.ipynb`](calculo2.ipynb) | Cálculo em várias variáveis: superfícies, derivadas parciais, gradiente, Taylor, plano tangente, pontos críticos e Lagrange |
| [`calculo3.ipynb`](calculo3.ipynb) | Integrais múltiplas, de linha e de superfície: volume, Fubini, massa/momento de inércia, comprimento de arco, Green, trabalho conservativo, superfícies paramétricas |
| [`calculo4.ipynb`](calculo4.ipynb) | Sequências e séries, EDOs: confronto, convergência, Taylor, Fourier (fenômeno de Gibbs), Parseval, equações diferenciais de 1ª e 2ª ordem |

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

## Cálculo 3 — Integrais múltiplas, de linha e de superfície

Oito seções em 3 partes, cada uma com teoria em LaTeX e visualização (Matplotlib 3-D + Plotly interativo quando aplicável). Funções, regiões e campos são configuráveis editando as strings nas células de parâmetros.

| Parte | Seção | Tópico |
|-------|-------|--------|
| 1 | 1 | Volume de sólido por integral dupla — soma de Riemann convergindo para a integral |
| 1 | 2 | Teorema de Fubini — troca da ordem de integração (tipo I/II) |
| 1 | 3 | Massa e momento de inércia $I_0$, $I_x$, $I_y$ de uma lâmina |
| 2 | 4 | Integrais de linha e comprimento de arco |
| 2 | 5 | Teorema de Green |
| 2 | 6 | Trabalho de campo conservativo vs. não conservativo (independência do caminho) |
| 3 | 7 | Representação paramétrica de superfícies (plano, esfera, cone, toro) |
| 3 | 8 | Integrais de superfície — área e $\iint_S f\,dS$, vetor normal $\mathbf{r}_u\times\mathbf{r}_v$ |

## Cálculo 4 — Sequências, séries e equações diferenciais

Nove seções com teoria em LaTeX e visualização de convergência (Matplotlib). Funções, séries e EDOs são configuráveis editando as strings nas células de parâmetros.

| Seção | Tópico |
|-------|--------|
| 1 | Teorema do confronto |
| 2 | Séries convergentes e divergentes — somas parciais e testes de convergência |
| 3 | Sequências/séries limitadas vs. convergentes |
| 4 | Série de Taylor — aproximação por ordens crescentes |
| 5 | Série de Fourier — onda quadrada/dente de serra/triangular e fenômeno de Gibbs |
| 6 | Fórmula de Parseval — energia acumulada por harmônico |
| 7 | Equações diferenciais de 1ª ordem — campo de direções e curvas-solução |
| 8 | Equações diferenciais de 2ª ordem — oscilador harmônico e retrato de fase |

## Bibliotecas

`numpy`, `matplotlib`, `sympy`, `plotly` (opcional para gráficos interativos)
