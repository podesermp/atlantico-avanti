



# 10 - Utilizando pandas, mostre uma forma de detectar e tratar valores outliers em um DataFrame.

"""
É possível identificar outliers utilizando o plot de gráfico ou alguma funções auxiliares para verificar valores que fogem dos padrões dos dados. Para tratar, é possível remover eles ou adicionar valores de média, moda ou mediana para eles.
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore


data = {

    "Nome": ['João', 'Maria', 'Marta', 'Pedro', 'Ricardo'],
    "Idade": [25, 16, 17, 20, 0],
    "Sexo": ['m','f','f','m', 'm']
}


df = pd.DataFrame(data)

limite_superior = 20 #definido olhando para o boxplot
limite_inferior = 15 #definido olhando para o boxplot

outliers = df[df['Idade'] < limite_inferior]

print(outliers) 

df_sem_outliers = df[df['Idade'] > limite_inferior]

plt.figure(figsize=(9, 3))


plt.subplot(121)
plt.boxplot(df['Idade'])
plt.title('Com outliers')

plt.ylabel('Idade (anos)')

plt.subplot(122)
plt.boxplot(df_sem_outliers['Idade'])
plt.title('Sem outliers')


plt.show()