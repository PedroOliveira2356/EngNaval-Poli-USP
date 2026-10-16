# Resolução — Estimativa da Resistência ao Avanço (Método de Froude / ITTC-1957)

Este documento explica, passo a passo, a resolução implementada em [`exercicio.ipynb`](exercicio.ipynb), incluindo tanto a parte que já estava pronta no notebook quanto as correções e etapas adicionadas para fechar o exercício.

## 1. Enunciado — dados fornecidos

**Navio (escala real):**
- DWT total = 9.000 t
- Velocidade de serviço Vs = 14,0 nós
- Coeficiente DWT/Deslocamento: C_DWT = 0,69
- Água do mar a 19 °C: ρ = 1,025 t/m³, ν = 1,07854×10⁻⁶ m²/s

**Modelo (tanque de provas):**
- LPP = 4,6 m
- L/B = 6,3
- CB = 0,82
- S = 5,5041 m² (área molhada)
- ∇ = 0,8758 m³ (volume deslocado)
- Ct (ensaiado) = 0,006110
- Água doce a 17 °C: ρ = 0,9987 t/m³, ν = 1,08155×10⁻⁶ m²/s

**Pede-se:** Cf, Cr, Ct e Ca do navio e do modelo, e a resistência total ao avanço do navio em escala real, pelo método de extrapolação de Froude com a correção ITTC-1957:

- Linha de correlação ITTC-1957 para o atrito: `Cf = 0,075 / (log10(Re) − 2)²`
- Decomposição ITTC-1957: `Ct_navio = Cr + Cf_navio + Ca`

## 2. Fundamento teórico (método de Froude)

A ideia central do método de Froude é que a resistência total se decompõe em duas parcelas de naturezas físicas distintas, que escalam de formas diferentes entre modelo e navio:

- **Resistência de atrito (Cf):** depende do número de Reynolds (efeitos viscosos). Como modelo e navio não podem ter Re igual (não é possível respeitar Froude e Reynolds simultaneamente num mesmo fluido), o Cf é calculado separadamente para cada um, usando a linha de correlação ITTC-1957.
- **Resistência residual (Cr):** dominada pela geração de ondas, governada pelo número de Froude (Fn = V/√(gL)). O ensaio é conduzido de forma que o modelo navegue no **mesmo Fn do navio**; nessa condição, assume-se que **Cr é igual para modelo e navio** (hipótese de Froude).
- **Coeficiente de correlação (Ca):** um termo empírico de correção que contabiliza efeitos não capturados pela extrapolação pura (rugosidade do casco real, efeitos de escala adicionais etc.). Aplica-se apenas ao navio em escala real, nunca ao modelo.

Logo, o procedimento é:
1. Obter `Ct` do ensaio do modelo (dado).
2. Calcular `Cf` do modelo (via Re do modelo) e isolar `Cr = Ct_modelo − Cf_modelo`.
3. Transferir esse `Cr` diretamente para o navio (mesmo Fn).
4. Calcular `Cf` do navio (via Re do navio, em escala real).
5. Obter `Ca` do navio por uma curva/tabela empírica em função do deslocamento.
6. Somar: `Ct_navio = Cr + Cf_navio + Ca`.
7. Converter `Ct_navio` em força de resistência: `Rt = Ct · ½ρV²S`.

---

# Resolução — Parte a)

## 3. Etapas da resolução

### 3.1 Função de atrito ITTC-1957 (`078e470d`)
```python
def Cf(Rex):
    return 0.075 / (np.log10(Rex) - 2) ** 2
```
Implementa diretamente a linha de correlação dada no enunciado.

### 3.2 Dicionários de dados do navio e do modelo (`e6e69924`, `9a737739`)
Guardam os dados brutos do enunciado em dois dicionários Python (`ship` e `model`), e já calculam:
- `Delta` (deslocamento do navio) = DWT / C_DWT = 9000 / 0,69 ≈ 13.043,5 t
- `Vd` (volume deslocado do navio) = Delta / ρ_navio ≈ 12.725,3 m³

