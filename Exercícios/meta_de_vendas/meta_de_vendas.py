# =============== Broadcasting ===============
import numpy as np

vendas = np.array([[2000, 1000, 900, 5000],
                   [1000, 2000, 1500, 3500],
                   [1500, 2500, 1350, 3200],
                   [1900, 2650, 1750, 3200],
                   [2200, 2700, 3000, 2900]
                   ])
meta = np.array([[1000, 2000, 2500, 3000]])

meta_por_vendedor = vendas - meta
filtro = meta_por_vendedor < 0
print(filtro)