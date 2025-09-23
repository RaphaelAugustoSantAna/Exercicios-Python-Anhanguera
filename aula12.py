import matplotlib.pyplot as plt
import random

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

plt.plot(dados1, dados2)

############################################

import pandas as pd

dados = {"Produto": ["A", "B", "C"], "qtde_vendida": [33, 50, 45]}

df = pd.DataFrame(dados)
df.plot(x="Produto", y="qtde_vendida", kind="bar")
# df.plot(x="Produto", y="qtde_vendida", kind="pie")
# df.plot(x="Produto", y="qtde_vendida", kind="line")
