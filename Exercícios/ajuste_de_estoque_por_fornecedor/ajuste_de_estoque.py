import pandas as pd
import numpy as np

'''
Exercício — Ajuste de Estoque por Fornecedor

Uma loja recebe reajustes de preço trimestrais dos fornecedores,
mas cada fornecedor tem um percentual de reajuste diferente.
Você tem 6 produtos, vindos de 3 fornecedores diferentes (2 produtos por fornecedor). 
Cada fornecedor tem seu próprio percentual de reajuste.
Depois de aplicar o reajuste correto em cada produto,
você precisa identificar quais produtos ficaram com preço acima de um teto definido por você.

Resolve do jeito que você achar melhor. Quando terminar (ou travar de verdade, sem saber nem por onde começar), me chama.
'''

report = {
    'produtos': ['Teclado', 'Mouse', 'Monitor', 'Fone Bluetooth', 'Mousepad', 'Light bar'],
    'preço': [200, 100, 2000, 100, 80, 70],
    'fornecedor': ['Fornecedor A', 'Fornecedor A', 'Fornecedor B', 'Fornecedor B', 'Fornecedor C', 'Fornecedor C']
}

df = pd.DataFrame(report)
print(df)

preco = df['preço'].to_numpy()

preco_fornecedorA = preco[0:2]
preco_fornecedorB = preco[2:4]
preco_fornecedorC = preco[4:]

reajuste_fornecedorA = preco_fornecedorA * 1.08
reajuste_fornecedorB = preco_fornecedorB * 1.10
reajuste_fornecedorC = preco_fornecedorC * 1.09

def sinalizar_acima_teto(precos, teto):
    filtro = precos > teto
    valor_acima = precos[filtro]
    return valor_acima

print(sinalizar_acima_teto(reajuste_fornecedorA, 200))
print(sinalizar_acima_teto(reajuste_fornecedorB, 2000))
print(sinalizar_acima_teto(reajuste_fornecedorC, 80))