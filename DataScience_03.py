#!/usr/bin/env python
# coding: utf-8

# # Data Science
# #### By: Javier Orduz
# [license-badge]: https://img.shields.io/badge/License-CC-orange
# [license]: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en
# 
# [![CC License][license-badge]][license]  [![DS](https://img.shields.io/badge/downloads-DS-green)](https://github.com/Earlham-College/DS_Fall_2022)  [![Github](https://img.shields.io/badge/jaorduz-repos-blue)](https://github.com/jaorduz/)  ![Follow @jaorduc](https://img.shields.io/twitter/follow/jaorduc?label=follow&logo=twitter&logoColor=lkj&style=plastic)
# 
# ## Contents
# 1. [List and Tuples](#list_tuples)
# 1. [Exercises](#exercises)
# 1. [References](#references)

# # Lists and Tuples <a name="list_tuples"></a>

# In short, a list is a collection of arbitrary objects, somewhat akin to an array in many other programming languages but more flexible. **Lists are defined in Python by enclosing a comma-separated sequence of objects in square brackets** [1], as shown below:

# ## Same type

# In[1]:


a = ['foo', 'bar', 'baz', 'qux']


# In[2]:


a


# In[3]:


b = [1, 2, 3, 4]


# In[4]:


b


# ## Different type

# In[5]:


c = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]


# In[6]:


c


# Even lists can contain functions, classes, and modules.
# Each list assignes index for all elements starting from 0 (from left or -1 starting from right).

# In[7]:


c[0]


# In[8]:


a[-1]


# # Part of the list

# In[9]:


b[1:3]


# ## Operating with lists

# In[10]:


a + b


# # Mutable
# 
# It can be changed once they have been assigned.

# ##  Tuples

# 1. Tuples are **immutables**

# In[11]:


e = (1, 2, 3)


# In[12]:


e


# In[13]:


e[0]


# Reversal mechanism

# In[14]:


e[::-1]


# - Program execution is faster when manipulating **tuples**
# - Sometimes we want immutable data
# - Dictionarie concept uses the immutable propierty.

# # Packing and unpacking 

# In[15]:


(v1, v2, v3) = (2, 20, 200)


# In[16]:


v3


# You can test it without parenthesis.

# # Modifying 

# In[17]:


d = [1,2,3,4,5,6,7,8]


# In[18]:


d[1:6]=[9]


# In[19]:


d


# We replace a specific slice of the list with a new value```d[1:6]=[9]```

# # Dictionaries

# A dictionary is a collection which is 
#     - **ordered**, 
#     - **changeable** and 
#     - **does not allow duplicates**.
# 
# Dictionaries are used to store data values in ```key:value```pairs.
# 
# 

# In[20]:


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# In[21]:


print(thisdict["brand"])


# # Set

# Sets are used to store multiple items in a single variable.
# A set is a collection which is **unordered, unchangeable**, and **unindexed**.

# In[22]:


myset = {"apple", "banana", "cherry"} 


# The items in the set 
#     - do not have a defined order.
#     - Set items cannot be changed after the set has been created.
#     - and cannot be referred to by index or key

# In[4]:


x=[]
x.append('a')
x.append(['bb',['ccc','ddd'],'ee','ff'])
x.append('g')
x.append(['hh','ii'])
x.append('j')
print(x)


# In[18]:


v = ('a','bb','ccc','ddd','ee','ff','g','hh','ii','j')

x2 = v[2:4]
x3 = (v[1],x2,v[4],v[5])
result =(v[0],x3,v[6],v[7:9],v[9])
print(result)


# # Exercises <a name="exercises"></a>

# 1. Create the list for the next diagram
# 
# [<img src="https://files.realpython.com/media/t.08554d94a1e5.png">](https://files.realpython.com/media/t.08554d94a1e5.png)
# 
# <!---
# 
# ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
# --->

# 2. Implement some examples with methods such as
#     - ```append```
#     - ```upper```
#     - ```extend```
#     - ```insert```
#     - ```remove```
#     - ```pop```

# 3. Apply basic operations with tuples
# 4. Create a Jupyter Notebook and solve this NB's questions.
# 5. Submmit your report in Moodle. Template https://www.overleaf.com/read/xqcnnnrsspcp

# ## Versions

# In[23]:


from platform import python_version
print("python version: ", python_version())
get_ipython().system('pip3 freeze | grep qiskit')


# # References <a name="references"></a>

# [1] https://realpython.com/python-lists-tuples/
