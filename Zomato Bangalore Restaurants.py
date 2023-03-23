#!/usr/bin/env python
# coding: utf-8

# # About this file
# The basic idea of analyzing the Zomato dataset is to get a fair idea about the factors affecting the aggregate rating of each restaurant, establishment of different types of restaurant at different places, Bengaluru being one such city has more than 12,000 restaurants with restaurants serving dishes from all over the world. With each day new restaurants opening the industry has'nt been saturated yet and the demand is increasing day by day. Inspite of increasing demand it however has become difficult for new restaurants to compete with established restaurants. Most of them serving the same food. Bengaluru being an IT capital of India. Most of the people here are dependent mainly on the restaurant food as they don't have time to cook for themselves. With such an overwhelming demand of restaurants it has therefore become important to study the demography of a location. What kind of a food is more popular in a locality. Do the entire locality loves vegetarian food. If yes then is that locality populated by a particular sect of people for eg. Jain, Marwaris, Gujaratis who are mostly vegetarian. These kind of analysis can be done using the data, by studying different factors.

# In[60]:


import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
import seaborn as sns


# In[61]:


#reading csv file
df =pd.read_csv("zomato.csv")


# df.head(10)

# In[63]:


df.shape


# # Data Cleaning

# In[64]:


df.columns


# In[65]:


df['location'].unique()


# In[66]:


df['listed_in(city)'].unique()


# **location and listed in (city) both has similar data. So we can drop anyone of them.**

# In[67]:


# dropping unnessary columns
df = df.drop(['url', 'address', 'phone', 'menu_item', 'dish_liked', 'reviews_list','listed_in(city)'], axis = 1)
df.head()


# In[68]:


df.info()


# In[69]:


df['name'].value_counts()


# In[70]:


# dropping duplicates
df.drop_duplicates(inplace = True)
df.shape


# In[71]:


df.head()


# In[72]:


# renaming the columns which has very long name
df.rename(columns={'approx_cost(for two people)':'cost2people', 'listed_in(type)':'type'}, inplace = True)
df.head()


# **Cleaning Rate Column**

# In[73]:


df['rate'].unique()


# **Removing 'New' , '-' and '/5' from rate column**

# In[74]:


df['rate'] = df['rate'].apply(lambda x: str(x).strip('/5'))
df['rate'] = df['rate'].apply(lambda x: str(x).replace('NEW', 'nan'))
df['rate'] = df['rate'].apply(lambda x: str(x).replace('-', 'nan'))


# In[75]:


# Converting the type of rate column
df['rate'] = df['rate'].astype(float)


# In[76]:


df['rate'].head()


# **Filling Null Values in Rate Column with Median**

# In[77]:


# checking null values in rate column
df.rate.isnull().sum()


# In[78]:


df['rate'].fillna(df['rate'].median(),inplace = True)


# In[79]:


df.rate.isnull().sum()


# In[80]:


df.info()
df.shape


# **Dealing with null values -**
# As we can see there are still some null values in other columns, which are compartively low. So, we can drop those.

# In[81]:


df.dropna(inplace = True)


# In[82]:


df.head()


# **Cleaning cost2people column**

# In[84]:


df['cost2people'].unique()


# **Removing ',' from cost2people Column**

# In[87]:


df['cost2people'] = df['cost2people'].apply(lambda x: str(x).replace(',', ''))
df['cost2people'] = df['cost2people'].astype(float)


# In[88]:


df['cost2people'].unique()


# In[89]:


df.head()


# # Data Visualzation 

# In[91]:


plt.figure(figsize = (20,10))
ax = sns.countplot(df['location'])
plt.xticks(rotation=90)


# In[ ]:




