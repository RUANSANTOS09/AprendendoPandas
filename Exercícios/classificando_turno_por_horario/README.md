# 🕐 Classificação de Turno a partir de Horário

> *"Uma regra de negócio só está pronta quando cobre todas as horas do relógio, sem sobreposição e sem lacuna."*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

---

## 📌 Sobre o projeto

Este exercício classifica cada registro de um DataFrame em um turno do dia — **Manhã**, **Tarde** ou **Noite** — a partir do componente de hora extraído de uma coluna `datetime`, aplicando lógica condicional própria através de `.apply()`.

```
┌──────────────────┐     ┌────────────────┐     ┌──────────────────┐
│   created_at      │ ──▶ │  .dt.hour       │ ──▶ │   turno           │
│   (datetime64)     │     │  (0 a 23)       │     │  Manhã/Tarde/Noite│
└──────────────────┘     └────────────────┘     └──────────────────┘
```

---

## 🎯 Regra de negócio aplicada

| Turno | Faixa de horário |
|---|---|
| Manhã | 06h às 11h59 |
| Tarde | 12h às 18h59 |
| Noite | 19h às 05h59 |

---

## 🛠️ Estratégia aplicada

1. Extração da hora diretamente de `created_at.dt.hour`, sem necessidade de criar uma coluna intermediária `horas`
2. Construção de uma função `shift(hour)` com estrutura `if` / `elif` / `else`, cada caminho retornando o turno correspondente
3. Aplicação da função na coluna com `.apply()`

---

## 🔍 Ponto de atenção identificado

A primeira versão da função continha uma sobreposição de faixa: a condição `hour <= 12` no bloco `if` da manhã capturava o valor `12`, impedindo que ele chegasse ao `elif` da tarde — resultado, meio-dia era classificado como manhã. A correção substituiu o limite superior da manhã para `hour <= 11`, eliminando a sobreposição e garantindo que cada hora do dia pertença a exatamente um turno.

---

## 🧠 Principais aprendizados

- Numa cadeia `if` / `elif` / `else`, cada condição só é avaliada se as anteriores falharem — o limite inferior de uma faixa intermediária pode ficar implícito, sem necessidade de reescrevê-lo explicitamente
- Sobreposição de faixas em regras condicionais é um erro silencioso: o código roda sem exceção, mas produz classificação incorreta em casos de borda (nesse caso, especificamente às 12h)
- Não é necessário recriar uma coluna auxiliar (`horas`) quando o componente pode ser acessado diretamente da coluna `datetime` original via `.dt.hour`, reduzindo uma etapa desnecessária no pipeline

---

## 🚀 Tecnologias utilizadas

- Python 3.14
- Pandas
- Jupyter Notebook (PyCharm)

---

## 👤 Autor

**Ruan Santos**
Estudante de Engenharia de Dados | [GitHub](https://github.com/RUANSANTOS09)