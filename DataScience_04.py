#!/usr/bin/env python
# coding: utf-8

# # Data Science
# #### By: Javier Orduz
# [license-badge]: https://img.shields.io/badge/License-CC-orange
# [license]: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en
# 
# [![CC License][license-badge]][license]  [![DS](https://img.shields.io/badge/downloads-DS-green)](https://github.com/Earlham-College/DS_Fall_2022)  [![Github](https://img.shields.io/badge/jaorduz-repos-blue)](https://github.com/jaorduz/)  ![Follow @jaorduc](https://img.shields.io/twitter/follow/jaorduc?label=follow&logo=twitter&logoColor=lkj&style=plastic)
# 

# # Importing different modules

# ## Imports ```numpy```

# ### A numerical programming library

# In[1]:


import numpy as np


# ```Numpy``` check some documentation [1]

# ##  Imports statistics functions and more

# In[97]:


import scipy as sp 
from scipy import cbrt


# ```scipy``` check some documentation [2]

# ## Imports ```matplotlib```

# In[3]:


import matplotlib as mpl


# ```matplotlib``` check come documentation [3]

# ### Module: to access to colormaps

# In[4]:


import matplotlib.cm as cm


# ```matplotlib.cm``` check some documentation [4]

# ### Module: to set up plotting under plt

# In[5]:


import matplotlib.pyplot as plt


# ```matplotlib.pyplot``` check some documentation [5]

# ## Imports ```pandas``` to use data as dataframes

# In[6]:


import pandas as pd


# ```pandas``` check some documentation [6]

# ### Option to manipulate size and more

# In[7]:


#sets up pandas table display
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 100)
pd.set_option('display.notebook_repr_html', True)


# ## Line to embed plots

# In[9]:


get_ipython().run_line_magic('matplotlib', 'in inline')


# ## Imports ```seaborn```

# ### sets up styles and gives us more plotting options

# In[10]:


import seaborn as sns


# In[12]:


alist=[1,2,3,4,5]
for i in range(len(alist)):
    alist[i]=alist[i]**2
print(alist)


# In[13]:


df=pd.read_csv("books.csv", header=None,
    names=["rating", 'review_count', 'isbn', 
    'booktype','author_url', 'year', 'genre_urls', 
    'dir','rating_count', 'name'],
)
df.head()


# In[106]:


#first and last books in the file
ratings = []
plots=[]
for i in df:
    v = np.array ((df))
print(v)
for i in range(5):
        plots.append(cbrt(v[i][0]))
        
plt.plot(plots)
plt.ylabel('some numbers')
plt.show()


# ```seaborn``` check some documentation [7]

# # Exercises

# 1. Consider this list ```alist=[1,2,3,4,5]```, obtain with an interation a new list with the i-element-squared
# ```output -> [1,4,6,16,25]```
# 
# <!---
# alist=[1,2,3,4,5]
# asquaredlist=[i*i for i in alist]
# asquaredlist
# --->
# 2. Create a Jupyter Notebook where you implement some functions, methods, and different parameters with each module/package. Check **NB_Examples** folder.
# 3. Submmit your report in Moodle. Template https://www.overleaf.com/read/xqcnnnrsspcp

# ## Versions

# In[ ]:


from platform import python_version
print("python version: ", python_version())
get_ipython().system('pip3 freeze | grep qiskit')


# # References

# [1] numpy https://numpy.org/
# 
# [2] scipy https://docs.scipy.org/
# 
# [3] matplotlib https://matplotlib.org/
# 
# [4] matplotlib.cm https://matplotlib.org/stable/api/cm_api.html
# 
# [5] matplotlib.pyplot https://matplotlib.org/stable/api/pyplot_summary.html
# 
# [6] pandas https://pandas.pydata.org/docs/
# 
# [7] seaborn https://seaborn.pydata.org/
