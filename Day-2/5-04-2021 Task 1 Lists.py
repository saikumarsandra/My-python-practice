#!/usr/bin/env python
# coding: utf-8

# In[1]:


shoplist=['apple','mango','carrot','banana']
shoplist


# In[3]:


shoplist.append('rice')
shoplist


# In[5]:


shoplist.pop()
shoplist


# In[6]:


shoplist.extend(['milk','bread','boost'])
shoplist


# In[7]:


shoplist.insert(1,"orange")
shoplist


# In[9]:


shoplist.remove("orange")
shoplist


# In[26]:


shoplist.count("apple")


# In[28]:


shoplist.sort()
shoplist


# In[29]:


shoplist.reverse()
shoplist


# In[31]:


final_list=shoplist.copy()
final_list


# In[38]:


final_list.index('milk')


# In[41]:


shoplist
all(shoplist)


# In[44]:


any(shoplist)


# In[63]:


enum = enumerate(shoplist)
print(tuple(enum))


# In[64]:


enum = enumerate(shoplist)
print(list(enum))


# In[65]:


len(shoplist)


# In[66]:


list(shoplist)


# In[67]:


max(shoplist)


# In[68]:


min(shoplist)


# In[69]:


sorted(shoplist)


# In[86]:


l=[7,8,9,4,5,6,1,2,3]
s=sum(l,3)
s


# In[96]:


txt="i have {}items to purchase"
print(txt.format(len(shoplist)))


# In[99]:


print(shoplist[:-3])


# %%
