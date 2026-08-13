# Dinâmica de Sistemas II

Análise dinâmica de sistemas navais e oceânicos: espectros de ondas, RAOs, pêndulo duplo e séries temporais experimentais.

## Conteúdo

| Arquivo | Descrição |
|---------|-----------|
| [`Cruzamento_espectral.ipynb`](Cruzamento_espectral.ipynb) | Espectro JONSWAP × RAO de heave → espectro de resposta; séries temporais e verificação via FFT |
| [`Exemplo_FFT_onda_regular.ipynb`](Exemplo_FFT_onda_regular.ipynb) | DFT de onda regular: conversão do domínio do tempo para o de frequência com `scipy.fft` |
| [`Exercicio_Semi-sub.ipynb`](Exercicio_Semi-sub.ipynb) | Períodos naturais de heave, roll e pitch de plataforma semi-submersível via massa adicional e inércia |
| `EDOs.ipynb` | Placeholder (arquivo vazio) |
| [`Trabalho 1/T1.ipynb`](Trabalho%201/T1.ipynb) | Pêndulo duplo: formulação Lagrangeana (SymPy), integração RK4 (`odeint`) e animação em GIF |
| [`Trabalho 2/T2.ipynb`](Trabalho%202/T2.ipynb) | RAO experimental via FFT/Welch em dados de tanque de provas; comparação com modelo analítico e cruzamento com JONSWAP |

## Trabalho 1 — Pêndulo Duplo

Derivação simbólica das equações de Euler-Lagrange com SymPy, conversão para funções numéricas com `lambdify`, integração de Runge-Kutta via `scipy.integrate.odeint` e animação do movimento caótico.

## Trabalho 2 — RAO Experimental

Carregamento de séries temporais de onda e heave a partir de planilha Excel (`grupo08.xlsx`), cálculo do espectro por FFT e estimativa de Welch, obtenção do RAO experimental $\sqrt{S_{\text{heave}}/S_{\text{onda}}}$, e cruzamento espectral com JONSWAP para estimativa da resposta em mar irregular.

## Conceitos

- Espectro JONSWAP (Hs, Tp, γ)
- Cruzamento espectral: $S_{\text{resp}}(\omega) = [\text{RAO}(\omega)]^2 \cdot S(\omega)$
- Momentos espectrais m₀, m₁, m₂, m₄ e períodos característicos
- Forças de Froude-Krylov em pontoons e colunas

## Bibliotecas

`numpy`, `scipy`, `matplotlib`, `sympy`, `openpyxl`
