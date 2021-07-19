import pandas as pd
import seaborn as sns

URL = "https://stepik.org/media/attachments/lesson/8083/genetherapy.csv"
data = pd.read_csv(URL)

#Finding mean values for all therapies
data.groupby('Therapy').mean()

#Seting graphics for data

sns.set(font_scale=1.5)
ax = (sns.boxplot(x='Therapy', y='expr', data=data))