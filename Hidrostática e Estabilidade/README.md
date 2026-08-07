# Hidrostática e Estabilidade

Exercício-programa da disciplina PNV3315: cálculo das propriedades hidrostáticas de um navio a partir da tabela de balizas (body plan), usando método dos painéis e interpolação por splines cúbicas.

## Conteúdo

| Arquivo | Descrição |
|---------|-----------|
| [`EP_PNV3315.ipynb`](EP_PNV3315.ipynb) | Cálculo de volume deslocado, centro de carena, momento de inércia da linha d'água, KB, BM, KM e curvas hidrostáticas |
| `Tabela_de_cotas.xlsx` | Tabela de cotas (offsets) do navio — entrada de dados para o notebook |
| `PNV3315_2022_Relatório_Grupo_5.pdf` | Relatório entregue (PDF) |

## Metodologia

1. **Interpolação de balizas** — splines cúbicas nas direções transversal e longitudinal para refinamento da malha de offsets (`interpolaColunas`, `interpolaLinhas`, `nInterpolaAmbos`)
2. **Integração por painéis** — integração numérica das áreas de seção transversal ao longo do comprimento para obter volume deslocado ($\nabla$), centroide vertical ($K\!B$) e área da linha d'água ($A_W$)
3. **Parâmetros metacêntricos** — $BM_T$, $BM_L$, $KM_T$, $KM_L$ para cada calado
4. **Curvas hidrostáticas** — variação de $\nabla$, $KB$, $KM$, $A_W$, $LCB$ e $LCF$ em função do calado

## Bibliotecas

`numpy`, `scipy` (interpolação), `matplotlib`
