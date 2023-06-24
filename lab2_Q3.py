#!/usr/bin/env python
# coding: utf-8

# In[28]:



def checkfl(a):
    count=0
    if(a[0]==a[-1]):
        count+=1
    return count

list=['home','classroom' ,'car' ,'window' , 'house' , 'clam']

size=len(list)
k=0
i=0
count=0
while(i<size):
    temp=''
    current=list[i]
    temp=current[0]
    temp+=current[-1]
    i+=1
    j=i
    while(j<size):
        temp2=''
        current2=list[j]
        temp2=current2[0]
        temp2+=current2[-1]
        if temp==temp2:
            count+=1
        j+=1
        
  
    
    
print(count)


# In[ ]:





# In[ ]:





# In[ ]:




