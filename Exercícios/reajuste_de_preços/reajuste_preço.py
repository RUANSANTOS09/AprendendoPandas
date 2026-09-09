# =============== Broadcasting ===============
import numpy as np

precos = np.array([[20, 30, 50],   # = (4,3)
                  [10.45, 11, 12.50],
                   [90.80, 91, 92],
                   [45.80, 46.80, 47.50]
                  ])
reajuste = np.array([[1.02], # = (4,1)
                    [1.03],
                    [1.04],
                    [1.05]])
aplicando_reajuste = precos * reajuste
print(aplicando_reajuste)
