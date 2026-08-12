# 🏬 Painel de Performance de Loja — Pandas + NumPy

> "Dado achatado é só matéria-prima — reshape é o que revela a estrutura que já estava lá."

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-DataFrame-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Aggregate%20%26%20Reshape-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 🎯 Objetivo

Mini projeto de consolidação: construir um painel de indicadores de performance para uma rede de 5 filiais ao longo de um trimestre (3 meses), respondendo perguntas de negócio reais usando Pandas para organização dos dados e NumPy para os cálculos vetorizados — sem roteiro de ferramentas pré-definido, com a escolha de abordagem feita de forma autônoma.

---

## 📐 Perguntas de negócio respondidas

1. Qual o faturamento total de cada filial no trimestre?
2. Qual o faturamento total da empresa em cada mês?
3. Qual filial teve o melhor mês individual, e em que posição (filial, mês) isso ocorreu?
4. Quanto cada filial recebe de comissão (4%) sobre o total vendido no trimestre?
5. Quais filiais não bateram a meta trimestral definida?

---

## 🧱 Pipeline do projeto

```
┌───────────────────────────┐
│  DataFrame long-format       │  vendas, filiais (15 linhas: 5 filiais x 3 meses)
└─────────────┬─────────────────┘
              │  .to_numpy()
              ▼
┌───────────────────────────┐
│  vendas (array 1D, 15 itens) │
└─────────────┬─────────────────┘
              │  .reshape(5, 3)
              ▼
┌───────────────────────────┐
│  vendas_matriz (5x3)         │  linhas = filiais | colunas = meses
└─────────────┬─────────────────┘
              │
    ┌─────────┼─────────────────────────┬───────────────────────┐
    ▼                     ▼                                     ▼
faturamento_por_filial   faturamento_total          melhor_mes(array)
np.sum(axis=1)           np.sum(axis=0)             argmax + unravel_index
    │                     │                                     │
    ▼                     ▼                                     ▼
acrescimo(array, taxa)                     filiais_abaixo_da_meta(array, meta)
soma por filial * comissão                  soma por filial < meta → boolean masking
```

---

## 🔧 Etapas realizadas

- [x] Construção do DataFrame em formato longo (long-format) com vendas e filiais
- [x] Conversão da coluna `vendas` para array NumPy
- [x] Reorganização do array 1D em matriz `(5,3)` via `.reshape()`, sem digitar os dados manualmente de novo
- [x] Faturamento total por filial via `np.sum(axis=1)`
- [x] Faturamento total por mês via `np.sum(axis=0)`
- [x] Localização do melhor mês individual com `np.argmax()` + `np.unravel_index()`, retornando valor e posição real (filial, mês)
- [x] Função `acrescimo(array, comissao)` — cálculo de comissão reutilizável, recebendo array e taxa como parâmetros
- [x] Função `filiais_abaixo_da_meta(filial, meta)` — identificação de filiais abaixo da meta via boolean masking

---

## 💡 Conceitos praticados

| Conceito | Onde apareceu |
|---|---|
| `.reshape()` | Reorganizar array 1D achatado em matriz 5x3 sem redigitar dados |
| `axis=0` vs `axis=1` | Diferenciar "por mês" (empresa) de "por filial" (trimestre) |
| `np.argmax()` + `np.unravel_index()` | Localizar valor máximo com posição real de matriz |
| Função com parâmetros (não variável global) | `acrescimo()` e `filiais_abaixo_da_meta()` reutilizáveis |
| Comparison operator + boolean masking | Filtro de filiais abaixo da meta |

---

## ⚠️ Erros corrigidos durante o desenvolvimento

1. **Confusão entre reajuste e comissão isolada:** a primeira versão da função de comissão multiplicava por `1.04` (total + comissão embutidos), quando o esperado era `0.04` (apenas o valor da comissão).
2. **`axis` trocado na meta:** a meta é por filial (trimestral), então a soma precisa ser `axis=1` (por linha), não `axis=0` (por mês) — erro comum de inverter o eixo de agregação.
3. **`np.max(axis=0)` no lugar de `argmax`+`unravel_index`:** `np.max(axis=0)` retorna o campeão de cada coluna (mês) isoladamente, misturando filiais diferentes — não é o mesmo que "o maior valor único de toda a matriz e sua posição exata".
4. **Uso de variável global em vez do parâmetro da função:** a função `melhor_mes` buscava o valor final direto na variável externa `vendas_matriz` em vez de usar o parâmetro `array` recebido, quebrando a reutilização da função para outras matrizes.

---

## 🗂️ Estrutura

```
painel_performance_loja_pandas_numpy/
└── painel_performance_loja.py
```

---

## 🚀 Próximos passos

Fechar o curso de fundamentos de NumPy: filtering (boolean masking formal) → random numbers.