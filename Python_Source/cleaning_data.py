#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os


# In[4]:


fileToLoad = "Resources/missing_grades.csv"

missingGradeDf = pd.read_csv(fileToLoad)
missingGradeDf


# In[5]:


missingGradeDf.dropna()


# In[6]:


missingGradeDf.fillna(85)


# In[7]:


missingGradeDf.dtypes


# In[ ]:




