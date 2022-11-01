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

# # Function

# In[36]:


def add_numbers(x, y):
    return x + y

add_numbers(x = 2, y = -3)


# In[40]:


def additionThreePara(x, y, z = None):
    if (z==None):
        return x+y
    else:
        return x+y+z
    
    
additionThreePara(1,2)


# In[43]:


def additionThreePara(x, y, z = 'add'):
    if (z=='add'):
        return x+y
    else:
        return x-y
    
    
additionThreePara(1,2)


# In[3]:


from sympy import Eijk, LeviCivita

print( LeviCivita(3, 1, 2) )
    


# # Exercises

# 1. Write a function to calculate the determinant using the Levi-Civita operator.
# 1. Create a Jupyter Notebook and solve this NB's questions.
# 1. Submmit your report in Moodle. Template https://www.overleaf.com/read/xqcnnnrsspcp
