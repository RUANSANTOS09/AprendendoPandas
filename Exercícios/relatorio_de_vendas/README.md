# 🛒 Relatório de Vendas — Pipeline de Limpeza de Dados

> *"Um DataFrame criado do zero ensina mais sobre a estrutura de uma tabela do que qualquer dado já pronto."*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 📌 Sobre o projeto

Mini projeto de consolidação, construído para praticar um pipeline completo de limpeza de dados a partir de uma base criada manualmente com `pd.DataFrame()` — sem uso de arquivo externo ou banco de dados. O objetivo foi simular, em pequena escala, os mesmos problemas de dado sujo já trabalhados em exercícios anteriores (padronização, conversão, duplicatas), desta vez com dado 100% autoral, incluindo a decisão consciente de adotar o **padrão numérico americano** como convenção de saída.

```
┌───────────────┐     ┌──────────────────────┐     ┌───────────────┐
│  DataFrame     │ ──▶ │   PADRONIZAÇÃO         │ ──▶ │  Relatório     │
│  criado do zero│     │  texto · número · data │     │  limpo         │
└───────────────┘     └──────────────────────┘     └───────────────┘
```

---

## 🎯 Sujeira aplicada de propósito

| Coluna | Inconsistências |
|---|---|
| `seller` | Espaço nas pontas, capitalização mista |
| `value` | Formatos mistos — padrão BR (`1.200,00`) e formato solto (`850.00`) |
| `sale_date` | Separadores diferentes (`-`, `/`), mês inválido (`2020-15-29`) |
| Linhas | Uma duplicata exata (mesma venda inserida duas vezes) |

---

## 🛠️ Estratégia de padronização

### `seller`
- `.str.split()` + `.str.join(" ")` para eliminar espaços redundantes sem afetar nomes compostos legítimos
- `.str.title()` para capitalização consistente

### `value`
- Conversão para o padrão numérico americano: remoção do símbolo de moeda (`R$`), remoção do separador de milhar (`.`) e substituição da vírgula decimal por ponto
- Conversão final para tipo numérico com `pd.to_numeric(errors='coerce')`

### `sale_date`
- Padronização de separadores (`/` → `-`)
- Correção pontual de valor com ordem de componentes divergente
- Conversão para `datetime` com `pd.to_datetime(format='%Y-%m-%d', errors='coerce')`, eliminando a necessidade de inferência automática de formato

### Duplicatas
- Identificação e remoção via `drop_duplicates()`, com `subset` definido pelas colunas que caracterizam uma venda (`seller`, `product`, `sale_date`)

---

## 🔍 Decisões de negócio e pontos de atenção

- **Padrão americano por escolha consciente**: diferente de exercícios anteriores (padrão BR), este projeto adotou o padrão numérico americano como convenção — decisão simples de aplicar por não exigir lógica condicional entre múltiplos formatos, já que a regra (ponto = decimal, vírgula = milhar) é fixa.
- **Mês inválido tratado como erro de origem genuíno**: o valor `2020-15-29` foi propositalmente mantido inconvertível, resultando em `NaT` após `pd.to_datetime`, validado via `.isna().sum()`.
- **`format` explícito elimina inferência ambígua**: especificar `format='%Y-%m-%d'` no `pd.to_datetime` removeu o `UserWarning` de inferência automática, tornando a conversão mais rápida e previsível.

---

## 🧠 Principais aprendizados

- Construção de DataFrame do zero com `pd.DataFrame()`, e a regra de que todas as colunas do dicionário precisam ter o mesmo número de elementos
- Diferença prática entre padrão numérico brasileiro e americano na hora de decidir qual `.replace()` aplicar
- `subset` em `drop_duplicates()` sem a coluna de valor pode não capturar divergências de preço em vendas com as demais colunas idênticas — ponto identificado para atenção em cenários futuros
- Especificar `format` no `pd.to_datetime` evita o comportamento de inferência linha a linha, mais lento e menos previsível em bases maiores

---

## 🚀 Tecnologias utilizadas

- Python 3.14
- Pandas
- Jupyter Notebook (PyCharm)

---

## 👤 Autor

**Ruan Santos**
Estudante de Engenharia de Dados | [GitHub](https://github.com/RUANSANTOS09)