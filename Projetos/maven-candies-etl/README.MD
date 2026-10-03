# Maven Candies ETL

> Pipeline de ETL (Extract, Transform, Load) para o dataset Maven Candies, extraindo dados de um banco MySQL, tratando inconsistências com Pandas e exportando os dados limpos para CSV.

## 📋 Sobre o projeto

Este projeto implementa um pipeline de ETL simples e modular que:

1. **Extrai** as tabelas `products`, `orders` e `customers` de um banco MySQL
2. **Transforma** os dados, corrigindo problemas de qualidade identificados (valores nulos, tipos de dado incorretos)
3. **Carrega** o resultado tratado em arquivos CSV, prontos para análise

## 🗂️ Estrutura do projeto

```
maven-candies-etl/
├── data/
│   ├── raw/            # CSVs originais, intocados (fonte imutável)
│   └── processed/      # CSVs tratados, gerados pelo pipeline
├── extract.py          # Conexão com MySQL e extração das tabelas
├── transform.py        # Limpeza e transformação dos dados
├── load.py              # Exportação dos dados tratados para CSV
├── main.py              # Orquestra o pipeline (extract → transform → load)
├── requirements.txt
├── .env.example         # Modelo de variáveis de ambiente (sem valores reais)
└── .gitignore
```

## ⚙️ Pré-requisitos

- Python 3.10+
- MySQL com o banco `maven_advanced_sql` já criado, contendo as tabelas `products`, `orders` e `customers`

## 🚀 Como rodar

1. Clone o repositório:
   ```
   git clone <url-do-repositorio>
   cd maven-candies-etl
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Crie o arquivo `.env` na raiz do projeto, seguindo o modelo de `.env.example`:
   ```
   DB_HOST=localhost
   DB_USER=seu_usuario
   DB_PASSWORD=sua_senha
   DB_NAME=maven_advanced_sql
   ```

4. Execute o pipeline completo:
   ```
   python main.py
   ```

5. Os arquivos tratados serão gerados em `data/processed/`:
   - `products_clean.csv`
   - `orders_clean.csv`
   - `customers_clean.csv`

## 🧹 Problemas de qualidade identificados e tratados

| Tabela | Coluna | Problema | Tratamento |
|---|---|---|---|
| `products` | `division` | 2 valores nulos | Preenchido com `'Other'` — os 2 produtos afetados possuem `product_id` no padrão `OTH-*` e juntos somam 100 vendas registradas em `orders`, descartando a opção de remover a linha |
| `products` | `unit_price` | 1 valor nulo | Preenchido com `0` — o produto afetado não possui nenhuma venda registrada em `orders`, não havendo risco de distorcer métricas de receita |
| `orders` | `order_date` | Armazenada como texto (`object`) | Convertida para `datetime` com `pd.to_datetime()` |
| `orders` | `order_id` + `product_id` | Possível duplicidade de linha | Validação automática no pipeline (`duplicated()`), sem ocorrências encontradas na extração atual |

## 🔒 Segurança

As credenciais do banco de dados são carregadas a partir de variáveis de ambiente (`python-dotenv`), nunca escritas diretamente no código. O arquivo `.env` está listado no `.gitignore` e não é versionado.

## 🛠️ Tecnologias

- Python
- Pandas
- MySQL Connector/Python
- python-dotenv