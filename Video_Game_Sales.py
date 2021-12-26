# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 18:07:02 2021

@author: Herman
"""
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

vg_data = pd.read_csv('Video_Games.csv')

vg_data.describe().to_csv('Video_Games_Summary.csv')

vg_data_UserScore = vg_data[vg_data['User_Score']!='tbd']
vg_data_UserScore['User_Score'] = vg_data_UserScore['User_Score'].astype(float)

fig1, ax1 = plt.subplots()


sns.histplot(data = vg_data['Critic_Score'].dropna(), ax = ax1, stat = 'probability', binwidth=2,
             binrange = (0,100))

fig2, ax2 = plt.subplots()

sns.histplot(data = vg_data_UserScore['User_Score'].dropna(), ax = ax2, 
             stat = 'probability', binwidth=0.5, binrange = (0,10))




