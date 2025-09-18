# primeiro modo

import math

math.sqrt(25)
math.log2(1024)
math.cos(45)

# segundo modo

import math as m

m.sqrt(25)
math.log2(1024)
m.cos(45)

# terceiro modo

from math import sqrt, log2, cos

sqrt(25)
log2(1024)
cos(45)


# usando biblioteca matplotlib

import matplotlib.pyplot as plt

# Dados

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

# Criar um gráfico de linha
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

# Adicionar um título ao gráfico

plt.title("Exemplo de Gráfico de Linha")

# Mostrar o gráfico
plt.show()
