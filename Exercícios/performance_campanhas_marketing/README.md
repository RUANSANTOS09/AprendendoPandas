# 📣 Performance de Campanhas de Marketing — Pandas (Melt + Pivot)

> "Quando duas métricas moram no nome da mesma coluna, separar não basta — em algum momento você precisa reuni-las de novo, lado a lado, pra fazer a conta que importa."

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Melt%20%26%20Pivot-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 🎯 Objetivo

Projeto de sábado (rotina de consolidação): organizar um relatório de campanhas de marketing recebido em formato largo — com **duas métricas diferentes** (investimento e cliques) misturadas nos nomes das colunas por mês — em uma base analítica única, calculando custo por clique e identificando campanhas com custo acima do aceitável.

Este foi o projeto mais complexo da série até o momento: exigiu corrigir de rota no meio do desenvolvimento (de duas transformações `melt` separadas e um `merge` para uma abordagem única de `melt` + `pivot_table`), além de lidar com colunas de resultado em múltiplos níveis (MultiIndex).

---

## 🧱 Pipeline do projeto

```
┌────────────────────────────────────────────┐
│  DataFrame largo                                │
│  campanha_id | canal | investimento_01-2024 |    │
│  investimento_02-2024 | investimento_03-2024 |   │
│  cliques_01-2024 | cliques_02-2024 | cliques_03-2024 │
└──────────────────────┬─────────────────────────┘
                        │  df.melt(id_vars=['campanha_id','canal'],
                        │          value_vars=[todas as 6 colunas],
                        │          var_name='metrica_mes', value_name='valor')
                        ▼
┌────────────────────────────────────────────┐
│  DataFrame longo (métrica + mês misturados)     │
│  ... | metrica_mes ('investimento_01-2024') | valor │
└──────────────────────┬─────────────────────────┘
                        │  str.rsplit('_', n=1) → metrica, mes
                        │  drop('metrica_mes')
                        ▼
┌────────────────────────────────────────────┐
│  campanha_id | canal | mes | metrica | valor    │
│  (metrica = 'investimento' ou 'cliques')         │
└──────────────────────┬─────────────────────────┘
                        │  pivot_table(index=['campanha_id','canal','mes'],
                        │              columns=['metrica'], values='valor',
                        │              aggfunc='first')
                        ▼
┌────────────────────────────────────────────┐
│  campanha_id | canal | mes | cliques | investimento │
│  (MultiIndex nas colunas: 'valor' → 'cliques'/'investimento') │
└──────────────────────┬─────────────────────────┘
                        │  custo_por_cliques = investimento / cliques
                        │  .round(2)
                        ▼
              boolean masking: custo > valor de corte
```

---

## 🔧 Etapas realizadas

- [x] Construção do relatório largo com 8 campanhas, 5 canais distintos (com repetição) e 2 métricas por mês
- [x] `melt()` único combinando as 6 colunas de investimento e cliques, evitando a necessidade de reunir dois DataFrames separados posteriormente
- [x] Separação de `metrica_mes` em `metrica` e `mes` via `str.rsplit()`
- [x] `pivot_table()` reabrindo `metrica` em colunas (`investimento`, `cliques`) lado a lado, usando `campanha_id` + `canal` + `mes` como índice composto
- [x] Cálculo de custo por clique (`investimento / cliques`) diretamente sobre colunas MultiIndex
- [x] Arredondamento para 2 casas decimais com `.round(2)`
- [x] `pivot_table()` adicional para investimento total por canal e mês (visão solicitada pela gerência)
- [x] Identificação de campanhas com custo por clique acima do valor de corte via boolean masking, preservando a linha completa

---

## 💡 Conceitos praticados

| Conceito | Aplicação |
|---|---|
| `melt()` combinando múltiplas métricas | Um único melt para colunas que misturam métrica + período no nome |
| `str.rsplit()` | Separação de string em métrica e período |
| `pivot_table()` para reabrir métricas em colunas | Reverter o achatamento do melt para permitir cálculo entre métricas na mesma linha |
| Índice composto (`index=[...]` com múltiplas colunas) | Garantir granularidade única por campanha + canal + mês |
| Colunas MultiIndex | Acesso a colunas aninhadas (`df['valor']['investimento']`) resultantes do pivot |
| `.round(n)` | Arredondamento controlado — distinção entre `.round()` (0 casas, destrutivo aqui) e `.round(2)` |
| Boolean masking sobre resultado calculado | Filtro de linhas com contexto completo a partir de uma métrica derivada |

---

## ⚠️ Erros e decisões de rota corrigidos durante o desenvolvimento

1. **Abordagem inicial descartada (dois melts + merge):** a primeira tentativa separava investimento e cliques em dois `melt()` distintos, exigindo um `merge()` posterior por `campanha_id` + mês para religar as métricas — viável, mas mais verboso. Substituída por um único `melt()` com todas as colunas, seguido de `pivot_table()` para reabrir as métricas — abordagem mais direta para colunas largas que misturam mais de uma métrica no nome.
2. **Nomenclatura de colunas enganosa:** nomear a coluna resultante do melt como `investimento` quando ela continha tanto valores de investimento quanto de cliques (antes da separação por `metrica`) — corrigido para nomes neutros (`metrica_mes`, `valor`) até a separação de fato ocorrer.
3. **Divisão invertida no custo por clique:** primeira tentativa calculava `cliques / investimento` (cliques por real, métrica inversa), corrigida para `investimento / cliques`.
4. **`KeyError` em coluna MultiIndex:** após o `pivot_table`, tentar acessar `df['investimento']` diretamente falhava porque as colunas ficaram em dois níveis (`'valor'` → `'investimento'`/`'cliques'`). Resolvido acessando o nível completo (`df['valor']['investimento']`).
5. **`.round()` sem argumento zerando a granularidade:** arredondar sem especificar casas decimais reduziu todos os valores de custo por clique a `1.0` ou `2.0`, eliminando a diferenciação entre campanhas. Corrigido com `.round(2)`.

---

## 🗂️ Estrutura

```
performance_campanhas_marketing_pandas/
└── performance_campanhas_marketing.py
```

---

## 🚀 Próximos passos

Projeto de domingo (a definir). Em paralelo: SQL Avançado (window functions, CTEs, índices, modelagem dimensional) e fechamento pendente da etapa de carga (load) do pipeline de clima no MySQL.