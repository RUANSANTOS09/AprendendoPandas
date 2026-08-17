# 🪵 Limpeza de Dados com Logging — Pandas + MySQL

> "Log bom não é o que registra tudo — é o que registra o suficiente pra quem for ler entender o que aconteceu sem abrir o código."

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Cleaning-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Logging](https://img.shields.io/badge/Logging-Structured-4B8BBE?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 🎯 Objetivo

Exercício de aquecimento (retorno após pausa de estudos) aplicando `logging` estruturado — prática observada no acompanhamento de um tutorial de pipeline de engenharia de dados — em uma rotina simples de limpeza de dados vindos do MySQL: conversão de tipo e remoção de duplicatas.

O foco não foi o tratamento em si (já dominado em projetos anteriores), mas a qualidade da **observabilidade** do processo: registrar cada etapa de forma clara e proporcional à sua importância.

---

## 🧱 Pipeline do projeto

```
┌──────────────────────────┐
│   MySQL: customers_raw     │
│   pd.read_sql()             │
└─────────────┬────────────────┘
              │  logging.info → total de registros carregados
              ▼
┌──────────────────────────┐
│   Conversão de tipo         │
│   registration_date →       │
│   pd.to_datetime()          │
└─────────────┬────────────────┘
              │  logging.info → coluna convertida
              ▼
┌──────────────────────────┐
│   Verificação de duplicatas │
│   (critério: cpf)           │
└─────────────┬────────────────┘
              │  logging.warning (se houver) / logging.info (se não houver)
              ▼
┌──────────────────────────┐
│   Remoção de duplicatas     │
│   df.drop_duplicates()      │
│   (subset='cpf', keep='last')│
└──────────────────────────┘
              │  logging.info → quantidade e índices removidos
```

---

## 🔧 Etapas realizadas

- [x] Conexão ao MySQL e carga da tabela `customers` via `pd.read_sql()`
- [x] Configuração de `logging` estruturado (`logging.basicConfig`, com timestamp e nível)
- [x] Conversão de `registration_date` para datetime, com log informativo do nome da coluna
- [x] Verificação condicional de duplicatas por `cpf` — `warning` se encontradas, `info` se não
- [x] Remoção de duplicatas com `keep='last'`, reatribuindo corretamente o resultado a `df`
- [x] Log de contagem e índices das linhas removidas, sem despejar o DataFrame inteiro na mensagem

---

## 💡 Conceitos praticados

| Conceito | Aplicação |
|---|---|
| `logging.basicConfig()` | Configuração de log estruturado com timestamp e nível |
| `logging.info()` vs `logging.warning()` | Diferenciar progresso normal de situação que merece atenção |
| Log condicional | `warning` só dispara quando duplicata é de fato encontrada |
| `df.duplicated(subset=..., keep=...)` | Critério de duplicata consistente entre verificação e remoção |
| Reatribuição de métodos Pandas não-inplace | `df = df.drop_duplicates(...)` — método não modifica o DataFrame original sozinho |
| Log enxuto vs verboso | Uso de `len()` e `.index.tolist()` em vez de despejar o DataFrame inteiro na mensagem |

---

## ⚠️ Erros corrigidos durante o desenvolvimento

1. **Log despejando o DataFrame inteiro:** primeiras versões das mensagens de log incluíam a coluna ou o DataFrame completo formatado como texto (`f'Convertendo colunas para datetime:{df["registration_date"]}'`), tornando o log ilegível. Corrigido para incluir apenas o nome da coluna ou a contagem/índices relevantes.
2. **Critério de duplicata inconsistente:** a verificação inicial usava `subset=['cpf']`, mas a extração das linhas duplicadas para log usava `duplicated()` sem `subset` (considerando todas as colunas) — dois critérios diferentes gerando números diferentes. Padronizado para `subset=['cpf']` em ambos os pontos.
3. **`drop_duplicates()` sem reatribuição:** chamada ao método sem capturar o retorno (`df.drop_duplicates(...)` em vez de `df = df.drop_duplicates(...)`) não tinha efeito algum sobre `df`, já que o método não opera in-place por padrão.

---

## 🗂️ Estrutura

```
aquecimento_pandas_logging/
└── limpeza_com_logging.py
```

---

## 🚀 Próximos passos

Aquecimento 3: consulta SQL pura com `GROUP BY` + `HAVING`. Depois, retomar o pipeline ETL de clima (extração já revisada, transformação estudada via tutorial, falta a etapa de carga com `mysql.connector`).