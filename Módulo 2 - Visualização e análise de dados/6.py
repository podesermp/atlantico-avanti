
# 6 - Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?


import pandas as pd


data = pd.read_csv('PATH.csv') # para ler o arquivo csv
print(data.head()) # para mostrar os 5 primeiros elementos