### 3.3 Fator de escala geométrica (`3f7134a5`)
```python
F_scale = (ship["Vd"] / model["Vd"])**(1/3)
```
Como os volumes deslocados escalam com o cubo da razão de escala linear, inverte-se a relação para obter o fator de escala λ a partir dos volumes:
`λ = (∇_navio / ∇_modelo)^(1/3) ≈ 24,40`

### 3.4 Comprimento do navio e número de Reynolds do navio (`c789243c`)
```python
ship["LBP"] = model["LBP"]*F_scale
ship["Re"] = ship["rho"]*ship["Vs"]*ship["LBP"]/ship["mu"]
```
O LBP do navio é obtido escalando o LBP do modelo por λ. O Reynolds do navio usa a velocidade real de serviço (convertida de nós para m/s em `ship["Vs"]`).

### 3.5 Velocidade e Reynolds do modelo (`bc8072cd`)
```python
model["Vs"] = ship["Vs"] * np.sqrt(model["LBP"] / ship["LBP"])
model["Re"] = model["rho"]*model["Vs"]*model["LBP"]/model["mu"]
```
Aplica a **similaridade de Froude**: para que Fn seja igual entre modelo e navio, a velocidade do modelo deve ser `Vs_modelo = Vs_navio · √(L_modelo/L_navio)`. Com essa velocidade, calcula-se o Re do modelo.

### 3.6 Coeficientes de atrito Cf do navio e do modelo (`f03ba28d`)
```python
ship["Cf"] = Cf(ship["Re"])
model["Cf"] = Cf(model["Re"])
```
Aplica a função ITTC-1957 aos dois números de Reynolds calculados.

### 3.7 Cr do modelo, transferido para o navio (nova célula `3271175e`)
```python
model["Cr"] = model["Ct"] - model["Cf"]
ship["Cr"] = model["Cr"]
```
Isola o `Cr` a partir do `Ct` ensaiado do modelo e o atribui ao navio (hipótese de Froude: mesmo Fn → mesmo Cr).

Resultado: `Cr = 0,0028437` (igual para modelo e navio).

### 3.8 Ca do navio e do modelo (célula `5b7105fe`, ajustada)
```python
x = [1e3, 1e4, 1e5, 1e6]
y = [6e-4, 4e-4, 0.0, -6e-4]
x_interp = ship["Delta"]
ship["Ca"] = np.interp(x_interp, x, y)
model["Ca"] = 0.0
```
`Ca` é lido por interpolação linear numa curva empírica (tabela ITTC de correlação) em função do deslocamento do navio (≈13.043,5 t, entre os pontos 10⁴ e 10⁵ t). Foi adicionado explicitamente `model["Ca"] = 0.0`, pois esse coeficiente de correlação modelo-navio não se aplica ao próprio modelo.

Resultado: `Ca_navio = 0,0003865`.

### 3.9 Ct do navio (célula `fe456608`, corrigida)
```python
ship["Ct"] = ship["Cr"] + ship["Cf"] + ship["Ca"]
```
Agora monta corretamente o `Ct` do navio pela soma ITTC-1957, usando o `Cr` herdado do modelo, o `Cf` do navio (já calculado em escala real) e o `Ca`.

Resultado: `Ct_navio = 0,0048121`.

### 3.10 Área molhada do navio em escala real (nova célula `d4ad25d6`)
```python
ship["S"] = model["S"] * F_scale**2
```
A área molhada escala com o quadrado do fator de escala linear (grandeza de área).

Resultado: `S_navio ≈ 3.277,4 m²`.

### 3.11 Resistência total ao avanço do navio (nova célula `93e1a451`)
```python
ship["Rt"] = ship["Ct"] * 0.5 * (ship["rho"]*1000) * ship["Vs"]**2 * ship["S"]
```
Aplica a definição do coeficiente de resistência total, `Ct = Rt / (½ρV²S)`, isolando `Rt`. A densidade é convertida de t/m³ para kg/m³ (×1000) para que o resultado saia em Newtons.

Resultado: **Rt ≈ 419,2 kN**.

## 4. Tabela-resumo dos resultados

