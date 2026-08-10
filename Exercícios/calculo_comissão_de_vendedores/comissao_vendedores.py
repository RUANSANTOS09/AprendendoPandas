import pandas as pd
import numpy as np

report = {
    'vendedor': ['Ricardo', 'Luiz', 'Pedro', 'Marcos', 'Leandro', 'Felipe'],
    'valor_vendido': [100, 400, 5000, 3345.78, 98.02, 3591.62]
}
df = pd.DataFrame(report)
vendas = df['valor_vendido'].to_numpy()

def calcular_comissao_total(valor_vendido):
    comissao_base = valor_vendido * 1.05
    comissao_base[valor_vendido > 3000] += valor_vendido[valor_vendido > 3000] * 0.02
    return comissao_base
print(calcular_comissao_total(vendas))

