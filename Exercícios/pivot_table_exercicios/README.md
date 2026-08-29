# 🔀 Exercícios de `pivot_table()` — Pandas

> "`pivot()` reorganiza; `pivot_table()` reorganiza e agrega. A diferença é sutil no nome e decisiva na prática — a segunda não quebra quando os dados se repetem."

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Pivot%20Table-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 🎯 Objetivo

Fixar `pivot_table()` — a operação inversa ao `melt()` — através de dois exercícios curtos, praticando a diferença entre `pivot()` (quebra com duplicata) e `pivot_table()` (agrega automaticamente), e a troca do parâmetro `aggfunc` conforme a pergunta de negócio.

---

## 📐 Exercícios

### 1. Vendedores por mês (soma)

DataFrame com `vendedor`, `mes`, `valor_vendido`, incluindo um vendedor com duas vendas no mesmo mês (forçando agregação). `pivot_table()` com vendedores nas linhas, meses nas colunas, `aggfunc='sum'`.

```python
df_pivot_table = df.pivot_table(
    index=['vendedor'],
    columns=['mes'],
    values=['valor_vendido'],
    aggfunc='sum'
)
```

Resultado esperado: vendedor com duas vendas no mesmo mês exibe a soma combinada; demais células mostram o valor individual ou `NaN` quando não há venda naquele mês.

### 2. Ocupação hoteleira por tipo de quarto e dia da semana (média)

DataFrame com `tipo_quarto`, `dia_semana`, `reservas`, incluindo duas combinações repetidas (mesmo tipo de quarto no mesmo dia, simulando reservas em turnos diferentes). `pivot_table()` com tipo de quarto nas linhas, dia da semana nas colunas, `aggfunc='mean'`.

```python
df_pivot_table = df.pivot_table(
    index=['tipo_quarto'],
    columns=['dia_semana'],
    values=['reservas'],
    aggfunc='mean'
)
```

Resultado esperado: combinações repetidas exibem a média dos valores agregados; demais células mostram o valor individual.

---

## 💡 Conceitos praticados

| Conceito | Aplicação |
|---|---|
| `pivot()` vs `pivot_table()` | `pivot()` quebra com valores duplicados; `pivot_table()` agrega automaticamente via `aggfunc` |
| `pivot_table(index, columns, values, aggfunc)` | Reorganização de formato longo para largo com agregação embutida |
| Troca de `aggfunc` (`'sum'` → `'mean'`) | Adaptar a agregação à pergunta de negócio (total vs média) |
| Equivalência com `groupby` + `unstack` | `pivot_table` combina o que `groupby` (agregação) e reformatação fariam em duas etapas separadas |

---

## ⚠️ Ponto de atenção no design dos dados

Nas duas tentativas iniciais de montar os datasets, as combinações de índice/coluna não tinham repetição real (mesmo `tipo_quarto` aparecendo em dias diferentes, não no mesmo dia), o que não força agregação alguma — cada célula do pivot teria apenas um valor, sem testar de fato o `aggfunc`. Corrigido garantindo ao menos duas combinações idênticas de índice+coluna em cada exercício.

---

## 🗂️ Estrutura

```
pivot_table_exercicios/
└── pivot_table_exercicios.py
```

---

## 🚀 Próximos passos

Bloco de Pandas Avançado concluído (groupby, melt, `.dt`, apply, pivot_table). Seguir para SQL Avançado, ou fechar a etapa de carga (load) pendente do pipeline de clima no MySQL.