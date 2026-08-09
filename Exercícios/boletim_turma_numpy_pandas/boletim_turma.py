import pandas as pd
import numpy as np

report = {
    'aluno': ['Renato', 'Fabricio', 'Gustavo', 'Henrique', 'Leandro', 'Pedro'],
    'prova1': [7.8, 4.5, 5.8, 8.9, 9.5, 6.8],
    'prova2': [8.8, 6.7, 7.8, 9.2, 7.5, 9.8],
    'prova3': [6.1, 8.1, 7.1, 7.3, 9.5, 8.2]
}
df = pd.DataFrame(report)
# Verificando se existe valores nulos
print(df.isnull().sum())

#transformando colunas das provas em array
array = df[['prova1', 'prova2', 'prova3']].to_numpy().copy()

# Aplicando bônus de 0.5
array += 0.5


# Tirando a média de cada aluno
prova1 = array[:, 0:1]
prova2 = array[:, 1:2]
prova3 = array[:, 2:3]
media_prova = (prova1 + prova2 + prova3) / 3
print(media_prova)

#Extraindo apenas a coluna da prova 1
print(prova1)

#Extraindo as 3 primeiras notas dos 3 primeiros alunos
tres_primeiras_notas = array[0:3, :]
print(tres_primeiras_notas)

#Filtrando medias abaixo de 6
filtro = media_prova[media_prova < 6]
print(f'Notas abaixo de 6 {filtro}')


