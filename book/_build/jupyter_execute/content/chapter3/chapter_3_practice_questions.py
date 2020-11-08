#!/usr/bin/env python
# coding: utf-8

# # Practice Questions

# ## 1.
# Write a Python function that finds the minimum of three numbers.
# It should take three numbers as input and then return the smallest.

# ## 2.
# In mathematics the factorial of a number is denoted by 
# 
# $$n! = n\cdot(n-1)\cdot(n-2)\cdot(n-3)\cdot\cdot\cdot\cdot3\cdot2\cdot1$$
# 
# For example, 
# 
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 
# 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 1 = 3628800
# 
# Both 1! and 0! are defined to be 1 so those are special cases you can handle.
# Write a function that takes any integer greater than or equal to 0 as input 
# and then returns the factorial. That is, it multiplies the number by all the numbers
# before it like the examples above.
# 
# ## HINT
# 
# Try the question first before revealing the hint.

# In[1]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    result = 1
    
    # Then use a loop and range that does:
    # result = 2 * result
    # result = 3 * result
    # result = 4 * result
    # and so on.
 
    return result
        


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
# You should use of the [enumerate](enumerate) function.
# 
# ## HINT
# 
# Try the question first before revealing the hint.
# 
# 
# 
# 

# In[2]:


def find_twos(numbers):
    result = []
    
    if 2 not in numbers:
        return result
    else:
        # use for loop and enumerate to loop over numbers
        # and check if the number is 2.
        # If it is, append the position to result.
        pass
    
    return result
        


# ## 4.
# Define a function, `sum_and_round`, which takes a list of floats as input and adds all the numbers together and returns the result rounded with 2 decimal places.
# Use the built in functions `sum` and `round`. For example:
# 
# `sum_and_round([1.2353, 7.532, 7.532, 8.9, 9.654])` should return 34.85
# 
# 

# ## 5.
# Consider the function
# 

# In[3]:


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

# ## 6.
# Consider the following code.

# In[4]:


x = 5
def my_func(a=1):
    x = 19
    return a + x


# If you were to run the above code and then use `print(x)` what would be the value printed?

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
# 
# 
# 

# In[ ]:




