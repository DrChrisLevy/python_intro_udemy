#!/usr/bin/env python
# coding: utf-8

# # Data Structures
# 
# There are many types of data structures in Python.
# Data structures are used for storing and organizing data.
# In this chapter we will learn about some of the most common
# data structures in Python such as list, tuple, dictionary, and set.
# 
# # List
# You have already learned about lists and
# have used them a lot. Here we will learn
# some more things about lists. It's important
# to remember that lists are **mutable** which
# means you can edit and them and change them after 
# they are created.
# 
# Here we will learn about some more common
# list methods. We have already learned some list
# methods such as `extend` and `append`. Methods
# are a little different then functions and we will
# learn more about methods when we learn about
# object oriented programming. For now, you can sort
# of think as a method as similar to a function. 
# We will not cover all the list methods but you can
# check the official documentation for more [details](https://docs.python.org/3.9/tutorial/datastructures.html)
# 
# ## `sort`
# We can use the `sort` method to sort a list.
# The `sort` method does not return any value
# and sorts the list in place.

# In[1]:


x = [10,60,90,100,-5]
print(x)


# In[2]:


x.sort()


# In[3]:


print(x)


# To sort it in reverse you can use the `reverse` argument.

# In[4]:


y = [0,1,2,3,4]


# In[5]:


y.sort(reverse=True)


# In[6]:


print(y)


# In[7]:


things = ['apple', 'ape', 'cat', 'dog']
things.sort()
print(things)


# ## `count`
# The `count` method can count
# the number of times an item is in a list.

# In[8]:


x = [1,2,2,2,3,5]


# In[9]:


x.count(-1)


# In[10]:


x.count(1)


# In[11]:


x.count(3)


# In[12]:


x.count(2)


# ## `pop`
# The `pop` method is used to remove an item
# at a specific index. It removes the item from the
# list and returns the value of the item that was removed.
# If you do not specify the position of the item to remove,
# it will automatically remove the last item in the list.

# In[13]:


y = [10, 20, 30, 40, 50]


# In[14]:


y.pop(2)


# In[15]:


print(y)


# In[16]:


y.pop(1)


# In[17]:


print(y)


# In[18]:


y.pop()


# In[19]:


print(y)


# ## `remove`
# The `remove` method is used to remove the
# first item in a list that is equal to some 
# value (provided as an argument). If there is no
# such value, a `ValueError` is raised.

# In[20]:


some_stuff = ['hello', 'bye', 1, 2, -10, 'good', 'bad', 3.14, 'hello']


# In[21]:


some_stuff.remove('hello')
print(some_stuff)


# In[22]:


some_stuff.remove(3.14)


# In[23]:


some_stuff


# ## List Comprehension
# 
# List comprehensions give you a very convenient way to define lists quickly.
# In this sections I will show you several types of examples and you can always
# Google more examples too. As you read and write Python code, you will find your self
# using list comprehensions all the time.
# 
# Suppose you wanted to create a list with the integers between 0 and 10.
# One approach would be this:

# In[24]:


numbers = []
for i in range(11):
    numbers.append(i)
print(numbers)


# We can accomplish the same thing in one line using list comprehensions.

# In[25]:


numbers = [i for i in range(11)]
print(numbers)


# In[ ]:




