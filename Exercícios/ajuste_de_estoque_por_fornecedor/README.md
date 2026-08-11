# 📦 Ajuste de Estoque por Fornecedor — Pandas + NumPy

> "Nem todo problema pede a ferramenta mais sofisticada — às vezes a solução já está na sua mão, só falta reconhecer."

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-DataFrame-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Boolean%20Masking-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 🎯 Objetivo

Simular um cenário de loja com produtos vindos de fornecedores diferentes, cada um com seu próprio percentual de reajuste trimestral. Aplicar o reajuste correto por fornecedor e sinalizar produtos que ultrapassaram um teto de preço definido — usando uma função reutilizável com boolean masking.

Este projeto foi resolvido de forma autônoma, sem roteiro de ferramentas pré-definido: a escolha de como separar, calcular e filtrar os dados partiu de tentativa e ajuste próprios.

---

## 📐 Regra de negócio

- 6 produtos, vindos de 3 fornecedores diferentes (2 produtos por fornecedor).
- Cada fornecedor tem seu próprio percentual de reajuste trimestral.
- Após o reajuste, produtos que ultrapassam um teto de preço (definido por fornecedor) devem ser sinalizados.

---

## 🧱 Pipeline do projeto

```
┌──────────────────────────────┐
│   DataFrame de produtos        │   produtos, preço, fornecedor
└───────────────┬────────────────┘
                │  .to_numpy()
                ▼
┌──────────────────────────────┐
│   preco (array bruto)          │
└───────────────┬────────────────┘
                │  slicing por fornecedor
                ▼
┌──────────────────────────────────────────┐
│  preco_fornecedorA = preco[0:2]            │
│  preco_fornecedorB = preco[2:4]            │
│  preco_fornecedorC = preco[4:]             │
└───────────────┬────────────────────────────┘
                │  operação escalar (reajuste)
                ▼
┌──────────────────────────────────────────┐
│  reajuste_fornecedorA = preco_A * 1.08     │
│  reajuste_fornecedorB = preco_B * 1.10     │
│  reajuste_fornecedorC = preco_C * 1.09     │
└───────────────┬────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────┐
│      sinalizar_acima_teto(precos, teto)     │
│                                              │
│      filtro = precos > teto                 │
│      return precos[filtro]                  │
└──────────────────────────────────────────┘
```

---

## 🔧 Etapas realizadas

- [x] Construção do DataFrame com 6 produtos, preços e fornecedores (2 produtos por fornecedor)
- [x] Conversão da coluna `preço` para array NumPy
- [x] Separação dos preços por fornecedor via slicing
- [x] Aplicação do reajuste percentual específico de cada fornecedor (operação escalar)
- [x] Função `sinalizar_acima_teto(precos, teto)` reutilizável, aplicada aos três grupos de fornecedor

---

## 💡 Conceitos praticados

| Conceito | Onde apareceu |
|---|---|
| `.to_numpy()` | Conversão da coluna de preços |
| Slicing 1D | Separação dos preços por fornecedor |
| Operação escalar | Reajuste percentual específico por fornecedor |
| Função com parâmetros reutilizável | `sinalizar_acima_teto(precos, teto)` |
| Comparison operator + boolean masking | Identificação de preços acima do teto |

---

## 🗂️ Estrutura

```
ajuste_estoque_fornecedor_pandas_numpy/
└── ajuste_estoque_fornecedor.py
```

---

## 🚀 Próximos passos

Broadcasting consolidado → seguir para aggregate functions (axis) → filtering formal → random numbers.