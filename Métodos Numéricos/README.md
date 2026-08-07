# Métodos Numéricos

Três exercícios-programa implementando métodos numéricos fundamentais do zero (sem bibliotecas de álgebra linear de alto nível): decomposição LU, quadratura de Gauss e aproximação por mínimos quadrados.

## Conteúdo

| Arquivo | Método | Descrição |
|---------|--------|-----------|
| [`EP1/EP1.ipynb`](EP1/EP1.ipynb) | Decomposição LU | Fatoração LU com substituição direta/inversa para sistemas tridiagonais e tridiagonais cíclicos |
| [`EP2/EP2.ipynb`](EP2/EP2.ipynb) | Quadratura de Gauss | Integração numérica com 6, 8 e 10 pontos de Gauss-Legendre para funções 2-D em intervalos arbitrários |
| [`EP3/EP3.ipynb`](EP3/EP3.ipynb) | Mínimos Quadrados | Ajuste polinomial por mínimos quadrados usando base de funções ortogonais e matriz de Gram tridiagonal |

## EP1 — Decomposição LU

Implementa a fatoração $A = LU$ para matrizes esparsas tridiagonais (armazenamento compacto) e a variante cíclica (termo de canto não-nulo). Resolve sistemas com múltiplos lados direitos e valida o resultado.

## EP2 — Quadratura de Gauss

Implementa a regra de quadratura de Gauss-Legendre de n pontos com mapeamento de intervalo $[a,b] \to [-1,1]$. Compara resultados para 6, 8 e 10 pontos contra o valor exato para funções-teste polinomiais e transcendentais.

## EP3 — Mínimos Quadrados

Constrói uma base de funções ortogonais via recorrência de três termos e monta a matriz de Gram tridiagonal. Resolve o sistema com a decomposição LU do EP1 para obter os coeficientes do polinômio ajustado e calcula o erro de aproximação.

## Bibliotecas

`numpy` (apenas para arrays e plot — algoritmos implementados manualmente), `matplotlib`
