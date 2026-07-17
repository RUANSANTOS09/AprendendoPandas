<div align="center">

# 🐼 Pandas + MySQL — Filtros com read_sql

> "Pandas é a ponte entre o dado bruto e o dado pronto pra uso."

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success?style=for-the-badge)

</div>

---

## 📌 Sobre o projeto

Primeiros exercícios de Pandas integrados diretamente com MySQL: em vez de praticar filtros com arquivos Excel/CSV soltos (como no exemplo do curso), os dados são extraídos direto do banco `sakila` usando `pandas.read_sql()`, conectando os dois aprendizados desde o primeiro dia de Pandas.

---

## 🔌 Conexão Pandas + MySQL

```python
import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Ruan81527733',
    database="sakila",
    charset='utf8mb4'
)

df = pd.read_sql("SELECT * FROM film", connection)
```

`pd.read_sql(query, connection)` executa uma query SQL e já devolve o resultado como DataFrame, dispensando `cursor.fetchall()` manual.

---

## 🧠 Exercícios

### 1. Filtro numérico simples com `.loc`
```python
df_filter_film = df.loc[df['rental_rate'] > 3]
```
Filtra filmes com preço de aluguel acima de R$3 — equivalente a `WHERE rental_rate > 3` em SQL.

### 2. Filtro por lista de valores com `.isin()`
```python
itens = ['PG', 'PG-13', 'R']
df_filter_rating = df.loc[df['rating'].isin(itens)]
```
Filtra filmes cuja classificação esteja dentro de uma lista — equivalente ao `WHERE rating IN ('PG', 'PG-13', 'R')` em SQL.

### 3. Filtro combinado com `&`
```python
df_filter_film = df.loc[(df['rental_duration'] > 5) & (df['replacement_cost'] < 20)]
```
Combina duas condições simultâneas — equivalente ao `WHERE rental_duration > 5 AND replacement_cost < 20` em SQL. Cada condição precisa estar entre parênteses ao usar `&`.

---

## 💡 Conceitos praticados

- `pandas.read_sql()` para extrair dado direto do MySQL como DataFrame
- `.loc[]` para filtragem de linhas (equivalente ao `WHERE` do SQL)
- `.isin()` para filtro por lista de valores (equivalente ao `IN` do SQL)
- Combinação de condições com `&`, exigindo parênteses em cada uma
- Raw string (`r"..."`) para caminhos de arquivo no Windows

---

<div align="center">

**Ruan Santos** · [GitHub](https://github.com/RUANSANTOS09)

</div>