| Grandeza | Modelo | Navio |
|---|---|---|
| L [m] | 4,6 | 112,25 |
| V [m/s] | 1,4579 | 7,2016 (14,0 nós) |
| Re | 6,19×10⁶ | 7,68×10⁸ |
| Cf | 0,003266 | 0,001582 |
| Cr | 0,002844 | 0,002844 |
| Ca | 0 (não se aplica) | 0,000386 |
| Ct | 0,006110 (ensaiado) | 0,004812 (extrapolado) |

- Fator de escala: λ ≈ 24,40
- Área molhada do navio: S ≈ 3.277,4 m²
- **Resistência total ao avanço do navio: Rt ≈ 419,2 kN**

## 5. Interpretação física do resultado

O `Ct` do navio (0,004812) é **menor** que o `Ct` do modelo (0,006110), o que é esperado: o `Cf` cai fortemente com o aumento de escala (Re muito maior no navio reduz a contribuição relativa do atrito viscoso), enquanto o `Cr` (efeito de ondas, dominante em escala real para a maioria dos cascos nessa faixa de Froude) permanece igual. O `Ca` soma um pequeno acréscimo para compensar efeitos de rugosidade e outros fatores de escala não capturados pela extrapolação pura de Froude.

---

# Resolução — Parte b) Método ITTC-1978

Esta segunda resolução trata do item (b) do enunciado: a reestimativa da resistência do navio pelo **método ITTC-1978**, que refina o método de Froude/ITTC-1957 ao introduzir o **fator de forma (k)** e uma nova fórmula (Townsin) para o coeficiente de correlação `Ca`. Implementada nas novas células do mesmo notebook [`exercicio.ipynb`](exercicio.ipynb), reaproveitando os dicionários `ship` e `model` já calculados na parte (a).

## 6. Enunciado — dados adicionais da parte (b)

- Decomposição conceitual ITTC-1978: `Ct = (1 + k)·Cf + Cw`, em que `k` é o **fator de forma** do casco (efeito tridimensional sobre o atrito, que a placa plana de Froude/ITTC-1957 não capturava) e `Cw` é o coeficiente de resistência de geração de ondas (quem antes se chamava `Cr`, mas agora isolado do efeito de forma).
- Fórmula de Townsin (ITTC-1978) para o coeficiente de correlação:
  `10³·Ca = 44·[(h/L)^(1/3) − 10·Re^(−1/3)] + 0,125`
  onde `h` é a rugosidade média aparente do casco (adotado o valor padrão `h = 150 μm`, pois não foi informado).
- Ensaio extra do modelo a **Fn = 0,1** (velocidade baixa, onde a resistência de ondas é desprezível): `Ct_modelo(Fn=0,1) = 0,004487`.

## 7. Fundamento teórico (método ITTC-1978)

A principal mudança conceitual em relação ao método de Froude (parte a) é **não tratar mais o atrito como o de uma placa plana equivalente**: em um casco real, a curvatura e a forma tridimensional aumentam o atrito viscoso em relação à placa plana lisa de mesmo comprimento e Reynolds. Esse acréscimo é capturado pelo **fator de forma `k`**, multiplicando o `Cf` de placa plana: `(1+k)·Cf`.

Como `k` é um efeito puramente viscoso (geométrico, independente de Fn), ele pode ser determinado isoladamente em um ensaio a **Fn muito baixo**, onde a resistência de ondas `Cw` é desprezível:

`Ct_modelo(Fn baixo) ≈ (1+k)·Cf_modelo(Fn baixo)  ⟹  k = Ct_modelo(Fn baixo)/Cf_modelo(Fn baixo) − 1`

Uma vez obtido `k` (admitido igual para modelo e navio — é geométrico, não depende da escala nem da velocidade), ele é usado para isolar `Cw` a partir do ensaio principal do modelo (no Fn de serviço, o mesmo usado na parte a):

`Cw = Ct_modelo(Fn serviço) − (1+k)·Cf_modelo(Fn serviço)`

Por hipótese de Froude, `Cw` (resistência de ondas) **não depende de escala** para o mesmo número de Froude, logo é transferido diretamente para o navio. O `Ca` deixa de ser lido de uma curva genérica em função do deslocamento (como na parte a) e passa a ser calculado pela **fórmula de Townsin**, em função da rugosidade do casco e do Reynolds do próprio navio. Por fim:

