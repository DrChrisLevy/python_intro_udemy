#!/usr/bin/env python
# coding: utf-8

# # More Basic Python Operators
# We have already learned multiple Python operators such as
# `+,=,-,*,/,>,<,>=,<=,and,or,not,in,not in` and so on.
# In this section we will learn some more. Create a new Jupyter Notebook
# and name it **more_basic_operators** to follow along.
# 
# (mod-operator)=
# ## Modulus Operator `%` 
# The operator `%` is called the modulo operator.
# It gives the remainder when performing division between two
# numbers. For example, if you divide 4 by 2 the remainder is 0.
# Therefore, `4 % 2` would return `0`. Another example is when
# you do 9 divided by 4. The remainder is 1 so `9 % 4` would
# return `1`.

# In[1]:


4 % 2


# In[2]:


print(9 % 4)


# We can use the `%` operator to check if a number is even.
# For example, the number `n` is even if `n % 2` returns `0`
# because the number 2 would divide evenly into `n`.

# In[3]:


6 % 2 # 6 is even because remainder is 0


# In[4]:


10 % 2 # 10 is even because remainder is 0


# In[5]:


13 % 2 # 13 is odd because remainder is not 0.


# You can also use `%` to check if a number is a multiple of any given number. If you do `a % b` and get a remainder of 0, then it means that `a` is a multiple of `b`. This just means that `b` divides into `a` evenly with a remainder of 0.

# In[6]:


123 % 3 # returns 0 so 123 is a multiple of 3


# In[7]:


256 % 32 # returns 0 so 256 is multiple of 32


# In[8]:


99 % 45 # does not return 0 so 99 is not a multiple of 45


# ## Assignment Operators
# We have already learned about the `=` operator.

# In[9]:


a = 1


# In[10]:


print(a)


# But there are some other operators which you will
# often see coders use. For example, you will often see the pattern:

# In[11]:


i = 0
for x in range(4):
    print(i)
    i = i + 1


# Another way of writing `i = i + 1` is `i += 1`

# In[12]:


i = 0
for x in range(4):
    print(i)
    i += 1 # is the same as i = i + 1


# In general, `a += b` is the same as `a = a + b`. It is good to know about
# this because many Python coders will use these little shortcuts operators.
# Here are some others ones:
# 
# - `a += b` is the same as `a = a + b`
# - `a -= b` is the same as `a = a - b`
# - `a *= b` is the same as `a = a * b`
# - `a /= b` is the same as `a = a / b`
# 
# Feel free to use these when you want.

# In[ ]:




