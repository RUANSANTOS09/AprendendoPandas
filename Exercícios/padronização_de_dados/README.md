# 🧹 Padronização de Dados com Pandas

> *"Dado sujo não avisa que está errado — ele simplesmente mente com confiança."*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Data Engineering](https://img.shields.io/badge/Data%20Engineering-FF6F00?style=for-the-badge&logo=databricks&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 📌 Sobre o projeto

Este projeto simula um cenário real de Engenharia de Dados: uma tabela de pedidos (`orders_raw_import`) construída com **sujeira intencional** — a mesma bagunça que qualquer pipeline de produção recebe de sistemas externos, formulários e integrações.

O objetivo foi transformar essa camada **Raw** em uma camada **Clean**, aplicando padronização de tipos, formatos e valores, com auditoria em cada etapa do processo.

```
┌─────────────┐       ┌──────────────────────┐       ┌─────────────┐
│     RAW     │  ───▶ │      PADRONIZAÇÃO     │  ───▶ │    CLEAN    │
│ orders_raw_ │       │  price · order_date   │       │  df pronto  │
│   import    │       │  tipos · formatos     │       │ para análise│
└─────────────┘       └──────────────────────┘       └─────────────┘
```

---

## 🎯 Problemas enfrentados no dataset bruto

| Coluna | Inconsistências encontradas |
|---|---|
| `price` | `R$`, `$`, letra `O` no lugar de `0`, sinal `-` sobrando, separador decimal e de milhar misturados (`R$ 8.500,00`, `4500.50`, `4.300`) |
| `order_date` | Separadores diferentes (`/`, `.`, espaço), nomes de mês por extenso (`23 Abril 2025`), ordem de componentes invertida (`YYYY-MM-DD` vs `DD-MM-YYYY`), ano com 2 dígitos, mês inválido (`13`), valores vazios |

---

## 🛠️ Estratégia de padronização

### `price`
1. Remoção de símbolos monetários (`R$`, `$`)
2. Correção de erro de digitação (`O` → `0`)
3. Resolução de separador decimal vs. milhar via lógica condicional:
   - Presença de vírgula → formato BR (`.` = milhar, `,` = decimal)
   - Ausência de vírgula + 3 dígitos após o último ponto → milhar sem separador decimal
   - Ausência de vírgula + 2 dígitos após o último ponto → decimal genuíno
4. Conversão para tipo numérico com `pd.to_numeric(errors='coerce')`
5. Auditoria com `.unique()` e `.isna().sum()` antes de considerar a coluna finalizada

### `order_date`
1. Substituição de nomes de mês por número via dicionário de mapeamento
2. Padronização de separadores (`.`, `/`, espaço → `-`)
3. Remoção de hífens residuais nas extremidades
4. Correção pontual de datas com ordem de componentes invertida
5. Conversão para `datetime` com `pd.to_datetime(dayfirst=True, errors='coerce')`
6. Auditoria de cada valor convertido para `NaT`, com causa identificada e documentada

---

## 🔍 Princípio central aplicado

> **Nunca corrigir sem diagnosticar antes.**

Cada etapa de limpeza foi validada com `.unique()` antes da correção e `.isna().sum()` depois da conversão — garantindo que nenhum valor fosse silenciosamente perdido ou distorcido no processo.

---

## 📊 Resultado final

| Métrica | Resultado |
|---|---|
| Valores inválidos em `price` após padronização | `0` |
| Valores `NaT` em `order_date` | `2` (ambos com causa de origem identificada: mês inválido e data ausente) |

---

## 🧠 Principais aprendizados

- Diferença entre `.str.replace()` (trecho de texto) e `.replace()` (valor inteiro)
- Funções sem `return` explícito em todos os caminhos retornam `None` silenciosamente
- `pd.to_datetime` infere um formato único para toda a coluna — formatos mistos exigem padronização prévia, não apenas o parâmetro `dayfirst`
- Separador de milhar vs. decimal sem vírgula como pista: resolvido contando dígitos após o último separador
- Importância de reiniciar o kernel após alterar funções já aplicadas em pipeline

---

## 🚀 Tecnologias utilizadas

- Python 3.14
- Pandas
- Jupyter Notebook (PyCharm)

---

## 👤 Autor

**Ruan Santos**
Estudante de Engenharia de Dados | [GitHub](https://github.com/RUANSANTOS09)