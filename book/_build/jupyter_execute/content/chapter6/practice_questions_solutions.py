#!/usr/bin/env python
# coding: utf-8

# # Practice Questions (Solutions)

# ## 1.
# For each of the following `if` statements, determine what will be printed.

# In[1]:


x = 0
if x:
    print(1)
else:
    print(2)


# In[2]:


y = [0]
if y:
    print(1)
else:
    print(2)


# In[3]:


if 1 and 0:
    print(1)
else:
    print(2)


# In[4]:


if [] and {1:4}:
    print(1)
else:
    print(2)


# In[5]:


if set() or (1,):
    print(1)
else:
    print(2)


# In[6]:


if [] or () or {}:
    print(1)
else:
    print(2)


# In[7]:


x = None
if x:
    print(1)
else:
    print(2)


# ## 2.
# 
# Write a function that checks if something is an empty list, or an empty dict, or an empty set,
# or an empty tuple, or is `None`. If so, the function should return `True`. Otherwise return `False`.

# In[8]:


def is_empty(x):
    if x == [] or x == {} or x == set() or x == () or x is None:
        return True
    else:
        return False


# ## 3. 
# 
# Write a function `add_to_dict(key_list, value_list, my_dict)` which adds the key value pairs `k:v` to the dictionary `my_dict` for each key and value in `key_list` and `value_list`. If one of the keys in `key_list` is already present in `my_dict` it should overwrite it in `my_dict`. If `my_dict` is not provided, the function should create an empty dictionary and then add the key value pairs.
# If the dictionary `my_dict` is provided as an argument, then the key value pairs will simply be added to it. Remember
# that dictionaries are mutable and you should not provide mutable objects as default arguments. The final dictionary should be returned after the items are added to it. Here are some examples of how the function should work.
# 
# `add_to_dict([1],[2])` should return the dictionary `{1: 2}`
# 
# `add_to_dict([1,2,3],[4,5,6])` should return the dictionary `{1: 4, 2: 5, 3: 6}`
# 
# `add_to_dict([1,2,3],[4,5,6],my_dict={'hello': 'world'})` should return the dictionary`{'hello': 'world', 1: 4, 2: 5, 3: 6}`
# 
# `add_to_dict([1] ,['new'],my_dict={1: 1, 3:5})` should return the dictionary `{1: 'new', 3: 5}`

# In[9]:


def add_to_dict(key_list, value_list, my_dict=None):
    if my_dict is None:
        my_dict = {}
    for k,v in zip(key_list, value_list):
        my_dict[k] = v
    return my_dict


# In[10]:


add_to_dict([1],[2])


# In[11]:


add_to_dict([1,2,3],[4,5,6])


# In[12]:


add_to_dict([1,2,3],[4,5,6],my_dict={'hello': 'world'})


# In[13]:


add_to_dict([1] ,['new'],my_dict={1: 1, 3:5})


# ## 4.
# 
# Write a function `read_file(file_name)` which reads the contents of a local file line by line and returns
# a list with each element of the list being a line of the file. You can assume the local file exists. Also, remove the new line characters.
# 
# For example: 
# 
# If the local file was `'my_file.txt'` and contained the contents
# 
# ```
# Hello World!
# 1 2 3 4 5
# a
# b
# c
# Good Bye!
# ```
# 
# then `read_file('my_file.txt')` would behave like this:

# In[14]:


def read_file(file_name):
    with open(file_name, 'r') as f:
        return [l.rstrip() for l in f]


# In[15]:


read_file('my_file.txt')


# ## 5.
# 
# For the function `read_file` from above, run it for a file that does not exist.

# In[16]:


read_file('some_file.txt')


# The code will raise an error. In particular, a `FileNotFoundError` error.
# Adjust the function logic for `read_file` so that it handles this error. That is, if you pass
# an argument for a file that does not exist, instead of raising the error, the code should instead
# print a simple message such as `'The file, some_file.txt does not exist! Exiting and returning None.
# '` and should return `None`. Do this with a `try` and `except` block where you specifically handle
# the `FileNotFoundError` error.

# In[61]:


def read_file_improved(file_name):
    try:
        with open(file_name, 'r') as f:
            return [l.rstrip() for l in f]
    except FileNotFoundError:
        print(f'The file, {file_name} does not exist! Exiting and returning None.')
        return None


# In[62]:


read_file_improved('some_file.txt')


# If the file does exist, then the function should have the same behavior as before.

# In[63]:


read_file_improved('my_file.txt')


# ## 6.
# Write code that writes some data to a file. 

# In[64]:


with open('dots_file.txt', 'w') as f:
    for i in range(1, 101):
        f.write('.' * i )
        f.write('\n')

