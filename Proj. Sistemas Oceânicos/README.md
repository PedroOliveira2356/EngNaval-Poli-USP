# Projeto de Sistemas Oceânicos

Projeto de otimização de plataforma semi-submersível para produção offshore, com análises hidrostáticas, de pesos e hidrodinâmicas integradas em um modelo orientado a objetos.

## Conteúdo

| Arquivo | Descrição |
|---------|-----------|
| [`semi-sub.ipynb`](semi-sub.ipynb) | Versão procedural: funções independentes para hidrostática, pesos/estabilidade e RAO de heave; otimização por amostragem aleatória com busca de Pareto |
| [`new_semi-sub.ipynb`](new_semi-sub.ipynb) | **Versão OOP:** classe `SemiSub` com métodos encapsulados; otimização via Evolução Diferencial (`scipy`) |
| [`catenaria.ipynb`](catenaria.ipynb) | Cálculo de linha de ancoragem catenária: tensão, ponto de toque e força restauradora em função da carga ambiental horizontal |

---

## Classe `SemiSub` (`new_semi-sub.ipynb`)

A plataforma é modelada por seis parâmetros geométricos: comprimento dos pontoons ($L_P$), largura dos pontoons ($B_P$), altura dos pontoons ($H_P$), largura das colunas ($B_C$), altura das colunas ($H_C$) e calado ($T$).

```python
plat = SemiSub(LP=170, BP=40, HP=20, BC=23, HC=60, T=35)
plat.hidrostat(visual=True)   # KM, deslocamento
plat.pesos(visual=True)       # GM, airgap, peso do casco
plat.rao(visual=True)         # Tn, RAO de heave, cruzamento JONSWAP
plat.avaliar(ger=0, visual=2) # análise completa
```

### Métodos

| Método | Retorno | Descrição |
|--------|---------|-----------|
| `hidrostat(visual)` | `(KM, D)` | Volume deslocado, KB, BM, KM, deslocamento |
| `pesos(boe, visual)` | `dict` | Pesos de topside, casco, lastro, risers; GM e airgap |
| `rao(ger, zeta, visual)` | `(Tn, airgap_calc, Hs_resp)` | Forças FK, massa adicional, RAO, cruzamento JONSWAP |
| `avaliar(ger, visual)` | — | Executa os três métodos acima em sequência |

---

## Otimização por Evolução Diferencial

A função `otimizar(base, ger)` usa `scipy.optimize.differential_evolution` para minimizar o **peso do casco** sujeito a restrições de projeto:

| Restrição | Critério |
|-----------|---------|
| Estabilidade | $1 \le GM \le 4$ m |
| Dinâmica | $T_n > 20$ s |
| Lastro | $V_{\text{lastro}} \le 0{,}9 \cdot V_{\text{pontoons}}$ |
| Airgap | airgap estrutural > airgap mínimo pelo RAO |
| Geometria | $H_P < T < H_P + H_C$ |
| Deck | $A_{\text{topside}} \le L_P^2$ |

A cada geração, o raio de busca se reduz por $\text{amplitude} = \max(0{,}05,\; 1/(g+1))$.

---

## Sistema de Ancoragem (`catenaria.ipynb`)

Análise da linha de ancoragem catenária considerando peso por unidade de comprimento, comprimento total e carga horizontal aplicada pela plataforma. Calcula a variação de tensão de topo, ponto de toque no fundo e curva de restauração do sistema de amarração.

## Bibliotecas

`numpy`, `scipy` (`differential_evolution`), `matplotlib`
