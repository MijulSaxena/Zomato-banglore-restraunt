#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df =pd.read_csv("zomato.csv")


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.columns


# In[10]:


df = df.drop(['url', 'address', 'phone', 'menu_item', 'dish_liked', 'reviews_list'], axis = 1)
df.head()


# In[11]:


df.info()


# # Dropping Duplicates

# In[14]:


df['name'].value_counts()


# In[16]:


df.drop_duplicates(inplace = True)
df.shape


# # Cleaning Rate Column

# In[17]:


df['rate'].unique()


# # Removing 'New' , '-' and '/5' from rate column

# In[21]:


df['rate'] = df['rate'].apply(lambda x: str(x).strip('/5'))


# In[22]:


df['rate'] = df['rate'].apply(lambda x: str(x).replace('NEW', 'nan'))
df['rate'] = df['rate'].apply(lambda x: str(x).replace('-', 'nan'))


# In[28]:


df['rate'] = df['rate'].astype(float)


# In[29]:


df['rate'].head()


# # Removing null values

# In[30]:


df.rate.isnull().sum()


# In[ ]:




