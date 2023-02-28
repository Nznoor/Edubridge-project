#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import packages in python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# In[9]:


#read iris dataset
Data=pd.read_excel('iris.xls')
Data.head()


# In[16]:


# to delete the column ie target
Data=Data.drop(columns=['target'])
Data.head()


# In[28]:


#Histogram
Data['sepal width (cm)'].hist()
plt.savefig('histogram')
plt.show()


# In[29]:


Data['sepal length (cm)'].hist()


# In[34]:


#to display no of sample on each class
Data['sepal width (cm)'].value_counts()


# In[39]:


# check for null values
Data.isnull().sum()


# In[ ]:





# In[ ]:




