# -*- coding: utf-8 -*-
"""20L-2074_Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10kUiCP7zKG2hEMqtgUslVpzwI2h5jl0H
"""

def checkpalindrome(array):

  l1=[]
  flag = True
  k=0
  for i in array:
    if i.isalpha() or i.isdigit():
      l1.append(array[k])
    k+=1
  print(l1)
  l2=l1
  print(l2)


  size=len(l1)
  start=0
  end=size-1
  while start<end :
    if l1[start]!=l1[end]:
      print("Not Palindrome!")
      flag=False
      break
    else:
      start+=1
      end-=1
  if flag==True:
   print("String Is Palindrome!")
 

arr="A man, a plan, a canal: Panama"
arr2=arr.lower()
checkpalindrome(arr2)