#!/usr/bin/env python
# coding: utf-8

# # Data Science
# #### By: Javier Orduz
# [license-badge]: https://img.shields.io/badge/License-CC-orange
# [license]: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en
# 
# [![CC License][license-badge]][license]
# 
# [![DS](https://img.shields.io/badge/downloads-DS-green)](https://github.com/Earlham-College/DS_Fall_2022)
# 
# [![Github](https://img.shields.io/badge/jaorduz-repos-blue)](https://github.com/jaorduz/)
# 
# ![Follow @jaorduc](https://img.shields.io/twitter/follow/jaorduc?label=follow&logo=twitter&logoColor=lkj&style=plastic)
# 
# 
# 
# ## Contents
# 1. [List and Tuples](#list_tuples)
# 1. [Exercises](#exercises)
# 1. [References](#references)

# We call the package

# In[8]:


import numpy as np


# We create an set of random mumbers.

# In[9]:


data = {i : np.random.randn(2,4) for i in range(3)}


# We print the data with the label from $i= 0$ to $i= 6$

# In[12]:


print(data)
print(sum(data)/len(data))


# In[19]:


print(data[0])
print(sum(data[0])/len(data[0]))


# In[20]:


print(data[0][0])
print(sum(data[0][0])/len(data[0][0]))


# This is how we extract the 000 element

# In[22]:


data[0][0][0]


# # Exercise

# 1. Add documentation for the previous code, each line.
# 1. Calculate the average for the different columns
# 1. Discuss differences between List and tuples.
# 4. Create a Jupyter Notebook and solve this NB's questions.
# 5. Submmit your report in Moodle. Template https://www.overleaf.com/read/xqcnnnrsspcp

# 