`Ct_navio = (1+k)·Cf_navio + Cw + Ca`

## 8. Etapas da resolução (novas células do notebook)

### 8.1 Condição do ensaio extra a Fn = 0,1 (célula `0bc70666`)
```python
ittc1978 = {"h": 150e-6}
ittc1978["Fn_k"] = 0.1
ittc1978["V_model_k"] = ittc1978["Fn_k"] * np.sqrt(g * model["LBP"])
ittc1978["Re_model_k"] = model["rho"] * ittc1978["V_model_k"] * model["LBP"] / model["mu"]
ittc1978["Cf_model_k"] = Cf(ittc1978["Re_model_k"])
ittc1978["Ct_model_k"] = 0.004487
```
A velocidade do modelo nesse ensaio extra é obtida isolando `V` da definição de Froude, `Fn = V/√(g·L)`, com `L` do modelo (o mesmo LBP = 4,6 m já usado na parte a). Com essa velocidade calcula-se `Re` e, pela mesma linha de correlação ITTC-1957 (`Cf`), o atrito de placa plana equivalente nessa condição.

Resultado: `V_modelo(Fn=0,1) ≈ 0,6718 m/s`, `Re ≈ 2,853×10⁶`, `Cf ≈ 0,0037783`.

### 8.2 Fator de forma k (célula `dfe9caa0`)
```python
ittc1978["k"] = ittc1978["Ct_model_k"] / ittc1978["Cf_model_k"] - 1
```
Como a Fn=0,1 a resistência de ondas é desprezível, todo o `Ct` ensaiado é atribuído ao atrito corrigido pela forma: `k = Ct/Cf − 1`.

Resultado: **k ≈ 0,1876**.

### 8.3 Coeficiente de onda Cw (célula `f6ddded6`)
```python
ittc1978["Cw"] = model["Ct"] - (1 + ittc1978["k"]) * model["Cf"]
```
Usa o `Ct` e o `Cf` do ensaio **principal** do modelo (mesmo Fn de serviço do navio, já calculados na parte a: `model["Ct"] = 0,00611`, `model["Cf"] = 0,0032663`), descontando agora o atrito já corrigido pelo fator de forma `(1+k)`.

Resultado: **Cw ≈ 0,0022311** (igual para modelo e navio, por hipótese de Froude).

### 8.4 Coeficiente de correlação Ca pela fórmula de Townsin (célula `f23d3582`)
```python
ittc1978["Ca_ship"] = (44 * ((ittc1978["h"] / ship["LBP"]) ** (1/3)
                              - 10 * ship["Re"] ** (-1/3)) + 0.125) * 1e-3
```
Aplica a fórmula de Townsin diretamente para o navio, usando a rugosidade padrão `h = 150 μm`, o comprimento do navio (`ship["LBP"] ≈ 112,25 m`, calculado na parte a) e o Reynolds do navio em serviço (`ship["Re"] ≈ 7,68×10⁸`, também da parte a).

Resultado: **Ca ≈ 0,0001292** — bem menor que o `Ca ≈ 0,0003865` obtido na parte (a) pela curva genérica em função do deslocamento, pois a fórmula de Townsin é mais específica (depende da rugosidade real do casco, não de uma tendência estatística por porte do navio).

### 8.5 Ct do navio pelo método ITTC-1978 (célula `e068bcda`)
```python
ittc1978["Ct_ship"] = (1 + ittc1978["k"]) * ship["Cf"] + ittc1978["Cw"] + ittc1978["Ca_ship"]
```
Monta o `Ct` do navio somando o atrito já corrigido pela forma, a resistência de ondas e a correlação de Townsin.

Resultado: **Ct_navio (ITTC-1978) ≈ 0,0042390**.

### 8.6 Resistência total pelo método ITTC-1978 (célula `62578644`)
```python
ittc1978["Rt"] = ittc1978["Ct_ship"] * 0.5 * (ship["rho"]*1000) * ship["Vs"]**2 * ship["S"]
```
Mesma definição de `Ct = Rt/(½ρV²S)` usada na parte (a), reaproveitando `ship["Vs"]` e a área molhada `ship["S"]` já calculadas.

