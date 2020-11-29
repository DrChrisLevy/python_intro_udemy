#!/usr/bin/env python
# coding: utf-8

# # The `import` Statement
# 
# [The Python Standard Library](https://docs.python.org/3/library/index.html) has a bunch of modules we can import and use in our Python code. These come built into Python. You can think of a *module* as a code library which contains all sort of functions and tools to use in your application code. Another thing that makes Python so amazing is all the external libraries you can install and import into your code from [The Python Package Index (PyPI)](https://pypi.org/).
# 
# First we need to learn to import modules and libraries into our code. We will begin with examples of modules that are built into the [The Python Standard Library](https://docs.python.org/3/library/index.html). That is, we do not have to install any external packages. They simply come along with your installation of Python.
# 
# Let's start with a simple example. Suppose we want to take the square root of a number. The square root of a number $x$ is a number $y$ such that $y \cdot y = x$. For example, the square root of 9 is 3 because 3 multiplied by 3 is 9. The square root of 16 is 4 because 4 multiplied by 4 is 16.
# 
# Python has a built-in module that you can use for mathematical tasks and is called the `math` module. We can use it to perform many mathematical operations and here we will first use
# it to compute the square root. We begin by **importing** the `math` module by using the `import` statement.
# 

# In[1]:


import math


# In[2]:


math.sqrt(16)


# In[3]:


math.sqrt(4)


# In[4]:


math.sqrt(49)


# In[5]:


math.sqrt(50)


# There are all sorts of cool functions and constants we can use from the [math module](https://docs.python.org/3/library/math.html)
# 
# Here is the famous mathematical constant [Pi](https://en.wikipedia.org/wiki/Pi).

# In[6]:


math.pi


# Here is the [factorial function](https://en.wikipedia.org/wiki/Factorial)

# In[7]:


math.factorial(5)


# When we use `import math` we have access to all the "stuff" (functions, constants, etc) from the `math` module. We simply just have to use `math.<name_of_tool>`. If you want to import
# only one function or object you can do it like this.

# In[8]:


from math import pi


# In[9]:


pi


# In[10]:


from math import pi, sqrt, factorial


# In[11]:


pi


# In[12]:


sqrt(49)


# In[13]:


factorial(6)


# But in this case, it's more readable to just `import math` and then use the dot notation
# `math.` to access whatever tool you require.
# 
# Lets import some other modules that comes built into the Python standard library.

# In[14]:


import time


# In[15]:


time.sleep(2) # waits for 2 seconds


# In[16]:


from datetime import date


# In[17]:


date.today() # will return the date that this code is executed on


# Earlier in the course we used the `random` module. It has all 
# sorts of [cool stuff](https://docs.python.org/3/library/random.html)

# In[18]:


import random
numbers = [i for i in range(10)]
x = random.choice(numbers)
x


# In[19]:


x = random.choice(numbers)
x


# In[20]:


x = random.choice(numbers)
x


# In[21]:


x = random.choice(numbers)
x


# In[22]:


random.shuffle(numbers)


# In[23]:


numbers


# In[24]:


random.shuffle(numbers)


# In[25]:


numbers


# In[26]:


sample_one = random.sample(numbers, 5)
sample_one


# In[27]:


sample_two = random.sample(numbers, 5)
sample_two


# There is lot more that could be said about the `import` statement but for now
# I just want you to know how to import a module and how to import a particular function or
# object from a module.
