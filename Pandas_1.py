#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd


# In[15]:


seri_1 = pd.Series([1,2,3,4,5,6])


# In[16]:


print(seri_1)


# In[17]:


print(seri_1.index)


# In[21]:


import pandas as pd

seri_2 = pd.Series([178, 160, 180, 165, 179], index=['Ahmet', 'Elif', 'Mehmet', 'Hatice', 'Ali'])


# In[22]:


print(seri_2)


# In[23]:


seri_2.index = ["sıra 1","sıra 2","sıra 3","sıra 4","sıra 5"]


# In[24]:


print(seri_2)


# In[ ]:




