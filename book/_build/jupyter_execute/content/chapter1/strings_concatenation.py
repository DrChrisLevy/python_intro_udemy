#!/usr/bin/env python
# coding: utf-8

# # Strings
# 
# In the last section we learned how to do some simple math with numbers
# and print the results with the `print()` function. For example,

# In[1]:


print(9 * 4 + 100/25)


# Now we are going to learn about strings. In programming
# a string is a sequence of characters. 
# Strings in Python are surrounded by either single quotation marks or double quotation marks.
# Create a new Jupyter Notebook and name it **intro_to_strings**. Use
# it to type out the examples which follow. 
# Take the time to play around and create strings different than these as well.

# In[2]:


print('Hello World!')
print("Hello World!")
print('How are you doing today?')
print("abcedfg")
print("1")
print('')
print('123456789')
print('123asd')
print("'")
print('"')
print("Python    is      so               cool    ! ! ! !")


# All the strings were single line strings in that they print over a single line.
# You can make multiline string in python by using triple quotes like this.

# In[3]:


print("""I am a multiline string.



I can be written over multiple lines.
""")


# ## String Concatenation
# 
# You can concatenate strings which means to simply add strings together.
# We already know how to add numbers together like this:

# In[4]:


5 + 5


# You can use the `+` symbol to also add/concatenate strings.
# It simply pastes the strings together into one string.

# In[5]:


print('My name is ' + 'Chris')
print('c' + 'a' + 't')
print('1' + '2')


# Note the difference for example between `5 + 9` and `'5' + '9'`.

# In[6]:


print(5 + 9)
print('5' + '9')


# You can not add a number with a string.
# For example you can not do `5 + '5'`.
# This is because `5` is an integer type and `'5'` is a string type.
# We will learn more about data types later.
# For now though, know that Python will raise
# errors if you try and *add* two objects
# where one is a number and the other is a string.

# In[7]:


5 + '5'

