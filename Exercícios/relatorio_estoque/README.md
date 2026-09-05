# 🔄 Melt + Pivot Table — Controle de Estoque Mensal

> "Melt e pivot_table são operações inversas — se você consegue ir e voltar entre os dois formatos sem perder dado, é sinal de que o conceito grudou de verdade."

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Melt%20%26%20Pivot-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 🎯 Objetivo

Exercício de revisão (retorno após pausa para prova da faculdade) para confirmar que `melt()` e `pivot_table()` são operações inversas: transformar um controle de estoque mensal de formato largo para longo, e depois voltar ao formato largo original, validando que nenhum dado se perde no processo.

---

## 🧱 Pipeline do exercício

```
┌─────────────────────────────────────┐
│  DataFrame largo                        │
│  produto | estoque_01 | estoque_02 |     │
│  estoque_03                              │
└─────────────────┬─────────────────────────┘
                   │  df.melt(id_vars=['produto'],
                   │          var_name='mes', value_name='quantidade_estoque')
                   ▼
┌─────────────────────────────────────┐
│  DataFrame longo                        │
│  produto | mes ('estoque_01') | quantidade_estoque │
└─────────────────┬─────────────────────────┘
                   │  str.rsplit('_', n=1) → separa prefixo/número do mês
                   │  drop da coluna de prefixo
                   ▼
┌─────────────────────────────────────┐
│  produto | mes ('01') | quantidade_estoque │
└─────────────────┬─────────────────────────┘
                   │  pivot_table(index=['produto'], columns=['mes'],
                   │              values=['quantidade_estoque'], aggfunc='first')
                   ▼
┌─────────────────────────────────────┐
│  DataFrame largo reconstruído           │
│  produto | 1 | 2 | 3                     │
└─────────────────────────────────────┘
```

---

## 🔧 Etapas realizadas

- [x] Construção de controle de estoque com 5 produtos e 3 meses
- [x] Transformação para formato longo com `melt()`
- [x] Separação do prefixo "estoque_" do número do mês via `str.rsplit()`
- [x] Reconstrução do formato largo original com `pivot_table()`, usando `aggfunc='first'` (sem necessidade de agregação real, já que cada combinação produto+mês tem valor único)
- [x] Validação de que o resultado final reproduz fielmente os dados de entrada

---

## 💡 Conceitos praticados

| Conceito | Aplicação |
|---|---|
| `melt()` | Formato largo → longo |
| `pivot_table()` | Formato longo → largo (operação inversa ao melt) |
| `aggfunc='first'` | Escolha apropriada quando não há duplicata para agregar de fato |
| `str.rsplit()` | Separação de prefixo textual de valor numérico |

---

## ⚠️ Observação técnica

A coluna de mês foi convertida para datetime (`pd.to_datetime(..., format='%m')`) e depois extraída de volta como número inteiro (`.dt.month`) — passo desnecessário nesse caso, já que o valor original (`'01'`, `'02'`, `'03'`) já representava um número em formato string, podendo ser convertido diretamente com `.astype(int)`. A conversão via datetime só se justifica quando operações reais de data são necessárias (extração de nome do mês, cálculo de diferença entre datas, etc.).

---

## 🗂️ Estrutura

```
exercicios_pandas_revisao/
└── estoque_melt_pivot.py
```

---

## 🚀 Próximos passos

Fechar exercício de revisão de funcionários/departamento (groupby + apply com faixa salarial). Em seguida, iniciar o curso de SQL Avançado (window functions, CTEs, funções por tipo de dado).