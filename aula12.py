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

############################################################

import seaborn as sns

sns.set(style="whitegrid")  # opções: darkgrid, whitegrid, dark, white, ticks

df_tips = sns.load_dataset("tips")

print(df_tips)

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

sns.barplot(data=df_tips, x="sex", y="total_bill", ax=ax[0])

# media por sexo

sns.barplot(data=df_tips, x="sex", y="total_bill", ax=ax[1], estimator=sum)
# O motivo para optar pelo "barplot()" muitas vezes se baseia nos parâmetros adicionais e na flexibilidade que ele oferece.
# Vamos dar destaque ao parâmetro "estimator", que, por padrão, calcula a média.

sns.barplot(data=df_tips, x="sex", y="total_bill", ax=ax[2], estimator=len)
# A função "barplot()" do Seaborn apresenta uma variedade de opções estatísticas,
# permitindo que os cientistas de dados escolham a métrica que melhor se ajusta aos seus objetivos.
# Por exemplo, você pode calcular a soma, a contagem ou até mesmo outras métricas personalizadas.
# Isso é particularmente útil quando você deseja exibir informações diferentes nas barras,
# como a quantidade (len) ou a soma (sum) dos valores, em vez da média.
