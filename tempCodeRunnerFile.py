
from datetime import date
from datetime import datetime as dt

data_extracao = date.today()

df_selic["data_extracao"] = data_extracao
df_selic["responsavel"] = "Autor"

print(df_selic.info())
df_selic.head()