Resultado: **Rt (ITTC-1978) ≈ 369,27 kN**.

### 8.7 Comparação entre os métodos (célula `5f8029ae`)
```python
print(f"Ct_navio Froude/ITTC-1957: {ship['Ct']:.6f}  ->  Rt = {ship['Rt']/1000:.2f} kN")
print(f"Ct_navio ITTC-1978:        {ittc1978['Ct_ship']:.6f}  ->  Rt = {ittc1978['Rt']/1000:.2f} kN")
print(f"Diferenca relativa: {(ittc1978['Rt']-ship['Rt'])/ship['Rt']*100:.2f} %")
```

## 9. Tabela-resumo dos resultados (parte b)

| Grandeza | Valor |
|---|---|
| V_modelo a Fn=0,1 | 0,6718 m/s |
| Re_modelo a Fn=0,1 | 2,853×10⁶ |
| Cf_modelo a Fn=0,1 | 0,0037783 |
| Ct_modelo a Fn=0,1 (ensaiado) | 0,004487 |
| **Fator de forma k** | **0,1876** |
| **Cw** (modelo = navio) | **0,0022311** |
| h (rugosidade padrão) | 150 μm |
| **Ca do navio** (Townsin) | **0,0001292** |
| **Ct do navio** (ITTC-1978) | **0,0042390** |
| **Rt do navio** (ITTC-1978) | **≈ 369,27 kN** |

## 10. Comparação entre os métodos e explicação técnica das diferenças

| Método | Ct do navio | Rt do navio |
|---|---|---|
| Froude / ITTC-1957 (parte a) | 0,004812 | ≈ 419,2 kN |
| ITTC-1978 (parte b) | 0,004239 | ≈ 369,3 kN |
| Diferença | — | **≈ −11,9 %** |

O método ITTC-1978 resultou numa resistência **cerca de 12 % menor** que o método de Froude/ITTC-1957. As causas técnicas dessa diferença são:

1. **Separação do efeito de forma (k):** no método de 1957, todo o efeito tridimensional do casco (forma) ficava implicitamente misturado dentro do `Cr` (chamado "resistência residual"), que incluía tanto resistência de ondas quanto o excesso de atrito viscoso devido à forma do casco. No método de 1978, esse excesso de atrito é isolado em `(1+k)` e aplicado sobre o `Cf` de placa plana — um tratamento fisicamente mais correto, pois `k` não depende de Fn nem de escala, enquanto a resistência de ondas (`Cw`) sim. Com a decomposição mais refinada, menos resistência de atrito "vaza" para dentro do termo que é extrapolado como se fosse puramente de onda, mudando o balanço final.
2. **Novo cálculo do `Ca`:** na parte (a), o `Ca` veio de uma curva genérica (função apenas do deslocamento do navio), que é uma estimativa grosseira e tende a ser conservadora (valor maior: 0,000386). Na parte (b), a fórmula de Townsin calcula o `Ca` a partir da rugosidade real do casco e do Reynolds do navio, resultando em um valor bem menor (0,000129) para um casco "liso" (h = 150 μm padrão). Essa redução de quase 0,00026 no `Ca` já responde por boa parte da queda do `Ct` total.
3. **Consistência física:** o método ITTC-1978 é considerado mais preciso porque usa um ensaio extra dedicado (baixo Fn) para separar fisicamente dois fenômenos (atrito viscoso tridimensional vs. geração de ondas) que o método de Froude agrupava em um único coeficiente `Cr`. Isso reduz a dependência de curvas empíricas genéricas (como a de `Ca` em função do deslocamento) e torna a extrapolação modelo-navio mais robusta, especialmente para navios com formas de casco muito diferentes da média histórica usada para construir aquela curva genérica.

Em suma, a diferença entre os dois métodos não é um erro, mas reflete a evolução da modelagem física da resistência: o método de 1978 é mais detalhado e, para este casco, indica uma resistência real provavelmente mais próxima de ≈369 kN do que de ≈419 kN estimados pelo método mais simples de 1957.
