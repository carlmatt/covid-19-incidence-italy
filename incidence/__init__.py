__version__ = '0.1.0'

import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns

# Covid case data
url = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province.json'
response = requests.get(url)
data = response.json()
df_covid = pd.DataFrame(data)

df_covid['data'] = pd.to_datetime(df_covid.data)


def diff_function(df):
    return df.diff()

cases_increase = df_covid.groupby('denominazione_provincia')['totale_casi'].apply(diff_function)
df_covid['cases_increase'] = cases_increase
df_covid = df_covid.dropna(subset=['cases_increase']).reset_index(drop=True)
df_covid['cases_increase'] = df_covid['cases_increase'].astype('int')

df_covid[df_covid.denominazione_provincia == 'Parma']

df_covid[df_covid.denominazione_provincia == 'Parma'].set_index('data').cases_increase.plot()
