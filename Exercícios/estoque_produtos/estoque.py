import pandas as pd
import numpy as np

estoque = {
    'produto': ['Teclado', 'mouse', 'monitor', 'Webcam', 'Pc'],
    'preco_unitario': [450, 100, 1400, 100, 3000],
    'quantidade_estoque': [4, 5, 5, 2, 3]
}

df = pd.DataFrame(estoque)

array = df[['preco_unitario', 'quantidade_estoque']].to_numpy()
preco_unitario = array[:, 0:1]
quantidade_estoque = array[:, 1:2]
valor_total = preco_unitario * quantidade_estoque
filtro = valor_total[valor_total > 500]
print(f'Produtos acima de 500 reais: {filtro}')