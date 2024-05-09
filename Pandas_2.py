#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


seri_not = pd.Series([50,55,67,90,78])
seri_not


# In[3]:


seri_not.index = ["3489","4526","7825","1978","9183"]
seri_not


# In[4]:


type(seri_not)


# In[5]:


for i in seri_not.values:
    if i > 50:
        print("Geçti")
    else:
        print("Kaldı")


# In[6]:


seri_final = pd.Series({'3467':80,'3478':45,'3489':34,'3412':78,'3490':55})


# In[7]:


print(seri_final)


# In[8]:


seri_final.values


# In[9]:


#vize notları ile final notlarını toplayıp,ikiye bölelim.
#vize ve final ortalaması hesaplatalım.


# In[16]:


import numpy as np
son_not = (seri_not.values* 0.4) + (seri_final.values* 0.6)
print(son_not)


# In[17]:


son_not = pd.Series(son_not, index=["öğrenci 1","öğrenci 2","öğrenci 3","öğrenci 4","öğrenci 5",])


# In[18]:


print(son_not)


# In[19]:


for i in son_not.values:
    if i > 50:
        print("Geçtiniz!")
    else:
        print("Kaldınız!")


# In[20]:


# Vize ve final notlarını tek bir seride birleştirelim.


# In[22]:


birlesik_not = pd.concat([seri_not,seri_final])
print(birlesik_not)


# In[23]:


#DataFrame 
#DataFrame, tamamen tablo mantığına göre çalışır.
#Series'den en önemli farklı birden fazla sütun değerinin olmasıdır.


# In[24]:


#ilk DataFrame tanımlama
my_def = pd.DataFrame([80,56,67,23,44,67,89,45])
print(my_def)


# In[25]:


my_def.index = ["ogr-1","ogr-2","ogr-3","ogr-4","ogr-5","ogr-6","ogr-7","ogr-8",]
print(my_def)


# In[31]:


my_def.columns = {"Notlar"}
my_def


# In[34]:


my_dic = {'Vize':seri_not.values,'Final':seri_final.values,'Geçme Notu':son_not.values}
my_def1= pd.DataFrame(my_dic)
print(my_def1)


# In[35]:


my_def1.index = ['öğrenci 1','öğrenci 2','öğrenci 3','öğrenci 4','öğrenci 5']
my_def1


# In[36]:


my_def1["Mantıksal Geçme Notu"] = my_def1["Geçme Notu"] > 50
print(my_def1)


# In[ ]:




