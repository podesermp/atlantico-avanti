
# 8 - Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

"""
Uma alternativa é preencher os valores, caso números, utilizando o método fillna() e utilizar valores como 0, média, mediana ou moda para não perder o contexto dos dados. fillna também pode ser utilizado com valores que não são números. Outra alternativa é remover as linhas que possuem dados ausentes utilizando o método dropna().
"""

import pandas as pd
import numpy as np

data = {

    "Nome": ['João', 'Maria', 'Marta', 'Pedro', 'Ricardo'],
    "Idade": [14, np.nan, 17, 18, np.nan],
    "Sexo": ['m','f','f','m', 'm']
}


df = pd.DataFrame(data)

print('DF original')
print(df)


# média das idades
# df_tratado = df.fillna(np.mean(df['Idade'])) 

# preenche tudo com 0
# df_tratado = df.fillna(0)

df_tratado = df.dropna() # remove as linhas que contém valores NaN

print('Com valores ausentes tratados')
print(df_tratado)
