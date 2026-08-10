# 💰 Cálculo de Comissão de Vendedores — Pandas + NumPy

> "Regra de negócio em código vetorizado: a condição decide onde aplicar, a máscara decide quem recebe."

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-DataFrame-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Boolean%20Masking-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 🎯 Objetivo

Simular um problema comum de dia a dia corporativo: cálculo de comissão de vendedores com regra de bônus condicional por performance, aplicando o cálculo de forma vetorizada (sem loops) através de boolean masking, e encapsulando a lógica em uma função reutilizável.

---

## 📐 Regra de negócio

- Todo vendedor recebe **comissão base de 5%** sobre o valor vendido.
- Vendedores que venderam **acima de R$ 3.000** recebem um **bônus extra de 2%** sobre o valor vendido, somado à comissão base.

---

## 🧱 Pipeline do projeto

```
┌───────────────────────┐
│   DataFrame de vendas   │   colunas: vendedor, valor_vendido
└───────────┬────────────┘
            │  .to_numpy()
            ▼
┌───────────────────────┐
│   vendas (array bruto)  │   preservado intacto para a condição do bônus
└───────────┬────────────┘
            │
            ▼
┌─────────────────────────────────────────────┐
│      calcular_comissao_total(valor_vendido)   │
│                                                │
│  1. comissao_base = valor_vendido * 1.05      │
│  2. máscara: valor_vendido > 3000             │
│  3. comissao_base[máscara] +=                 │
│         valor_vendido[máscara] * 0.02         │
│  4. return comissao_base                      │
└─────────────────────────────────────────────┘
```

---

## ⚠️ Ponto de atenção resolvido durante o desenvolvimento

Na primeira tentativa, a comissão base foi calculada **sobrescrevendo** o array de vendas original (`vendas *= 1.05`). Isso quebrou a regra do bônus, porque a condição `> 3000` passou a comparar a **comissão já calculada** em vez do **valor de venda bruto** — mudando quem se qualificava para o bônus.

**Correção:** manter o array de vendas bruto intacto em uma variável separada, usado exclusivamente para a condição da máscara, enquanto o resultado do cálculo vive em uma variável própria.

---

## 🔧 Etapas realizadas

- [x] Construção do DataFrame com 6 vendedores e valores de venda variados
- [x] Conversão da coluna `valor_vendido` para array NumPy
- [x] Cálculo da comissão base (5%) via operação escalar
- [x] Identificação de vendedores elegíveis ao bônus via comparison operator + boolean masking
- [x] Aplicação do bônus (2% sobre o valor vendido) apenas nas posições elegíveis, usando atribuição condicional (`+=`)
- [x] Encapsulamento da lógica completa em `calcular_comissao_total()`, recebendo o array como parâmetro (sem depender de variável global)

---

## 💡 Conceitos praticados

| Conceito | Onde apareceu |
|---|---|
| `.to_numpy()` | Conversão da coluna de vendas |
| Operação escalar | Cálculo da comissão base (5%) |
| Comparison operator + boolean masking | Identificação de vendedores elegíveis ao bônus |
| Atribuição condicional (`array[mascara] += valor`) | Aplicação do bônus só nas posições elegíveis |
| Função com parâmetro (não variável global) | `calcular_comissao_total(valor_vendido)` reutilizável |
| Separação entre dado bruto e resultado calculado | Evitar sobrescrever `vendas` com a comissão |

---

## 🗂️ Estrutura

```
comissao_vendedores_pandas_numpy/
└── comissao_vendedores.py
```

---

## 🚀 Próximos passos

Retomar broadcasting (pendente) → aggregate functions (axis) → filtering (boolean masking formal) → random numbers.