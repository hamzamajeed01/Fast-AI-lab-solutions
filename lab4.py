# -*- coding: utf-8 -*-
"""Lab4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TqtAbp6vvCxNxelpFY42waXUaeD1PEJF
"""

#Q1
setX={'a','b',1,3,5,'y'}
setY={'w','y',4,3,5,'z'}
print(setX.symmetric_difference(setY))

#Q2
def division(P,Q):
  return P/Q

try:
  print(division(10,10))
except ValueError:
  print('You should have given either an int or a float')
except ZeroDivisionError:
  print('You are dividing by zero')
except ImportError:
  print('Wrong library')
except IndentationError:
  print('Intendation not specified properly')

#Q3
def my_function(x):
  return x[::-1]

file=open('/content/Alphabets.txt','r')
file2=open('/content/reverse.txt','w')
list=[]
for each in file:
  list.append(each)
i=len(list)-1
while(i>=0):
  list2=list[i]
  i=i-1
  list2=my_function(list2)
  file2.write(list2)
file2.close()
file.close()
print('list has been reversed and stored in the file')

