# Hidrodinâmica

Exercícios e projetos das disciplinas de Hidrodinâmica I (propulsores) e Hidrodinâmica II (fluxo potencial, RAOs, plataformas offshore).

## Estrutura

```
Hidrodinâmica/
├── Hidro I/          — Teoria de elemento de pá, propulsor NACA 4412
├── Hidro II/         — Fluxo potencial 2-D, RAOs, estudo de caso SPAR
│   ├── Estudo de caso - SPAR/
│   └── Arquivos MATLAB/
```

---

## Hidro I — Propulsores

| Arquivo | Descrição |
|---------|-----------|
| [`Hidro I/model_prop.ipynb`](Hidro%20I/model_prop.ipynb) | Análise de desempenho de propulsor 4 pás NACA 4412: empuxo e torque via Blade Element / Actuator Disk Theory |

Lê coeficientes de sustentação e arrasto (Cl, Cd) de `coef.txt` para cada ângulo de ataque e integra ao longo das pás para obter empuxo total e eficiência propulsiva.

---

## Hidro II — Ondas e Fluxo Potencial

| Arquivo | Descrição |
|---------|-----------|
| [`Hidro II/Exercícios_slides.ipynb`](Hidro%20II/Exercícios_slides.ipynb) | Escoamentos potenciais 2-D: linhas de corrente para fonte, sumidouro, vórtice e superposições |
| `Hidro II/Arquivos MATLAB/` | Scripts de exercícios sobre escoamento potencial (`potential_flow.m`) e RAOs de navio (`RAOs.m`, `AirgapRAO.m`) |

---

## Estudo de Caso — Plataforma SPAR

| Arquivo | Descrição |
|---------|-----------|
| [`Hidro II/Estudo de caso - SPAR/Caso_SPAR.ipynb`](Hidro%20II/Estudo%20de%20caso%20-%20SPAR/Caso_SPAR.ipynb) | Análise completa de plataforma SPAR: RAOs do WAMIT, verificação Morison, espectros de resposta em surge/heave/pitch e cargas extremas |

O notebook lê RAOs numéricos do WAMIT a partir de `RAOs SPAR WAMIT.xlsx`, valida a aplicabilidade da equação de Morison (razão D/λ), calcula os espectros de resposta via cruzamento espectral com JONSWAP e estima os valores extremos de esforços.

## Conceitos

- Teoria de Elemento de Pá (BET) e disco atuador
- Escoamento potencial: fonte, sumidouro, vórtice, cilindro com circulação
- RAOs de plataforma (heave, surge, pitch) via WAMIT
- Equação de Morison e critério de difração
- Cruzamento espectral para resposta em mar irregular

## Bibliotecas

`numpy`, `matplotlib`, `scipy`, `openpyxl`
