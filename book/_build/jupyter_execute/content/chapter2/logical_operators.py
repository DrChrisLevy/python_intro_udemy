#!/usr/bin/env python
# coding: utf-8

# # Logical Operators
# 
# The three logical operators in Python are `and`, `or`, and `not`. They are used to combine
# the `True` or `False` values of variables or expressions into a result that is 
# either `True` or `False`. Let's look at some examples.
# 
# Create a Jupyter Notebook and name it **intro_logical_operators** and follow along.
# 
# (and-operator)=
# ## `and` operator

# In[1]:


x = 5 
print(x > 3 and x < 10) # both are True so result is True


# In[2]:


print(x > 3 and x < 0) # one is True and other is False so result is False


# In[3]:


print(x < 0 and x > 3) # one is False and other is True so result is False


# In[4]:


print(x < 0 and x > 3) # one is False and other is True so result is False


# In[5]:


print(x < 0 and x < 3) # both are False so result is False


# The above examples were with numbers but the logical operators
# can be used with any valid Python expressions that are either
# `True` or `False`. For the `and` operator, the result is 
# only `True` if both things are `True`. If there is at least one
# `False` then the result is `False`. This should be clear from
# the English Language. If someone said you could have a cookie
# if you *cleaned your room* **and** *cleaned the dishes*, then you
# would know you would have to do both things to get the cookie.

# In[6]:


True and True


# In[7]:


True and False


# In[8]:


False and True


# In[9]:


False and False


# You can chain multiple logical operators together.
# And it is often wise to use `()` to keep things clear.
# For example,

# In[10]:


('hello' == 'hello') and (5 != 6) and (5 > -1) and ('A' != 0) # True and True and True and True is True


# In[11]:


('hello' == 'hellooo') and (5 != 6) and (5 > -1) and ('A' != 0) # False and True and True and True is False


# When chaining multiple `and`s together, the result is `True` if all the intermediate results are `True`. If there is at least one `False` then the final result is `False`.

# ## `or` operator
# 
# With the `or` operator, the resulting expression is `True` if there is at least
# one `True`. Otherwise it is `False`.

# In[12]:


True or False


# In[13]:


False or True


# In[14]:


True or True


# In[15]:


False or False


# In[16]:


a = 'cat'
b = 'dog'
c = a


# In[17]:


a == b or c == a # False or True is True


# In[18]:


c == a or a == b # True or False is True


# In[19]:


(5 == 5) or ( 0 > 1) or ( 5 == 4) or (10 > -5) or (10 != 10) # at least one is True so result is True


# ## `not` operator
# 
# The `not` operator takes any expression that is `True` or `False` and
# simply flips it to the opposite.

# In[20]:


not True


# In[21]:


not False


# In[22]:


not (1 == 1)


# In[23]:


not (5 < 4)


# In[24]:


not (-4 < -4)


# In[25]:


not ('hello' == 'hello')


# ## Simple Practice Using Operators
# 
# We will be using these comparison and logical operators a lot. Take some time now to understand 
# what each means and their differences. All of the expressions below will evaluate to either `True` or `False`.
# Try them first before checking in python. Make sure you understand why each one 
# is either `True` or `False`. These are all examples of boolean expressions. Boolean expressions
# are expressions which evaluate to either True or False.
# 
# `5 == 5`
# 
# `5 >= 5`
# 
# `5 <= 5`
# 
# ` 5 < 6`
# 
# `'4' + '3' == 7`
# 
# `str(10) + str(10) == '1010'`
# 
# `'a' + 'b' == 'a b'`
# 
# `5 + int('123') == 5123`
# 
# `str(5) + '5' == '55'`
# 
# `(5 > 3) and (5 > 4)`
# 
# `(5 > 3) and (4 < 5)`
# 
# `(5 > 3) or (5 > 4)`
# 
# `(2 < 1) or (3 < 1)`
# 
# `1 == 1`
# 
# `not (1 == 1)`
# 
# `5 > 3 or 3 < 5`
# 
# `not (5 > 3 or 3 < 5)`
# 
# `(not 3 == 5) and not (4 == 4)`
# 
# `not ( (True or False) and (False and True) )`
# 
# `not (True or False) == (not True) and (not False)`
# 
# `not (True and True) == (not True) or (not True)`
