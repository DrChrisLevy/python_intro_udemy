#!/usr/bin/env python
# coding: utf-8

# # Variables and Types
# 
# Python variables make it possible to keep track of objects that are stored in memory
# throughout your Python program. 
# You may be wondering what an "object" is. It turns out you have
# worked with **objects** already in this book and in your Jupyter Notebooks.
# Essentially, everything in Python is an object.
# 
# Here is a string with my name and a number with my age.
# The string `'Chris'` and the number `35` are examples of
# objects in Python. 
# 
# Be sure to create a new Jupyter Notebook and call it **intro_to_variables**.
# You can follow along by typing these examples out in your own
# Jupyter Notebook and executing the code.

# In[1]:


print('Chris')
print(35)


# So what is actually happening behind the scenes in Python when those lines of code are executed?
# 
# - For the line `print('Chris')`, Python will
#     - create a *string* object
#     - give it the value `'Chris'`
#     - print it to the screen
# 
# - For the line `print(35)`, Python will
#     - create an *integer* object
#     - give it the value `35`
#     - print it to the screen
# 
# But what if we want to use these objects again later in our program?
# At the moment we can not. These objects were created in the
# computers memory but they will just remain there forgotten.
# There is no way to retrieve them or get them back.
# 
# This is where **variables** come in to play in programming.
# In Python you can create a variable using the equal sign `=`.
# Variables have **names** and are assigned to an object that is
# in memory. The Variable holds the value of a specific object in memory
# so we can keep track of the object and use it for other purposes.
# 
# For example, here I create two variables named `my_name` and `my_age`.

# In[2]:


my_name = 'Chris'
my_age = 35


# In[3]:


my_name


# In[4]:


my_age


# In[5]:


print(my_name)
print(my_age)


# When the line `my_name = 'Chris'` is executed, Python will 
# - create a *string* object
# - give it the value `'Chris'`
# - the variable `my_name` is bound to that object. Programmers will refer to this 
#   as "The value of `my_name` is assigned `'Chris'`.
#   
# When the line `my_age = 35` is executed, Python will 
# - create an *integer* object
# - give it the value `35`
# - the variable `my_age` is bound to that object. Programmers will refer to this 
#   as "The value of `my_age` is assigned `35`.
# 
# ![variable_pointers_in_memory_1](variable_pointers_in_memory_1.png)

# Variables have a *name*, a *type*, and a *value*. The value is the object in memory
# which the variable is bound to. The variable `my_name` has the name "*my_name*" and is of
# type *string*. It's value is `Chris`. You can always get the type of an object
# by using the `type()` function. Here `str` stands for type string and `int` stands
# for type `integer`.

# In[6]:


type(my_name)


# In[7]:


print(type(my_name))
print(type(my_age))


# Let's create a new variable `x` and set it to the value of `my_age`.

# In[8]:


x = my_age
print(x)


# When we created the variable `x` above, Python does not create a new integer object with the value `35` in memory.
# Instead, `x` is just another reference to the existing `35` that is already in memory.
# 
# ![variable_pointers_in_memory_2](variable_pointers_in_memory_2.png)
# 
# In Python you can change the type and value of an existing variable.
# For example we can change `my_age` to a string.

# In[9]:


my_age = '35 years'


# ![variable_pointers_in_memory_3](variable_pointers_in_memory_3.png)

# In[10]:


print(my_name)
print(my_age)
print(x)


# In[11]:


print(type(my_name))
print(type(my_age))
print(type(x))


# Let's make one more final change and change the value of `x`. 
# Now the object that has the value of `35` is not assigned to
# any variable. It is in memory but will be garbage collected
# because nothing is referencing it in the code.

# In[12]:


x = 36
print(my_name)
print(my_age)
print(x)


# ![variable_pointers_in_memory_4](variable_pointers_in_memory_4.png)

# Let's use variables now in some more examples. 

# In[13]:


a = 5
b = 10
c = a + b
print(a)
print(b)
print(c)


# In[14]:


a = 'hello'
b = 'world'
c = a + b
print(a)
print(b)
print(c)


# In[15]:


x = 2
y = 3
z = x * x + y * y
print(z)


# In[16]:


intro = "Hello! My name is "
name = "Chris "
ending = "and I am "
age = "35 years old."

print(intro + name + ending + age)


# Remember, you can not add two objects together that are different types.
# Here we are concatenating strings which is okay but then we try to add
# the integer `35` to the string.

# In[17]:


name = 'Chris'
print(type(name))
age = 35
print(type(age))
print('My name is ' + name + ' and I am ' + age + 'years old.')


# Take some time on your own to play around with variables
# and see what you can create. Even if it's simple that is okay.
# The best way to learn is by doing!
