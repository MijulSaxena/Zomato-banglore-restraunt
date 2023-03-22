#!/usr/bin/env python
# coding: utf-8

# In[54]:


import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
import seaborn as sns


# In[55]:


df =pd.read_csv("zomato.csv")


# In[56]:


df.head()


# In[57]:


df.shape


# In[58]:


df.columns


# In[59]:


df = df.drop(['url', 'address', 'phone', 'menu_item', 'dish_liked', 'reviews_list'], axis = 1)
df.head()


# In[60]:


df.info()


# # Dropping Duplicates

# In[61]:


df['name'].value_counts()


# In[62]:


df.drop_duplicates(inplace = True)
df.shape


# # Cleaning Rate Column

# In[63]:


df['rate'].unique()


# # Removing 'New' , '-' and '/5' from rate column

# In[64]:


df['rate'] = df['rate'].apply(lambda x: str(x).strip('/5'))


# In[65]:


df['rate'] = df['rate'].apply(lambda x: str(x).replace('NEW', 'nan'))
df['rate'] = df['rate'].apply(lambda x: str(x).replace('-', 'nan'))


# In[66]:


df['rate'] = df['rate'].astype(float)


# In[67]:


df['rate'].head()


# # Filling Null Values in Rate Column with Median

# In[68]:


df.rate.isnull().sum()


# In[69]:


df['rate'].fillna(df['rate'].median(),inplace = True)


# In[70]:


df.rate.isnull().sum()


# In[71]:


df.info()
df.shape


# # Removing Null Values

# In[72]:


df.dropna(inplace = True)


# In[73]:


df.head()


# In[74]:


df['location'].unique()


# In[75]:


df['listed_in(city)'].unique()


# location and listed in (city) both has similar data. So we can drop anyone of them

# In[76]:


df = df.drop(['listed_in(city)'], axis = 1)


# In[77]:


df.head()


# In[78]:


df['approx_cost(for two people)'].unique()


# # Removing ',' from approx_cost(for two people) Column

# In[79]:


df['approx_cost(for two people)'] = df['approx_cost(for two people)'].apply(lambda x: str(x).replace(',', ''))
df['approx_cost(for two people)'] = df['approx_cost(for two people)'].astype(float)


# In[80]:


df['approx_cost(for two people)'].unique()


# In[81]:


df.head()

