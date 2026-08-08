import pandas as pd
import numpy as np

dados = {
    'id_venda': [0,1,2,3,5,5],
    'produto': ['Tv', None, None, 'Geladeira', 'Pc', 'Pc'],
    'quantidade': [5,None,None, 4, 3, 3],
    'preco': [1500.00, None, None, 2000.00, 3000.00, 3000.00 ]
}
df = pd.DataFrame(dados)
# Localizando as duplicadas
# duplicados = df[df.duplicated()]
# print(duplicados)
df = df.drop_duplicates()

# ======== Identificando valores nulos =====
# Localizando valores nulos
# nulos = df[df.isna().any(axis=1)]
df = df.dropna()
# ====== Convertendo =====
df['quantidade'] = df['quantidade'].astype(int)
df_array = df.to_numpy()
column_price = df_array[:, 3:]
all_raw = df_array[0:3, :]

column_price_and_amount = df_array[:, 2:]
print(column_price)
