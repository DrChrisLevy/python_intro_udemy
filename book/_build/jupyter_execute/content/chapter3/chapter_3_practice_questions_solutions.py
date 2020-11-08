#!/usr/bin/env python
# coding: utf-8

# # Practice Questions (Solutions)

# ## 1.
# Write a Python function that finds the minimum of three numbers.
# It should take three numbers as input and then return the smallest.
# 
# ### Solution

# In[1]:


def find_min(a, b, c):
    return min(a, b, c)
    


# In[2]:


find_min(10, 67.8, 100)


# ## 2.
# In mathematics the factorial of a number is denoted by 
# 
# $$n! = n\cdot(n-1)\cdot(n-2)\cdot(n-3)\cdot\cdot\cdot\cdot3\cdot2\cdot1$$
# 
# For example, 
# 
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 
# 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800
# 
# Both 1! and 0! are defined to be 1 so those are special cases you can handle.
# Write a function that takes any integer greater than or equal to 0 as input 
# and then returns the factorial. That is, it multiplies the number by all the numbers
# before it like the examples above.
# 
# ### SOLUTION
# 

# In[3]:


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result = result * i
    return result


# In[4]:


factorial(0)


# In[5]:


factorial(1)


# In[6]:


factorial(2)


# In[7]:


factorial(3)


# In[8]:


factorial(4)


# In[9]:


factorial(5)


# In[10]:


factorial(6)


# In[11]:


factorial(10)


# ## 3. 
# 
# Create a function called `find_twos` which takes a list of numbers as input.
# The function should return another list of all the indexes/positions
# where the number 2 is in the input list. If the number 2 is not
# in the input list then the function should return an empty list.
# 
# For example:
# 
# `find_twos([1,3,-19])` should return `[]`.
# 
# `find_twos([1,2,4])` should return `[1]`.
# 
# `find_twos([2,2,2])` should return `[0,1,2]`.
# 
# `find_twos([1,6,8,2,9,0,5,2])` should return `[3,7]`.
# 
# You should use the [enumerate](enumerate) function.
# 
# 
# 
# ### SOLUTION
# 

# In[12]:


def find_two(numbers):
    result = []
    if 2 not in numbers:
        return result
    else:
        for i, num in enumerate(numbers):
            if num == 2:
                result.append(i)
    return result


# In[13]:


find_two([])


# In[14]:


find_two([1,3,5,20])


# In[15]:


find_two([2])


# In[16]:


find_two([2,2,2,2])


# In[17]:


find_two([1,6,8,2,9,0,5,2])


# ## 4.
# Define a function, `sum_and_round`, which takes a list of floats as input and adds all the numbers together and returns the result rounded with 2 decimal places.
# Use the built in functions `sum` and `round`. For example:
# 
# `sum_and_round([1.2353, 7.532, 7.532, 8.9, 9.654])` should return 34.85
# 
# ### SOLUTION

# In[18]:


def sum_and_round(numbers):
    result = sum(numbers)
    result_rounded = round(result, 2)
    return result_rounded


# In[19]:


sum_and_round([1.2353, 7.532, 7.532, 8.9, 9.654])


# Or you could do it in one line:
# 

# In[20]:


def sum_and_round(numbers):
    return round(sum(numbers), 2)


# In[21]:


sum_and_round([1.2353, 7.532, 7.532, 8.9, 9.654])


# In[ ]:





# ## 5.
# Consider the function
# 

# In[22]:


def do_stuff(a, b, c):
    return a * b * c - a - c + b


# a) Call the function using only positional arguments.
# 
# b) Call the function using only keyword arguments.
# 
# c) Call the function using a mix of positional and keyword arguments.
# 
# d) Redefine the function and give default argument for `a,b,c`. Then call the function
# without providing any arguments so that the default arguments are used.
# 
# ### SOLUTION

# In[23]:


# a)
do_stuff(1, 2, 3)


# In[24]:


# b)
print(do_stuff(a=1, b=2, c=3))
print(do_stuff(c=3, a=1, b=2))


# In[25]:


# c)
print(do_stuff(1, 2, c=3))
print(do_stuff(1, b=2, c=3))


# In[26]:


# d)
def do_stuff(a=1, b=2, c=3):
    return a * b * c - a - c + b

do_stuff()


# ## 6.
# Consider the following code.

# In[27]:


x = 5
def my_func(a=1):
    x = 19
    return a + x


# If you were to run the above code and then use `print(x)` what would be the value printed?
# 
# ### SOLUTION
# 
# The value of `x` would still be 5 outside the function. For example
# we can run the code and check:

# In[28]:


x = 5
def my_func(a=1):
    x = 19
    return a + x
my_func(a=20)
print(x)


# ## 7.
# Write a function `get_seconds` that takes two arguments `hours` and `minutes` and converts
# them both to seconds and adds the result and returns it. For example,
# 
# `get_seconds(hours=1,minutes=0)` should return `3600`
# 
# `get_seconds(hours=0,minutes=1)` should return `60`
# 
# `get_seconds(hours=0,minutes=0)` should return `0`
# 
# `get_seconds(hours=10,minutes=48)` should return `38880`
# 
# 
# `get_seconds()` should return `0` so be sure to use default arguments to achieve this.
# 
# ### SOLUTION

# In[29]:


def get_seconds(hours=0, minutes=0):
    return hours * 60 * 60 + minutes * 60


# In[30]:


get_seconds(hours=1,minutes=0)


# In[31]:


get_seconds(hours=0,minutes=1)


# In[32]:


get_seconds(hours=10,minutes=48)


# In[33]:


get_seconds()

