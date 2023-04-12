#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("./FPData2.csv")
df.head()


# In[2]:


df.columns = ['Country', 'year', 'ladder', 'gdp', 'support', 'life_expec', 'freedom', 'generosity','corruption','positive', 'negative']
df.head()


# In[3]:



import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[49]:


df.isnull().sum()


# In[75]:


df.groupby('year').size()


# In[11]:


import plotly.express as px
df22 = df.loc[(df.year == 2022)]
df22.head()


# In[12]:


fig = px.choropleth(df22,
                    locationmode='country names',
                    locations='Country',
                    color='ladder',
                    title='Countries by Ladder Score'
                   )
fig.show()


# In[ ]:





# In[54]:


df_means = df.groupby(['year']).mean()
df_means


# In[71]:


df_means = df_means.drop([2005])


# In[74]:


x_labels = [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
#Plotting the means for each year, removing 2005, due to missing data
fig, axs = plt.subplots(2, 4, figsize=(14,8))
axs[0, 0].plot(x_labels, df_means['ladder'])
axs[0, 0].set_title('Ladder')
axs[0, 1].plot(x_labels, df_means['generosity'])
axs[0, 1].set_title('Generosity')
axs[1, 0].plot(x_labels, df_means['life_expec'])
axs[1, 0].set_title('Life Expectency')
axs[1, 1].plot(x_labels, df_means['freedom'])
axs[1, 1].set_title('Freedom')
axs[0, 2].plot(x_labels, df_means['support'])
axs[0, 2].set_title('Social Support')
axs[0, 3].plot(x_labels, df_means['corruption'])
axs[0, 3].set_title('Corruption')
axs[1, 2].plot(x_labels, df_means['positive'])
axs[1, 2].set_title('Positive Affect')
axs[1, 3].plot(x_labels, df_means['negative'])
axs[1, 3].set_title('Negative Affect')


# In[ ]:




