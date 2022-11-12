#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
bigdata=pd.read_csv('D:/New folder/archive/archive (4)/netflix_titles.csv')


# In[2]:


bigdata


# In[3]:


bigdata.head()


# In[4]:


bigdata.tail()


# In[5]:


bigdata.shape


# In[6]:


bigdata.size


# In[7]:


bigdata.columns


# In[8]:


bigdata.dtypes


# In[9]:


bigdata.info()


# In[11]:


bigdata[bigdata.duplicated()]


# In[16]:


bigdata.drop_duplicates(inplace=True)


# In[17]:


bigdata.shape


# In[18]:


bigdata.isnull()


# In[19]:


bigdata.isnull().sum()


# In[24]:


import seaborn as sns
sns.heatmap(bigdata.isnull())


# In[25]:


bigdata.head()


# In[28]:


bigdata[bigdata['title'].isin(['House of Cards'])]


# In[29]:


bigdata.dtypes


# In[30]:


bigdata['Date_N']=pd.to_datetime(bigdata['release_year'])


# In[31]:


bigdata.head()


# In[32]:


bigdata.dtypes


# In[34]:


bigdata['Date_N'].dt.year.value_counts()


# In[ ]:




