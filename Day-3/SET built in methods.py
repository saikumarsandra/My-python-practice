#!/usr/bin/env python
# coding: utf-8

# In[9]:


s={1,2,3}
print(s)


# In[11]:


type(s)


# In[14]:


s.add(4)
s


# In[19]:


s.update({5,6})
s


# In[20]:


s.remove(5)
s


# In[21]:


s.discard(1)
s


# In[22]:


s.pop()
s


# In[38]:


x = {"apple", "banana", "cherry","google"}
y = {"google", "microsoft", "apple"}

z = y.difference(x) 

print(z)


# In[30]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y) 

print(z)


# In[32]:


new_set=s.copy()
new_set


# In[39]:


u={1,2,3,5,6}
v={4,9,8,7,0}
uni=u.union(v)
uni


# In[40]:


q={1,2,3,5,6}
i={4,2,3,5,0}
u_set=q.union(i)
u_set


# In[41]:


q={1,2,3,5,6}
i={4,2,3,5,0}
i_set=q.intersection(i)
i_set


# In[42]:


q={1,2,3,5,6}
i={4,2,3,5,0}
semDiff_set=q.symmetric_difference(i)
semDiff_set


# In[44]:


q={1,2,5,5,6}
i={4,2,3,5,0}
semDiff_set=i.symmetric_difference(q)
semDiff_set


# In[47]:


q.clear()
i.clear()

