# 📈 Análise de Desempenho de Vendedores — NumPy

> "Uma função de agregação resume os dados — mas resumir sem saber ao longo de qual eixo é resumir errado."

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Aggregate%20Functions-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 🎯 Objetivo

Analisar uma matriz de vendas (vendedores x meses) usando funções de agregação do NumPy, praticando o controle do parâmetro `axis` para resumir dados por linha ou por coluna, e localizando o valor máximo em coordenadas reais de matriz (não em índice achatado).

---

## 🧱 Estrutura dos dados

```
vendas (shape 4x3) — 4 vendedores, 3 meses

           mês1   mês2   mês3
vendedor1  3000   1000   5000
vendedor2  1500    900   1900
vendedor3  2367   4998   1150
vendedor4  9455   3988   3010
```

---

## 🔧 Etapas realizadas

| Etapa | Pergunta de negócio | Função usada |
|---|---|---|
| 1 | Montagem da matriz de vendas | `np.array()` |
| 2 | Total vendido por vendedor (somando os 3 meses) | `np.sum(vendas, axis=1)` |
| 3 | Total vendido pela empresa em cada mês | `np.sum(vendas, axis=0)` |
| 4 | Maior venda individual e sua posição exata (vendedor, mês) | `np.argmax()` + `np.unravel_index()` |
| 5 | Média de vendas de cada mês | `np.mean(vendas, axis=0)` |

---

## 💡 Conceitos praticados

| Conceito | Aplicação |
|---|---|
| `axis=0` vs `axis=1` | Resumir por coluna (mês) vs por linha (vendedor) |
| `np.argmax()` | Localizar o índice do maior valor no array achatado |
| `np.unravel_index()` | Converter índice achatado em coordenadas reais (linha, coluna) |
| Conversão de `np.int64` para `int` | Output limpo, sem ruído de tipo NumPy no `print()` |

---

## ⚠️ Detalhe técnico resolvido

`np.argmax()` sozinho retorna a posição do maior valor como se a matriz fosse uma sequência 1D "achatada" — não como coordenada de linha/coluna. Para obter a posição real (ex: vendedor 4, mês 1), foi necessário combinar com `np.unravel_index(indice, shape)`, passando o shape original da matriz.

Além disso, o resultado de `unravel_index` vem em `np.int64`, o que deixa o `print()` poluído (`(np.int64(3), np.int64(0))`). Resolvido formatando a saída com f-string.

---

## 🗂️ Estrutura

```
desempenho_vendedores_numpy/
└── desempenho_vendedores.py
```

---

## 🚀 Próximos passos

Seguir para o bloco de filtering (boolean masking formal) → random numbers, fechando o curso de fundamentos de NumPy.