import pandas as pd
import numpy as np

'''
Cenário: você é responsável por analisar os dados de vendas de uma loja com múltiplas filiais ao longo de um trimestre, 
e vai gerar um pequeno painel de indicadores.

Contexto dos dados:

5 filiais, 3 meses de vendas (valores em R$).
Cada filial tem uma meta trimestral individual definida pela matriz.
A empresa aplica uma taxa de comissão fixa de 4% sobre tudo que é vendido.
'''

'''
O que o painel precisa responder (sem ordem obrigatória, resolve como fizer sentido pra você):

Qual foi o faturamento total de cada filial no trimestre?   
Qual foi o faturamento total da empresa em cada mês?
Qual filial teve o melhor mês individual (maior valor único) e em que posição (filial, mês) isso aconteceu?
Quanto cada filial vai receber de comissão sobre o total vendido no trimestre?
Quais filiais não bateram a meta trimestral (compare o faturamento total de cada uma com a meta dela)?

'''

# Passo 1. Criar um DataFrame onde mês = coluna ou seja 3 colunas e linhas = vendas ou seja 5 linhas
report = {
    'vendas': [9000, 10000, 5000, 2345, 9809, 17280, 8957, 17234, 10980, 18232, 1823, 1946, 3791, 7586, 6387], # (5,3)
}

df = pd.DataFrame(report)
vendas = df['vendas'].to_numpy()
vendas_matriz = vendas.reshape(5, 3)
print(vendas_matriz)

# Passo 2. Qual foi o faturamento total de cada filial no trimestre?
faturamento_por_filial = np.sum(vendas_matriz, axis=1)
print(faturamento_por_filial)

# Passo 3. Qual foi o faturamento total da empresa em cada mês?
faturamento_total = np.sum(vendas_matriz, axis=0)
print(faturamento_total)

# Passo 4. Qual filial teve o melhor mês individual (maior valor único) e em que posição (filial, mês) isso aconteceu?
def melhor_mes(array):
    filial, mes = np.unravel_index(np.argmax(array), array.shape) # posição (filial, mês) que isso aconteceu
    return f'Valor: {array[filial, mes]} | Filial: {filial} | Mes: {mes}'
print(melhor_mes(vendas_matriz))

# Passo 5. Quanto cada filial vai receber de comissão sobre o total vendido no trimestre?
def acrescimo(array, comissao):
    total_vendido_mes = np.sum(array, axis=1)
    aplicação_de_taxa = total_vendido_mes * comissao
    return aplicação_de_taxa
print(f'Total de comissão que cada filial ira receber: {acrescimo(vendas_matriz, 0.04)}')
# Passo 6. Quais filiais não bateram a meta trimestral (compare o faturamento total de cada uma com a meta dela)?
def filiais_abaixo_da_meta(filial, meta):
    filial = np.sum(filial,axis=1)
    filtro = filial[filial < meta]
    return filtro
print(filiais_abaixo_da_meta(vendas_matriz, 23000))

