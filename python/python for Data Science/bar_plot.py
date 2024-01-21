import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('python\python for Data Science\ca-covid.csv')
df.drop('state', axis= 1, inplace= True)
df['date'] = pd.to_datetime(df['date'], format = "%d.%m.%y")
df['month'] = df['date'].dt.month

df.set_index('date',inplace=True)
(df.groupby('month')['cases'].sum()).plot(kind="bar")

plt.savefig('plot.png')
