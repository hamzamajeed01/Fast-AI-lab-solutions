#!/usr/bin/env python
# coding: utf-8

# In[1]:


tuple = [(1, 24), (2, 10), (3, 28),
       (6, 5), (6, 20), (7, 15)]
 
def SortedTuple(tuple):
 

    getlist = len(tuple)
    for i in range(0, getlist):
 
        for j in range(0, getlist-i-1):
            if (tuple[j][1] > tuple[j + 1][1]):
                temp = tuple[j]
                tuple[j] = tuple[j + 1]
                tuple[j + 1] = temp
    return tuple
 
 

print(SortedTuple(tuple))


# In[ ]:




