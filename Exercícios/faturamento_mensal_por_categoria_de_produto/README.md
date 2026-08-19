# 🔄 Faturamento Mensal por Categoria — Pandas (melt)

> "Dado largo é bom pra planilha de humano ler; dado longo é bom pra máquina agregar. `melt()` é a ponte entre os dois mundos."

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Melt%20%26%20Reshape-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 🎯 Objetivo

Transformar um relatório de faturamento em formato largo (uma coluna por mês, comum em planilhas exportadas de sistemas legados) em formato longo, adequado para agregação e análise — aplicando `pd.melt()` em um cenário próprio, diferente do exemplo original visto em aula, para validar a generalização do conceito.

---

## 🧱 Pipeline do projeto

```
┌───────────────────────────────────────┐
│  DataFrame largo                          │
│  produto_id | categoria | faturamento_01-2024 │
│              | faturamento_02-2024 | faturamento_03-2024
└─────────────────┬───────────────────────────┘
                   │  pd.melt(id_vars=['produto_id','categoria'],
                   │          var_name='mes', value_name='valor')
                   ▼
┌───────────────────────────────────────┐
│  DataFrame longo                          │
│  produto_id | categoria | mes | valor       │
│  mes = 'faturamento_01-2024'                │
└─────────────────┬───────────────────────────┘
                   │  .str.replace('faturamento_', '')
                   │  .str.split('-', expand=True) → mes, ano
                   ▼
┌───────────────────────────────────────┐
│  produto_id | categoria | mes | ano | valor │
└─────────────────┬───────────────────────────┘
                   │
        ┌──────────┴──────────────┐
        ▼                         ▼
groupby(['categoria','mes'])   boolean masking
['valor'].sum()                 valor < mínimo definido
```

---

## 🔧 Etapas realizadas

- [x] Construção de DataFrame largo com 6 categorias e faturamento em 3 meses
- [x] Transformação para formato longo com `pd.melt()`
- [x] Separação da coluna `mes` (originalmente `'faturamento_01-2024'`) em mês e ano, resolvendo o desafio de múltiplos delimitadores na mesma string
- [x] Cálculo do faturamento total por categoria e mês com `groupby()` multi-nível
- [x] Identificação de registros individuais abaixo de um valor mínimo via comparison operator + boolean masking aplicado ao DataFrame completo (não apenas à coluna de valor)

---

## 💡 Conceitos praticados

| Conceito | Aplicação |
|---|---|
| `pd.melt()` | Conversão de formato largo (uma coluna por mês) para longo (uma linha por mês) |
| `id_vars` / `value_vars` / `var_name` / `value_name` | Controle de quais colunas ficam fixas e como as novas colunas são nomeadas |
| Manipulação de string em múltiplas etapas | Remoção de prefixo (`replace`) seguida de split, para lidar com string com mais de um padrão de delimitador |
| `groupby()` multi-nível | Agregação por duas colunas simultaneamente (`categoria` + `mes`) |
| Boolean masking em DataFrame completo | Diferença entre filtrar uma coluna isolada e filtrar linhas completas com contexto |

---

## ⚠️ Ponto de atenção resolvido durante o desenvolvimento

A string original da coluna de mês (`'faturamento_01-2024'`) possui dois delimitadores diferentes (`_` e `-`), mas apenas um estava sendo usado no primeiro split (`rsplit('-', n=1)`), o que deixava o texto `"faturamento_01"` misturado ao invés de separar mês, ano e o prefixo de forma limpa. Resolvido com uma remoção de prefixo (`str.replace`) antes do split por `-`.

---

## 🗂️ Estrutura

```
faturamento_mensal_melt_pandas/
└── faturamento_mensal_melt.py
```

---

## 🚀 Próximos passos

Seguir Pandas Avançado: `pivot_table()` (operação inversa ao melt) → trabalho com datas via `.dt` → `apply()`/`map()`. Em paralelo, retomar e fechar a etapa de carga (load) do pipeline de clima no MySQL.