#!/usr/bin/env python
# coding: utf-8

# # `None` Value
# 
# You may have come across the built in `None` value already when coding in Python.
# For example, `None` is the value a function returns when there is no `return` statement.
# 
# 

# In[1]:


def does_not_return(a,b):
    a + b # no return statment


# In[2]:


x = does_not_return(1,2)


# In[3]:


x # Notice that Jupyter does not display anything unless you print it


# In[4]:


print(x)


# In[5]:


type(x)


# The `None` keyword is used to define a null value, or no value at all.
# `None` is not the same as `0`, `False`, or objects that have no length. `None` is a built in data type (`NoneType`).

# ## Checking for `None`
# When checking if a variable is `None` use `is` and `is not`. Do not use `==` and `!=` to check if something is `None`.

# In[6]:


x = None
y = 6


# In[7]:


if y is None:
    print(f'y is None')
    
if x is None:
    print(f'x is None')


# In the previous section we learned about truthy and falsy values. `None` is falsy and evaluates to `False`.

# In[8]:


result = None
if result:
    print('I got a result!')
else:
    print('I did not get a result.')


# ## Using `None` as default argument
# It is very common to use `None` as a default argument in function definitions.

# In[9]:


def say_hello(name=None):
    if name is not None:
        print(f'Hello there {name}!')
    else:
        print(f'Hello there!')


# In[10]:


say_hello()


# In[11]:


say_hello('Chris')


# It is also common to use `None` as default argument when that argument will represent something that is mutable, such as a list. It's bad practice to use mutable objects as default arguments because weird things can happen. Consider the following function which has a mutable object as a default argument.

# In[12]:


def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list


# In[13]:


append_to_list(3, [1,2])


# In[14]:


append_to_list(7, [5, 6])


# Things seem fine right? But now look at this example where we use the default argument.
# 
# 
# 
# 

# In[15]:


append_to_list(1)


# In[16]:


append_to_list(2)


# In[17]:


append_to_list(3)


# You would expect the `my_list` to be empty at the beginning of the function logic in each of the above three examples. But a new list is created once when the function is defined, and the same list is used in each successive call. This is why you should **never** use a mutable data type as a default argument. Unexpected things can occur. Instead you can use `None` as the default argument.

# In[18]:


def append_to_list_improved(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


# In[19]:


append_to_list_improved(3, [1,2])


# In[20]:


append_to_list_improved(1)


# In[21]:


append_to_list_improved(2)


# In[22]:


append_to_list_improved(3)


# Now you know a little more about the `None` data type. You will see and use it a lot
# as you code in Python more.

# In[ ]:




