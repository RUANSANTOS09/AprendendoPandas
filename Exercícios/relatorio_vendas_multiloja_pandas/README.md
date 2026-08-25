# 🏪 Consolidação de Relatório de Vendas Multi-Loja — Pandas Avançado

> "Todo produto novo já foi vendido antes de existir no seu banco, pelo menos uma vez — é o dado sujo te avisando que algo não bate."

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Advanced-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 🎯 Objetivo

Projeto de consolidação do bloco de Pandas Avançado: transformar um relatório de vendas multi-loja de formato largo para longo, classificar produtos como "novo" ou "veterano" com base na relação entre data de cadastro e data de venda, agregar faturamento por loja/mês e identificar registros de baixo desempenho — combinando `melt()`, manipulação de datas (`.to_period()`), `apply()` multi-coluna, `groupby` multi-nível e boolean masking, todos já estudados isoladamente antes deste projeto.

---

## 🧱 Pipeline do projeto

```
┌──────────────────────────────────────────┐
│  DataFrame largo                              │
│  produto_id | loja | produtos | data_cadastro  │
│  venda_01-2024 | venda_02-2024 | venda_03-2024  │
└─────────────────────┬─────────────────────────┘
                       │  pd.melt(id_vars=[...],
                       │          var_name='relatorio_mes',
                       │          value_name='total_vendas')
                       ▼
┌──────────────────────────────────────────┐
│  DataFrame longo                              │
│  ... | relatorio_mes ('venda_01-2024') | total_vendas │
└─────────────────────┬─────────────────────────┘
                       │  str.rsplit('_', n=1) → separa mês/ano
                       │  pd.to_datetime() → data_venda real
                       ▼
┌──────────────────────────────────────────┐
│  classificar_produto(data_cadastro, data_venda) │
│                                                │
│  d1 = data_cadastro.to_period('M')             │
│  d2 = data_venda.to_period('M')                │
│  diff = (d2 - d1).n                            │
│  0 <= diff <= 3  → 'Novo'                      │
│  caso contrário  → 'veterano'                  │
└─────────────────────┬─────────────────────────┘
                       │
          ┌────────────┴─────────────┐
          ▼                          ▼
groupby(['loja','data_venda'])   boolean masking
['total_vendas'].sum()            total_vendas < mínimo definido
```

---

## 🔧 Etapas realizadas

- [x] Transformação do relatório de largo para longo com `pd.melt()`
- [x] Separação de `relatorio_mes` (`'venda_01-2024'`) em componentes de data via `str.rsplit()`
- [x] Conversão de `data_cadastro` e `data_venda` para datetime real
- [x] Função `classificar_produto()` comparando períodos mensais (`.to_period('M')`) entre cadastro e venda
- [x] Aplicação da classificação por linha com `.apply(..., axis=1)`, extraindo colunas específicas via lambda
- [x] Faturamento total por loja e por mês via `groupby()` multi-nível
- [x] Identificação de registros com venda abaixo de um valor mínimo via boolean masking, preservando o contexto completo da linha

---

## 💡 Conceitos praticados

| Conceito | Aplicação |
|---|---|
| `pd.melt()` | Formato largo → longo, mantendo múltiplas colunas fixas (`id_vars`) |
| `str.rsplit()` | Separação de string com múltiplos delimitadores em componentes de data |
| `.to_period('M')` | Comparação de datas por mês/ano, ignorando o dia |
| Subtração de `Period` e extração via `.n` | Diferença em número de meses entre dois períodos |
| `.apply(..., axis=1)` com lambda | Passagem de múltiplas colunas específicas para uma função customizada |
| `groupby()` multi-nível | Agregação por duas dimensões (`loja` + `data_venda`) |
| Boolean masking com contexto completo | Filtro que preserva todas as colunas da linha, não apenas o valor |

---

## ⚠️ Erros e inconsistências resolvidos durante o desenvolvimento

1. **Dados de cadastro fora do período de venda:** a primeira versão do dataset tinha produtos cadastrados em meses fora do intervalo de vendas simuladas (ex: cadastro em julho, vendas de janeiro a março), gerando inconsistência de negócio. Ajustado para que todas as datas de cadastro caíssem dentro do período analisado.
2. **`TypeError` na subtração de `Period`:** `(d2 - d1)` retornava um objeto `MonthEnd`, não um inteiro, quebrando a comparação `<= 3`. Resolvido extraindo o valor numérico com `.n`.
3. **Diferença negativa classificada como "Novo":** a condição `sub.n <= 3` não excluía valores negativos (venda registrada antes do cadastro), classificando incorretamente esses casos como "Novo". Corrigido com a condição composta `0 <= sub.n <= 3`, que também expôs uma inconsistência real nos dados simulados (venda antes do cadastro).
4. **`.dt` usado incorretamente em valores únicos:** dentro da função aplicada linha a linha, `.dt` foi usado por engano em um `Timestamp` isolado (o acessor `.dt` só funciona sobre uma coluna/Series inteira). Corrigido removendo o `.dt` dentro da função.
5. **`apply()` em seleção de colunas sem lambda:** tentativa inicial de aplicar a função diretamente sobre uma seleção de colunas (`df[['a','b']].apply(funcao, axis=1)`) passava a linha inteira como um único argumento, incompatível com uma função de dois parâmetros. Resolvido com `df.apply(lambda x: funcao(x['a'], x['b']), axis=1)`.

---

## 🗂️ Estrutura

```
relatorio_vendas_multiloja_pandas/
└── relatorio_vendas_multiloja.py
```

---

## 🚀 Próximos passos

`pivot_table()` (operação inversa ao `melt`, ainda não estudada) → fechar a etapa de carga (load) do pipeline de clima no MySQL → SQL Avançado.