# Métodos Numéricos

Três exercícios-programa implementando métodos numéricos fundamentais do zero (sem bibliotecas de álgebra linear de alto nível): decomposição LU, quadratura de Gauss e aproximação por mínimos quadrados. Além dos EPs, a pasta `Aulas/` reúne notebooks de apoio ao estudo, com teoria, implementação e visualizações didáticas de todos os tópicos da disciplina.

## Conteúdo

| Arquivo | Método | Descrição |
|---------|--------|-----------|
| [`EP1/EP1.ipynb`](EP1/EP1.ipynb) | Decomposição LU | Fatoração LU com substituição direta/inversa para sistemas tridiagonais e tridiagonais cíclicos |
| [`EP2/EP2.ipynb`](EP2/EP2.ipynb) | Quadratura de Gauss | Integração numérica com 6, 8 e 10 pontos de Gauss-Legendre para funções 2-D em intervalos arbitrários |
| [`EP3/EP3.ipynb`](EP3/EP3.ipynb) | Mínimos Quadrados | Ajuste polinomial por mínimos quadrados usando base de funções ortogonais e matriz de Gram tridiagonal |
| [`Aulas/01_Zeros_de_Funcoes.ipynb`](Aulas/01_Zeros_de_Funcoes.ipynb) | Zeros de funções | TVM/Bolzano, dicotomia, falsa posição, Newton-Raphson (precisão pré-fixada) e ponto fixo, com animações passo a passo e comparação de convergência |
| [`Aulas/02_Sistemas_Lineares.ipynb`](Aulas/02_Sistemas_Lineares.ipynb) | Sistemas lineares | Eliminação de Gauss com pivoteamento parcial, Gauss-Seidel, Jacobi e análise de convergência (dominância diagonal, raio espectral) |
| [`Aulas/03_MMQ.ipynb`](Aulas/03_MMQ.ipynb) | Mínimos quadrados | Ajuste polinomial, polinômios de Legendre (ortogonalidade e condicionamento) e análise harmônica (séries de Fourier, fenômeno de Gibbs) |
| [`Aulas/04_Interpolacao.ipynb`](Aulas/04_Interpolacao.ipynb) | Interpolação | Polinômio interpolador nas formas de Lagrange e Newton (diferenças divididas), erro de truncamento e fenômeno de Runge (nós equiespaçados vs. Chebyshev) |
| [`Aulas/05_Integracao_Numerica.ipynb`](Aulas/05_Integracao_Numerica.ipynb) | Integração numérica | Soma de Riemann, regra dos Trapézios e de Simpson repetidas, com verificação numérica da ordem de convergência $O(h^2)$/$O(h^4)$ |
| [`Aulas/formulário.pdf`](Aulas/formulário.pdf) | — | Formulário oficial da disciplina (fórmulas transcritas e usadas nos notebooks de MMQ, Interpolação e Integração Numérica) |

## EP1 — Decomposição LU

Implementa a fatoração $A = LU$ para matrizes esparsas tridiagonais (armazenamento compacto) e a variante cíclica (termo de canto não-nulo). Resolve sistemas com múltiplos lados direitos e valida o resultado.

## EP2 — Quadratura de Gauss

Implementa a regra de quadratura de Gauss-Legendre de n pontos com mapeamento de intervalo $[a,b] \to [-1,1]$. Compara resultados para 6, 8 e 10 pontos contra o valor exato para funções-teste polinomiais e transcendentais.

## EP3 — Mínimos Quadrados

Constrói uma base de funções ortogonais via recorrência de três termos e monta a matriz de Gram tridiagonal. Resolve o sistema com a decomposição LU do EP1 para obter os coeficientes do polinômio ajustado e calcula o erro de aproximação.

## Aulas — notebooks de apoio ao estudo

Material didático complementar, organizado por tópico da ementa. Cada notebook traz a teoria (com as fórmulas relevantes, incluindo as do `formulário.pdf` quando aplicável), implementação dos métodos do zero e visualizações pensadas para construir intuição — não apenas reproduzir os resultados.

### `01_Zeros_de_Funcoes.ipynb`

Teorema do Valor Médio e de Bolzano, método da dicotomia, método da falsa posição, método de Newton (com critério de parada por precisão pré-fixada e demonstração da convergência quadrática) e método das aproximações sucessivas (ponto fixo, com os clássicos gráficos de "teia de aranha"). Fecha com uma comparação direta de velocidade de convergência entre todos os métodos no mesmo problema.

### `02_Sistemas_Lineares.ipynb`

Eliminação de Gauss com pivoteamento parcial (com heatmap mostrando o escalonamento passo a passo e um exemplo da instabilidade numérica sem pivoteamento), método de Gauss-Seidel (com visualização da trajetória de convergência) e análise de convergência via dominância diagonal e raio espectral da matriz de iteração. Inclui também Jacobi como comparação extra.

### `03_MMQ.ipynb`

Ajuste polinomial por mínimos quadrados resolvendo o sistema normal do zero, construção de bases ortogonais com os polinômios de Legendre (com verificação numérica da ortogonalidade e comparação de condicionamento de matriz), e análise harmônica (coeficientes de Fourier, convergência da série truncada e o fenômeno de Gibbs em funções descontínuas).

### `04_Interpolacao.ipynb`

Polinômio interpolador nas formas de Lagrange e de Newton (diferenças divididas), com verificação de que ambas produzem o mesmo polinômio, erro de truncamento teórico vs. real, e o fenômeno de Runge — contrastando nós igualmente espaçados com nós de Chebyshev.

### `05_Integracao_Numerica.ipynb`

Da soma de Riemann às regras dos Trapézios e de Simpson (repetidas), com visualização geométrica de cada aproximação e verificação numérica das ordens de convergência $O(h^2)$ e $O(h^4)$ previstas na teoria.

### `formulário.pdf`

Formulário oficial fornecido na disciplina, usado como referência para as fórmulas transcritas nos notebooks acima.

## Bibliotecas

`numpy` (apenas para arrays e plot — algoritmos implementados manualmente), `matplotlib`
