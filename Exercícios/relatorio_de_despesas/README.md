# 🔁 Melt + Pivot Table — Relatório de Despesas por Departamento

> "Melt organiza pra você auditar linha a linha. Pivot table reorganiza pra quem só quer ver o resumo. O dado é o mesmo — só muda pra quem você está falando."

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Melt%20%26%20Pivot-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 🎯 Objetivo

Exercícios de fixação (rotina de sábado) combinando `melt()` e `pivot_table()` — operações inversas — em um cenário coerente de negócio: um relatório de despesas por departamento chega em formato largo (uma coluna por mês), é organizado em formato longo para auditoria, e depois reorganizado em uma nova visão (categoria de despesa x mês) via pivot table.

---

## 🧱 Pipeline dos exercícios

```
┌─────────────────────────────────────┐
│  DataFrame largo                        │
│  departamento | categoria_despesa |      │
│  despesa_01-2024 | despesa_02-2024 |     │
│  despesa_03-2024                         │
└─────────────────┬─────────────────────────┘
                   │  df.melt(id_vars=['departamento','categoria_despesa'],
                   │          var_name='mes_despesa', value_name='valor_despesa')
                   ▼
┌─────────────────────────────────────┐
│  DataFrame longo                        │
│  ... | mes_despesa ('despesa_01-2024')   │
└─────────────────┬─────────────────────────┘
                   │  str.rsplit('_', n=1) → separa prefixo/mês-ano
                   │  pd.to_datetime() → mês como data real
                   │  .dt.month_name(locale='pt_BR.UTF-8') → nome do mês em português
                   ▼
┌─────────────────────────────────────┐
│  df_melt.pivot_table(                    │
│      index=['categoria_despesa'],        │
│      columns=['mes'],                    │
│      values='valor_despesa',             │
│      aggfunc='sum')                      │
└─────────────────────────────────────┘
```

---

## 🔧 Etapas realizadas

- [x] Construção de relatório de despesas largo, com 6 departamentos e 3 meses
- [x] Transformação para formato longo com `melt()`
- [x] Separação da coluna de mês via `str.rsplit()`, remoção do prefixo textual
- [x] Conversão para datetime e extração do nome do mês em português com `.dt.month_name(locale='pt_BR.UTF-8')`
- [x] Reorganização em `pivot_table()`: categoria de despesa nas linhas, mês nas colunas, soma como agregação

---

## 💡 Conceitos praticados

| Conceito | Aplicação |
|---|---|
| `melt()` | Formato largo → longo, preservando `departamento` e `categoria_despesa` fixos |
| `str.rsplit()` | Separação de string composta em duas partes |
| `.dt.month_name(locale=...)` | Extração do nome do mês por extenso, em português |
| `pivot_table()` | Reorganização de longo → largo, com agregação por `aggfunc='sum'` |

---

## ⚠️ Observação técnica

As colunas de mês no resultado do `pivot_table` saíram em ordem alfabética (Fevereiro, Janeiro, Março), não cronológica. Isso ocorre porque a coluna de mês foi convertida para nome textual antes da pivotagem — o Pandas ordena colunas de texto alfabeticamente por padrão. Para manter ordem cronológica, seria necessário pivotar mantendo o mês como número, ou reordenar as colunas manualmente após o pivot.

---

## 🗂️ Estrutura

```
melt_pivot_despesas_exercicios/
└── melt_pivot_despesas.py
```

---

## 🚀 Próximos passos

Consolidar o conceito no projeto de sábado, combinando melt + pivot_table em um cenário maior e mais completo.