# 📊 Extrato de Vendas — Pandas + NumPy

> "Dados limpos não nascem limpos — são o resultado de um processo deliberado de verificação, tratamento e validação."

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Array%20Slicing-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 🎯 Objetivo

Projeto de treino integrando dois pilares do ecossistema de dados em Python:

1. **Pandas** para limpeza de dados brutos (duplicatas e valores nulos)
2. **NumPy** para manipulação do array resultante via slicing multidimensional

Simula um cenário comum de engenharia de dados: uma ingestão crua de vendas chega com problemas de qualidade e precisa ser tratada antes de virar dado confiável.

---

## 🧱 Pipeline do projeto

```
┌─────────────────────┐
│  DataFrame bruto     │   6 linhas | 1 duplicata | 2 nulos (produto)
│  (id, produto, qtd,  │
│   preco)             │
└──────────┬───────────┘
           │
           ▼
┌─────────────────────┐
│  Tratamento Pandas   │   drop_duplicates() → 5 linhas
│                       │   dropna() em 'produto' → 3 linhas
└──────────┬───────────┘
           │
           ▼
┌─────────────────────┐
│  df.to_numpy()        │   DataFrame limpo → array NumPy
└──────────┬───────────┘
           │
           ▼
┌─────────────────────────────────────────────┐
│              Slicing NumPy                    │
│                                                │
│  coluna 'preco'      → array[:, 3:]           │
│  3 primeiras linhas  → array[0:3, :]          │
│  'quantidade'+'preco'→ array[:, 2:]           │
└─────────────────────────────────────────────┘
```

---

## 🔧 Etapas realizadas

### Bloco Pandas
- [x] Construção do DataFrame de vendas com sujeira proposital (duplicata + nulos)
- [x] Auditoria de duplicatas com `.duplicated()`
- [x] Remoção de duplicatas com `drop_duplicates()`
- [x] Auditoria de nulos com `.isna().sum()`
- [x] Tratamento de nulos (remoção da linha, por se tratar de coluna categórica sem valor substituível)

### Bloco NumPy
- [x] Conversão do DataFrame limpo para array com `.to_numpy()`
- [x] Slicing vertical — extração da coluna `preco`
- [x] Slicing horizontal — extração das 3 primeiras linhas completas
- [x] Slicing combinado — extração das colunas `quantidade` e `preco` juntas

---

## 💡 Conceitos praticados

| Conceito | Onde apareceu |
|---|---|
| `.duplicated()` / `drop_duplicates()` | Auditoria e remoção de duplicatas |
| `.isna().sum()` | Diagnóstico de nulos por coluna |
| Decisão de estratégia para nulo categórico | Drop em vez de imputação |
| `.to_numpy()` | Ponte entre Pandas e NumPy |
| Slicing 2D (`array[linhas, colunas]`) | Recortes vertical, horizontal e combinado |

---

## 🗂️ Estrutura

```
extrato_vendas_pandas_numpy/
└── extrato_vendas.py
```

---

## 🚀 Próximos passos

Seguir o roadmap de NumPy: arithmetic → broadcasting → aggregate functions (axis) → filtering (boolean masking).