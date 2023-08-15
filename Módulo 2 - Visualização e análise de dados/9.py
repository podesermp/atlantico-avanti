

# 9 - Utilizando pandas, como remover uma coluna de um DataFrame?
"""
É possível fazer a remoção utilizando o drop() e passando como parâmetros o nome da coluna. O retorno do drop é outro Dataframe sem os valores da coluna.
"""
import pandas as pd
import numpy as np

data = {

    "Nome": ['João', 'Maria', 'Marta', 'Pedro', 'Ricardo'],
    "Idade": [14, np.nan, 17, 18, np.nan],
    "Sexo": ['m','f','f','m', 'm']
}


df = pd.DataFrame(data)


df = df.drop(columns='Sexo')

print(df)