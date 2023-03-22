#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df =pd.read_csv("zomato.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.columns


# In[6]:


df = df.drop(['url', 'address', 'phone', 'menu_item', 'dish_liked', 'reviews_list'], axis = 1)
df.head()


# In[7]:


df.info()


# # Dropping Duplicates

# In[8]:


df['name'].value_counts()


# In[9]:


df.drop_duplicates(inplace = True)
df.shape


# # Cleaning Rate Column

# In[10]:


df['rate'].unique()


# # Removing 'New' , '-' and '/5' from rate column

# In[11]:


df['rate'] = df['rate'].apply(lambda x: str(x).strip('/5'))


# In[12]:


df['rate'] = df['rate'].apply(lambda x: str(x).replace('NEW', 'nan'))
df['rate'] = df['rate'].apply(lambda x: str(x).replace('-', 'nan'))


# In[13]:


df['rate'] = df['rate'].astype(float)


# In[14]:


df['rate'].head()


# # Filling Null Values in Rate Column with Median

# In[15]:


df.rate.isnull().sum()


# In[17]:


df['rate'].fillna(df['rate'].median(),inplace = True)


# In[18]:


df.rate.isnull().sum()


# In[20]:


df.info()
df.shape


# # Removing Null Values

# In[22]:


df.dropna(inplace = True)


# In[23]:


df.head()


# In[26]:


df['location'].unique()


# In[27]:


df['listed_in(city)'].unique()


# location and listed in (city) both has similar data. So we can drop anyone of them

# In[30]:


df = df.drop(['listed_in(city)'], axis = 1)


# In[31]:


df.head()


# In[32]:


df['approx_cost(for two people)'].unique()


# # Removing ',' from approx_cost(for two people) Column

# In[44]:


df['approx_cost(for two people)'] = df['approx_cost(for two people)'].apply(lambda x: str(x).replace(',', ''))
df['approx_cost(for two people)'] = df['approx_cost(for two people)'].astype(float)


# In[40]:


df['approx_cost(for two people)'].unique()


# In[45]:


df.head()


# In[ ]:




