
# 7 - Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?

import numpy as np
import pandas as pd

data = {

    "Nome": ['João', 'Maria', 'Marta', 'Pedro', 'Ricardo'],
    "Idade": [14, np.nan, 17, 18, np.nan],
    "Sexo": ['m','f','f','m', 'm']
}


df = pd.DataFrame(data)

feminino = df[df['Sexo'] == 'f'] # para selecionar apenas os dados que possuam 'm' na coluna 'Sexo'

print(feminino)