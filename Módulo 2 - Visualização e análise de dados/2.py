
# 2 - Utilizando o matplotlib, utilize a função subplot() para mostrar 6 gráficos.

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 4 * np.pi, 100)

y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.sqrt(x)
y5 = x*2
y6 = -x


fig, grafs = plt.subplots(3, 2)

grafs[0,0].plot(x, y1)
grafs[0,0].set_title('Sen')

grafs[0,1].plot(x, y2)
grafs[0,1].set_title('Cos')

grafs[1,0].plot(x, y3)
grafs[1,0].set_title('Tan')

grafs[1,1].plot(x, y4)
grafs[1,1].set_title('Sqrt')

grafs[2,0].plot(x, y5)
grafs[2,0].set_title('*2')

grafs[2,1].plot(x, y6)
grafs[2,1].set_title('-x')

plt.show()