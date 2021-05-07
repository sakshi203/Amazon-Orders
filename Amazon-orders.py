#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
df = pd.read_csv('C:\\Users\\Sakshi\\Downloads\\amazon-orders.csv')
df.head()


# In[40]:


df.shape


# In[41]:


df = df.fillna(0)
df.head()


# In[51]:


df["Total Charged"] = df["Total Charged"].str.replace('$','').astype(float)
df.head()


# In[52]:


df["Total Charged"].sum()


# In[53]:


df["Total Charged"].mean()


# In[54]:


df["Total Charged"].median()


# In[55]:


df["Total Charged"].max()


# In[56]:


df["Total Charged"].min()


# In[57]:


df["Tax Charged"] = df["Tax Charged"].str.replace('$','').astype(float)
df.head()


# In[58]:


df["Tax Charged"].sum()


# In[59]:


df["Tax Charged"].sum()/df["Total Charged"].sum()


# In[61]:


df['Order Date'] = pd.to_datetime(df['Order Date'])
df.head()


# In[62]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[65]:


df.plot.bar(x='Order Date', y='Total Charged', rot=90)


# In[67]:


df.plot.bar(x='Order Date', y='Total Charged', rot=90, figsize=(20,10))


# In[68]:


daily_orders = df.groupby('Order Date').sum()["Total Charged"]
daily_orders.head()


# In[69]:


daily_orders.plot.bar(figsize=(20,10))

