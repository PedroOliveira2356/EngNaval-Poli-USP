# Mecânica de Estruturas II

Análise estrutural e otimização de seções navais usando o Método dos Elementos Finitos (MEF) via scripts Python para Abaqus.

## Estrutura

```
Mecânica de Estruturas II/
├── Abaqus/
│   ├── I-beam/              — Modelo paramétrico de viga I + otimização GA
│   └── Midship section/     — Seção mestra de navio (hogging, sagging, torção)
└── Projeto Final/
    └── Abaqus modeling/     — Modelo paramétrico de seção de casco completa
```

---

## Viga I (Abaqus/I-beam)

| Arquivo | Descrição |
|---------|-----------|
| [`Ex_Model_final.py`](Abaqus/I-beam/Ex_Model_final.py) | Constrói, malea e submete automaticamente um modelo MEF paramétrico de viga I no Abaqus |
| [`GAScript_v2.py`](Abaqus/I-beam/GAScript_v2.py) | Algoritmo Genético que otimiza as dimensões da seção transversal da viga I executando análises MEF em sequência |

---

## Seção Mestra (Abaqus/Midship section)

| Arquivo | Descrição |
|---------|-----------|
| [`Model.py`](Abaqus/Midship%20section/Model.py) | Modelo MEF da seção mestra sob hogging, sagging e torção; exporta resultados para CSV |

---

## Projeto Final — Seção de Casco Paramétrica

| Arquivo | Descrição |
|---------|-----------|
| [`Projeto Final/Abaqus modeling/Model.py`](Projeto%20Final/Abaqus%20modeling/Model.py) | Geometria paramétrica de seção de casco com cavernas e longitudinais |
| [`draw.py`](Projeto%20Final/Abaqus%20modeling/draw.py) | Gera padrões de linhas estruturais ramificadas (enrijecedores T e L) ao longo de uma viga mestra |
| [`make_abaqus_file.py`](Projeto%20Final/Abaqus%20modeling/make_abaqus_file.py) | Lê `inputs.csv`, chama `draw.py` e monta o arquivo de entrada Abaqus completo |
| `inputs.csv` | Tabela de parâmetros geométricos (raios, alturas, boca) |

## Conceitos

- Modelagem programática no Abaqus (Python API)
- MEF para análise estática linear (tensão de von Mises, flambagem)
- Algoritmo Genético para otimização de seção transversal
- Seção mestra sob carregamentos globais de navio (hogging/sagging)
