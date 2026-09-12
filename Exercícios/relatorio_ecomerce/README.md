# 📊 Análise de Vendas — Exercício Pandas

> "Não são os dados que mentem, é a pergunta que você esqueceu de fazer."

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

## 📌 Sobre

Exercício de consolidação em Pandas: análise de um pequeno dataset de vendas cobrindo criação de colunas derivadas, agregações por categoria e por período temporal, e identificação de máximos de forma programática.

## 🗂️ Estrutura dos Dados

```
produto | categoria | quantidade | preco_unitario | data_venda
```

## 🔍 O que foi feito

```
┌─────────────────────┐
│   DataFrame bruto    │
└──────────┬───────────┘
           │
           ▼
┌─────────────────────┐
│ valor_total =        │
│ quantidade × preço   │
└──────────┬───────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
┌─────────┐ ┌──────────────┐
│ Produto │ │ Faturamento  │
│ de maior│ │ por categoria│
│faturam. │ │  (groupby)   │
└─────────┘ └──────────────┘
           │
           ▼
┌─────────────────────┐
│ data_venda → datetime│
│ extração do mês (.dt)│
└──────────┬───────────┘
           │
           ▼
┌─────────────────────┐
│ Faturamento por mês  │
│ + idxmax() → mês top │
└─────────────────────┘
```

## 🛠️ Conceitos aplicados

- Criação de coluna derivada (`quantidade * preco_unitario`)
- Máscara booleana para localizar o valor máximo de uma coluna
- `groupby()` + `sum()` para agregação por categoria e por mês
- `pd.to_datetime()` para conversão de strings para datetime
- Acesso `.dt.month` para extração de componentes de data
- `idxmax()` para obter o índice do maior valor de uma Series sem inspeção manual

## 📈 Resultado

O mês de **janeiro** apresentou o maior faturamento agregado, identificado via `idxmax()` sobre o agrupamento mensal.

## ▶️ Como rodar

```bash
pip install pandas
jupyter notebook analise_vendas.ipynb
```