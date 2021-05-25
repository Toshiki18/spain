# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:35:18 2020

@author: oyamatoshiki
"""

import numpy as np
import pandas as pd
import seaborn as sns
import japanize_matplotlib


df = pd.read_csv('C:\sample\dataset-football-2010-2020.csv', header = None)
df.columns = ['date', 'home', 'away', 'score(H)', 'score(A)', 'Tournament', 'city', 'country', 'neutral']

#home = df[['date', 'home', 'away', 'score(H)', 'score(A)', 'Tournament', 'country']][df['home'].isin(['Japan'])]
home = df[['date', 'home', 'away', 'score(H)', 'score(A)', 'Tournament', 'country']][df['home'].isin(['Spain'])]

#away = df[['date', 'home', 'away', 'score(H)', 'score(A)', 'Tournament', 'country']][df['away'].isin(['Japan'])]
away = df[['date', 'home', 'away', 'score(H)', 'score(A)', 'Tournament', 'country']][df['away'].isin(['Spain'])]

dataset1 = pd.concat([home, away], ignore_index = True)
dataset = pd.concat([home, away], ignore_index = True)

dataset['home'][dataset['home'] != 'Spain'] = 0
dataset['away'][dataset['away'] != 'Spain'] = 0
dataset['home'][dataset['home'] == 'Spain'] = 1
dataset['away'][dataset['away'] == 'Spain'] = 1


home1 = np.copy(dataset.iloc[0:, 1].values)
away1 = np.copy(dataset.iloc[0:, 2].values)

scoreH = np.copy(dataset.iloc[0:, 3].values)
scoreA = np.copy(dataset.iloc[0:, 4].values)

country_region = {}
country_region.update(dict.fromkeys(['Belarus', 'Czech Republic', 'Georgia', 
                                     'Poland', 'Romania', 'Russia', 
                                     'Slovakia', 'Ukraine'], '東欧'))

country_region.update(dict.fromkeys(['Austria', 'Belgium', 'France', 
                                     'Germany', 'Liechtenstein', 'Luxembourg', 
                                     'Netherlands', 'Switzerland'], '西欧'))

country_region.update(dict.fromkeys(['Albania', 'Croatia', 'Italy', 
                                     'Malta', 'North Macedonia', 'Portugal', 
                                     'Spain'], '南欧'))

country_region.update(dict.fromkeys(['England', 'Faroe Islands', 'Finland', 
                                     'Lithuania', 'Norway', 'Scotland', 
                                     'Sweden', 'Wales'], '北欧'))

country_region.update(dict.fromkeys(['Argentina', 'Brazil', 'Ecuador', 
                                     'Venezuela'], '南米'))

country_region.update(dict.fromkeys(['Costa Rica', 'Mexico', 'Panama', 
                                     'Puerto Rico', 'United States'], '北中米'))

country_region.update(dict.fromkeys(['Israel', 'Qatar'], 'アジア'))

country_region.update(dict.fromkeys(['Egypt', 'Equatorial Guinea', 'South Africa'], 'アフリカ'))

dataset['地域'] = dataset['country'].map(country_region)


sns.barplot(x = "地域", y = 'score(H)', 
            order = ['東欧', '西欧', '南欧', '北欧', '南米', '北中米', 'アジア', 'アフリカ'], 
            data=dataset[home1 == 0])

#sns.barplot(x = "地域", y = 'score(A)', 
#            order = ['東欧', '西欧', '南欧', '北欧', '南米', '北中米', 'アジア', 'アフリカ'], 
#            data=dataset[away1 == 0])

#fig = plt.figure()
#ax = Axes3D(fig)

#ax.scatter(scoreH[home1 == 1], scoreA[home1 == 1], 
#           scoreH[home1 == 1] - scoreA[home1 == 1],  color='red', marker='o', label="Spain(H)", linestyle='None')
#ax.scatter(scoreH[home1 == 0], scoreA[home1 == 0], 
#           scoreH[home1 == 0] - scoreA[home1 == 0],  color='blue', marker='o', label="Spain(A)", linestyle='None')
