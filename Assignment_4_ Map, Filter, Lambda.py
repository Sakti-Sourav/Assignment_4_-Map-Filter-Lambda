#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

n = int(input('Input = '))
x = lambda n:n+25
print('Output =' ,x(n))


# In[11]:


# Write a Python program to triple all numbers of a given list of integers. Use Python map

nums = [1, 2, 3, 4, 5, 6, 7]
print("Sample list = ", nums)
result = map(lambda x: x + x + x, nums) 
print("Triple of list numbers =", list(result))


# In[10]:


# Write a Python program to square the elements of a list using map() function

def square_num(n):
  return n * n
nums = [4, 5, 2, 9]
print("Original List = ",nums)
result = map(square_num, nums)
print("Square the elements of the list =", list(result))


# In[ ]:




