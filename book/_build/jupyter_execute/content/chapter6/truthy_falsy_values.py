#!/usr/bin/env python
# coding: utf-8

# # Truthy and Falsy Values 
# 
# In previous chapters we have used the boolean values `True` and `False`.
# We already know that expressions with operators can evaluate to True or False.

# In[1]:


10 > 2


# In[2]:


if 10 > 2:
    print('Hello World!')


# We use these expressions a lot in `if` statements, `while` loops and so on. Now consider the following `if` statements where there is no use of an operator such as `>`, `<`, `==` etc.

# In[3]:


x = 10
if x:
    print('Hello World')
else:
    print('Good Bye')


# In[4]:


x = 0
if x:
    print('Hello World')
else:
    print('Good Bye')


# In[5]:


x = [1, 2, 3 ]
if x:
    print('Hello World')
else:
    print('Good Bye')


# In[6]:


x = []
if x:
    print('Hello World')
else:
    print('Good Bye')


# You may be wondering how the above `if` statements are even evaluating to `True` or `False`. There is not a typical expression next to the `if`. Instead, only a variable is next to the `if`. In Python, specific values can evaluate to either `True` or `False` even if they are not part of a larger expression. The basic idea is that values that evaluate to `False` are considered **Falsy** whereas values that evaluate to `True` are considered **Truthy**. There are several rules we need to know to figure out what these values will evaluate to. You can checkout out the official [Python documentation](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) for these rules. We will cover them here mostly.
# 
# By default, the majority of values in Python will be **truthy**. That is they will evaluate to `True`. So you just need to remember what type of values evaluate to `False`. They are:
# 
# - constants defined to be false: `None` and `False`.
# - zero of any numeric type: `0` and `0.0` for example.
# - empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`
# 

# So think of 0 and anything "empty" (having a length of 0) as evaluating to `False`.

# In[7]:


if 0:
    print('I will not print')
elif []:
    print('I will not print')
elif {}:
    print('I will not print')
elif set():
    print('I will not print')
elif ():
    print('I will not print')
elif None:
    print('I will not print')
else:
    print('I will print because every value above evaluates to False.')


# Here are some more examples.

# In[8]:


# once i gets to 0 it will evaluate to False and the loop will break/stop
i = 3
while i:
    print(i)
    i = i - 1


# In[9]:


if 5 and 0:
    print('HEY')


# In[10]:


if 3 and -10:
    print('HEY')


# In[11]:


if 0 or [] or {}:
    print('HEY')


# In[12]:


if 0 or [] or {} or 0.5:
    print('HEY')


# In[13]:


if None:
    print('HEY')


# In[14]:


if not None:
    print('Hey')


# That is it for truthy and falsy values. It's very important to remember these when using control flow. In the next section we will learn more about the `None` value type.
