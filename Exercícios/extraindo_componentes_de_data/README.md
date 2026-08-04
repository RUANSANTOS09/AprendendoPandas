# 📅 Formatação de Data a partir de Componentes Extraídos

> *"Dado bruto não se lê — se decompõe, se entende, e só depois se reconstrói."*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 📌 Sobre o projeto

Este exercício trabalha a extração de componentes de uma coluna `datetime` (`ano`, `mês`, `dia`) usando o acessor `.dt` do Pandas, seguida da reconstrução desses componentes numa string formatada e legível, no padrão brasileiro `DD/MM/AAAA`.

```
┌──────────────────┐     ┌───────────────────┐     ┌────────────────────┐
│   created_at      │ ──▶ │  .dt.year/.month/  │ ──▶ │  data_formatada     │
│   (datetime64)     │     │  .day → 3 colunas  │     │  "DD/MM/AAAA"       │
└──────────────────┘     └───────────────────┘     └────────────────────┘
```

---

## 🎯 Problema resolvido

A coluna `created_at` chega ao DataFrame como texto e precisa ser convertida para `datetime` antes de qualquer extração ser possível — o acessor `.dt` só existe em colunas desse tipo. A partir daí, o desafio real não é extrair os componentes (isso é direto), mas **reconstruí-los como texto sem perder a formatação de dois dígitos**, já que `.dt.day` e `.dt.month` retornam números simples (`1`, `6`, `11`) e não strings com zero à esquerda (`01`, `06`).

---

## 🛠️ Estratégia aplicada

1. Conversão da coluna `created_at` para `datetime` com `pd.to_datetime(errors='coerce')`
2. Extração dos componentes `ano`, `mes`, `dia` via `.dt.year`, `.dt.month`, `.dt.day`
3. Conversão de `dia` e `mes` para `string` com `.astype(str)`
4. Preenchimento com zero à esquerda usando `.str.zfill(2)`, garantindo sempre 2 dígitos
5. Concatenação das três colunas no formato `dia/mes/ano`

---

## 🔍 Ponto de atenção identificado

Durante a validação, foi observado que a ausência do `.zfill(2)` produzia datas como `1/11/2017` ao invés de `01/11/2017` — um erro sutil de formatação que só aparece em dias e meses de um único dígito, passando despercebido em boa parte da amostra até uma auditoria linha a linha.

Também foi validado o comportamento do Pandas diante de valores `NaT` (datas inválidas após `coerce`): a extração de componentes de um valor ausente não gera erro — propaga `NaN` de forma consistente, permitindo rodar `.dt` na coluna inteira sem necessidade de tratamento prévio linha a linha.

---

## 🧠 Principais aprendizados

- O acessor `.dt` só funciona sobre colunas já convertidas para `datetime64` — sobre texto, gera erro
- `NaT.year`, `NaT.month`, `NaT.day` retornam `NaN`, sem interromper a execução
- `.str.zfill(n)` preenche uma string com zeros à esquerda até atingir o tamanho `n`, sem afetar strings que já possuem esse tamanho ou mais
- Colunas numéricas extraídas de datas com valores ausentes podem virar `float` (ex: `2017.0`) — atenção ao convertê-las para string, para não herdar o `.0` residual

---

## 🚀 Tecnologias utilizadas

- Python 3.14
- Pandas
- Jupyter Notebook (PyCharm)

---

## 👤 Autor

**Ruan Santos**
Estudante de Engenharia de Dados | [GitHub](https://github.com/RUANSANTOS09)