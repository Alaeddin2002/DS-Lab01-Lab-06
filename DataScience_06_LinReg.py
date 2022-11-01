#!/usr/bin/env python
# coding: utf-8

# # Data Science
# #### By: Javier Orduz
# [license-badge]: https://img.shields.io/badge/License-CC-orange
# [license]: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en
# 
# [![CC License][license-badge]][license]  [![DS](https://img.shields.io/badge/downloads-DS-green)](https://github.com/Earlham-College/DS_Fall_2022)  [![Github](https://img.shields.io/badge/jaorduz-repos-blue)](https://github.com/jaorduz/)  ![Follow @jaorduc](https://img.shields.io/twitter/follow/jaorduc?label=follow&logo=twitter&logoColor=lkj&style=plastic)
# 

# In[31]:


import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
import statistics
get_ipython().run_line_magic('matplotlib', 'inline')


# # Part I: Simpler Linear Regression. Knowing data

# Data source [0].

# <h1>Table of contents</h1>
# 
# <div class="alert  alert-block alert-info" style="margin-top: 20px">
#     <ol>
#         <li><a href="#unData">Data</a></li>
#          <ol>
#              <li><a href="#reData">Reading</a></li>
#              <li><a href="#exData">Exploration</a></li>
#          </ol>
#         <li><a href="#daExploration">Data Exploration</a></li>
#         <li><a href="#simRegression">Simple Regression Model</a></li>
#     </ol>
# </div>
# <br>
# <hr>

# 
# <h2 id="unData">Data</h2>
# 
# ### `FuelConsumption.csv`:
# 
# This dataset contains a model-specific fuel consumption ratings and estimated carbon dioxide 
# emissions for new light-duty vehicles for retail sale in Canada.
# 
# Some **features** are
# 
# - **MODELYEAR** e.g. 2014
# - **MAKE** e.g. Acura
# - **MODEL** e.g. ILX
# - **VEHICLE CLASS** e.g. SUV
# - **ENGINE SIZE** e.g. 4.7
# - **CYLINDERS** e.g 6
# - **TRANSMISSION** e.g. A6
# - **FUEL CONSUMPTION in CITY(L/100 km)** e.g. 9.9
# - **FUEL CONSUMPTION in HWY (L/100 km)** e.g. 8.9
# - **FUEL CONSUMPTION COMB (L/100 km)** e.g. 9.2
# - **CO2 EMISSIONS (g/km)** e.g. 182   --> low --> 0

# In[2]:


df = pd.read_csv("FuelConsumption.csv")


# <h3>Dataframe</h3>
# 
# <div class="alert  alert-block alert-info" style="margin-top: 20px">
#     A DataFrame represents a rectangular table of data and contains an ordered collection 
#     of columns, each of which can be a different value type (numeric, string, boolean, etc.). 
#     The DataFrame has both a row and column index; it can be thought of as a dict 
#     of Series all sharing the same index. Under the hood, the data is stored as one or 
#     more two-dimensional blocks rather than a list, dict, or some other collection of 
#     one-dimensional arrays.
# </div>
# <br>
# <hr>

# In[3]:


df.dtypes


# In[4]:


df.shape


# In[5]:


print("Number of rows =", df.shape[0], "\nNumber of features (columns) =",df.shape[1])


# In[6]:


df.columns


# In[7]:


type(df)


# In[8]:


df.head()


# In[9]:


df.head(7)


# In[10]:


df.describe()


# ## Querying
# 
# Note, pandas considers a table (dataframe) as a pasting of many "series" together, horizontally.

# In[11]:


type(df.MODELYEAR), type(df)


# In[12]:


df.ENGINESIZE <= 2


# In[13]:


SumEng = np.sum(df.ENGINESIZE <= 2)
SumEng


# In[14]:


SumEngTotal = np.sum(df.ENGINESIZE <= 2)/df.shape[0]
SumEngTotal


# In[15]:


MeanTotal = np.mean(df.ENGINESIZE <= 2.0)
MeanTotal


# In[16]:


EngMean = (df.ENGINESIZE <= 2).mean()
EngMean


# In[17]:


AverageEng = np.average(df.ENGINESIZE <= 2.0)
AverageEng


# In[23]:


Cylmean = (df.CYLINDERS).mean()
Cylmean


# In[24]:


Cylaverage = np.average(df.CYLINDERS)
Cylaverage


# In[25]:


Cylmedian = np.median(df.CYLINDERS)
Cylmedian


# In[26]:


Cylsum = np.sum(df.CYLINDERS)
Cylsum


# In[32]:


Cylvar = statistics.variance(df.CYLINDERS)
Cylvar


# In[34]:


Cylcount = (df.CYLINDERS).count()
Cylcount


# In[35]:


Cylmin = (df.CYLINDERS).min()
Cylmin


# In[36]:


Cylmax = (df.CYLINDERS).max()
Cylmax


# ##  Exercises

# 1. Why previous outputs are same?
# 1. Use at least four more features and calculate: average, mean, median, sum, and implement at least three more statistics functions. Check the ```numpy``` and ```pandas``` documentation.
# 1. Submmit your report in Moodle. Template https://www.overleaf.com/read/xqcnnnrsspcp

# ## Versions

# In[23]:


from platform import python_version
print("python version: ", python_version())
get_ipython().system('pip3 freeze | grep qiskit')


# # References

# [0] data https://tinyurl.com/2m3vr2xp
# 
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
# 

# In[ ]:




