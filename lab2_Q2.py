#!/usr/bin/env python
# coding: utf-8

# In[23]:


def addst(a,b):
    final=""
    final+=b[0]
    final+=b[1]
    size=len(a)
    
    
    for i in range(2,size):
        final+=a[i]
    size=len(b)
    final+=' '
    final+=a[0]
    final+=a[1]
    for i in range(2,size):
        final+=b[i]
        
    return(final)
        


x=input('Enter first string : ')
y=input('Enter Second String : ')
print(x)
print(y)

print(addst(x,y))
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


dog
dinner

