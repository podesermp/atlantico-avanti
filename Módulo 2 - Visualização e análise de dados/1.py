
# Utilizando o matplotlib, crie e mostre um gráfico de linha simples e adicione títulos aos eixos X e Y do gráfico.

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 4 * np.pi, 100) 
y = np.sin(x)

plt.title('Seno')
plt.xlabel('Valor para X')
plt.ylabel('Valor para Y')
plt.plot(x, y)
plt.show()

