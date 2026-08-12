import numpy as np


# Passo 1. Montando array de vendedores coluna = mes Linha = vendedores 4 vendedores 3 meses
vendas = np.array([[3000, 1000, 5000],
                   [1500, 900, 1900],
                   [2367, 4998, 1150],
                   [9455, 3988, 3010]])

# Passo 2. Descobrir o total vendido por vendedor (considerando os 3 meses juntos)
faturamento_por_vendedor = np.sum(vendas, axis=1)
print(faturamento_por_vendedor)

# Passo 3. Descobrir o total vendido pela empresa inteira em cada mês
faturamento_mes = np.sum(vendas, axis=0)
print(faturamento_mes)

# Passo 4. Descobrir qual vendedor teve a maior venda individual (um valor específico, não a soma) e em qual posição ela está
linha, coluna = np.unravel_index(np.argmax(vendas), vendas.shape)
print(f'({linha},{coluna})')

# Passo 5. Descobrir a média de venda de cada mês
media = np.mean(vendas, axis=0)
print(media)

