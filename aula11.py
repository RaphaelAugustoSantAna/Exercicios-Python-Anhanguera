import pandas as pd

df_selic = pd.read_json(
    "http://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"
)

print(df_selic.info())
