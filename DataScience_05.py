#!/usr/bin/env python
# coding: utf-8

# # Data Science
# #### By: Javier Orduz
# [license-badge]: https://img.shields.io/badge/License-CC-orange
# [license]: https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en
# 
# [![CC License][license-badge]][license]  [![DS](https://img.shields.io/badge/downloads-DS-green)](https://github.com/Earlham-College/DS_Fall_2022)  [![Github](https://img.shields.io/badge/jaorduz-repos-blue)](https://github.com/jaorduz/)  ![Follow @jaorduc](https://img.shields.io/twitter/follow/jaorduc?label=follow&logo=twitter&logoColor=lkj&style=plastic)
# 

# # Documents, words, and tokenization

# In[6]:


f = open("hamlet.txt", "r")


# In[7]:


ftext = f.read()


# In[8]:


f.close()


# In[9]:


ftokens = ftext.split()


# ## Firsts 7 elements

# In[10]:


print(ftext[:7])


# In[11]:


print(ftext)


# In[12]:


print(ftokens)


# In[13]:


print("The number of words is ", len(ftokens))


# ## Last elements

# In[14]:


print(ftext[-10:])


# ## Tokens

# In[15]:


print(ftokens[1:4])


# ## Picking some words

# Get every 2nd word between the 1st and the 3th: i.e. 1st, and 3th.

# In[16]:


print(ftokens[1:4:2])


# In[17]:


print(ftokens[1:4]+ftokens[1:4:2])


# In[18]:


fstring="-".join(ftokens[1:4:2])


# In[24]:


print(fstring)


# In[ ]:


for i in range(len(ftokens)):
    if( len(ftokens[i])) == 20:
        print(ftokens[i])


# In[34]:


my_dict = {i:ftokens.count(i) for i in ftokens}

print (my_dict)


# In[52]:


import matplotlib.pyplot as plt

unique = []
names = []
for i in my_dict:
    if my_dict[i] >150:
        unique.append((my_dict[i]))
        names.append(i)
        
plt.bar(unique, names)
plt.title('Words Vs Count')
plt.show()


# ##  Exercises

# 1. Investigate more operations with tokens.
# 2. Count the different words.
# 3. Plot a bar chart
# 4. Submmit your report in Moodle. Template https://www.overleaf.com/read/xqcnnnrsspcp

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

# In[ ]:




