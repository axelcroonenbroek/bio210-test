#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x_0 = 0
x_1 = 1

fibo_list = [x_0, x_1]

for a in range (48) :
    fibo_list.append(fibo_list[a] + fibo_list[a+1])

