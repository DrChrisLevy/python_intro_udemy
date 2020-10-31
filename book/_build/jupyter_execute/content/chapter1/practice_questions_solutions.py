#!/usr/bin/env python
# coding: utf-8

# # Practice Questions (Solutions)
# 
# **1.** 
# 
# Create a new Jupyter Notebook called **practice_questions** or something similar.
# Use this notebook to practice Python by going through the rest of these questions.
# Remember to save your Jupyter Notebook through out. You can use markdown
# cells to give answers to questions where coding is not required.
# You can use markdown cells in general to take additional notes and so on.

# **2.** 
# 
# In your head, or on a piece of paper, workout the following math question. 
# 
# $$5 × 4 + 10 - \frac{20 + 40}{2}$$
# 
# Then use Python to get the same answer.

# In[1]:


5 * 4 + 10 - (20 + 40) / 2


# **3.** 
# 
# Print the string **She sells seashells by the seashore**. For some extra
# fun, try saying this out loud over and over again very quickly!
# 

# In[2]:


print('She sells seashells by the seashore')


# **4.**
# 
# Print a multiline string. It can be any string at all with multiple lines.

# In[3]:


print("""
HI

BYE
""")


# **5.**  
# 
# Why does this code raise an error: `'100' + 100`

# Because it is attempting to add a string and an integer which you can not do!

# **6.** 
# 
# Suppose you had these two variables defined:

# In[4]:


day_one = 'Monday'
day_two = 'Tuesday'


# Use the variables `day_one` and `day_two`, along with **string concatenation** to print the string:
# **The Day after Monday is Tuesday**. Do not use *f-strings* but use string concatenation.

# In[5]:


"The Day after " + day_one + " is " + day_two


# **7.**  
# 
# Repeat question 6 but using *f-strings* instead of string concatenation.

# In[6]:


print(f'The Day after {day_one} is {day_two}')


# **8.** 
# 
# If this code was executed, what would be the *value* and the *type* of 
# the variable `x`? What would be the *value* and the *type* of 
# the variable `y`? Do this question without writing any code first.
# Then type it out and execute it in Python to check your answer.

# In[7]:


y = 10
x = (y / y) - y
y = x + (2 * x)


# In[8]:


print(x)
print(type(x))
print(y)
print(type(y))


# **9.**  
# 
# Write code that takes a number as input from a user and then adds 5 to it. Print the final result.

# In[9]:


# just uncomment this code to see how it works.
# the reason it is commented out is because
# the input() will not work in this book
# builder.

# number = input('Please enter a number ')
# print(int(number) + 5)


# **10.**
# 
# Write code that takes three separate inputs from a user: 
#     - favorite food
#     - favorite color
#     - favorite movie
#     
# Then get the code to print a string such as:
# **Your favorite food, color, and movie are ____, ____, and ____!**. 
# Fill in the blanks
# with the users input that they entered.

# In[10]:


# just uncomment this code to see how it works.
# the reason it is commented out is because
# the input() will not work in this book
# builder.

# food = input('What is your favorite food? ')
# color = input('What is your favorite color? ')
# movie = input('What is your favorite movie? ')
# print(f'Your favorite food, color, and movie are {food}, {color}, and {movie}!')


# **11.** 

# In[11]:


sentance = 'The sky is blue and the grass is green.'


# *a)* Use string slicing to extract the string from `sentance`, `'the grass is green'`
# 
# *b)* Use string slicing to extract the string from `sentance`, `'The sky is blue'`
# 
# *c)* Without coding, what is the type and value of `sentance[0]`?
# 
# *d)* Without coding, what is the type and value of `sentance[-1]`?
# 
# *e)* Without coding, what string does this work out to be: `sentance[-6:-2]`
# 
# *f)* Without coding, what string does this work out to be: `sentance[-6:]`
# 
# *g)* Without coding, what string does this work out to be: `sentance[4:15]`
# 
# *h)* Without coding, what string does this work out to be: `sentance[4:15:2]`
# 
# *i)* Use code and string slicing to reverse the string defined by `sentance`.

# In[12]:


print(sentance)
# a)
print(sentance[20:38])

# b)
print(sentance[0:15])
# or you could do
print(sentance[:15])

# c)
print(sentance[0])
print(type(sentance[0]))

# d)
print(sentance[-1])
print(type(sentance[-1]))

# e) 
print(sentance[-6:-2])

# f) 
print(sentance[-6:])

# g)
print(sentance[4:15])

# h)
print(sentance[4:15:2])

# i)
print(sentance[::-1])


# **12.** 

# In[13]:


a = 1
b = -10
c = -10 / 2
d = 2.5 * 2


# Suppose the above code was executed.
# What would the *value* and *type* of `a`, `b`, `c`, and `d` be?
# Now check your answer by executing it in Python.
# 
# Next, write code that would convert (but only if the conversion is needed)
# `a` to a string, `b` to a float, `c` to an `int`, and `d` to a float.
# If the conversion is not needed than simply say so.

# In[14]:


print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))

#a to a string
print(str(a))
#b to a float
print(float(b))
#c to an int
print(int(c))
#d to a float. Not needed because already a float.


# **13.** 
# 
# Write code that gets three numbers from a user input and 
#     stores the values in variables named `a`, `b`, and `c`.
#     Then print a string that displays the sum of $a + b + c$ as a floating point number.
#     For example, if they entered $a=1, b=2, c=3$ then the code will print $6.0$.

# In[15]:


# just uncomment this code to see how it works.
# the reason it is commented out is because
# the input() will not work in this book
# builder.

# a = int(input())
# b = int(input())
# c = int(input())
# print(float(a + b + c))


# **14.**
# 
# Answer these questions without coding anything. These questions are supposed
# to test your understanding of integer, float, and string conversion
# as well as variable assignment. You can always check your answer after
# in the Jupyter Notebook.
# 
# *a)*
# 
# What is the *type* and *value* for both `a` and `b`?
# 
# ```
# a = 4.5
# b = int(a)
# ```
# 
# *b)*
# 
# What is the *type* and *value* for `a`?
# ```
# a = 5.43
# print(float(a))
# ```
# 
# *c)*
# 
# What is the *type* and *value* for `b`?
# ```
# a = '5.43'
# b = float(a)
# ```
# 
# *d)*
# 
# What is the *type* and *value* of `a`?
# 
# ```
# a = str(float(int(-4.99)))
# ```
# 
# *e*)
# 
# What is the *type* and *value* of `c`?
# ```
# a = 12
# b = 0
# c = str(a) + str(b)
# ```
# 
# *f*)
# 
# What is the *type* and *value* of `c`?
# 
# ```
# a = '12'
# b = '0'
# c = f'{int(a) + int(b)}'
# ```

# In[16]:


# answer to a)
a = 4.5
b = int(a)
# a is float 4.5 and b is integer 4
print(a)
print(type(a))
print(b)
print(type(b))


# In[17]:


# answer to b)
a = 5.43
print(float(a))
# a will be float 5.43
print(a)
print(type(a))


# In[18]:


# answer to c)
a = '5.43'
b = float(a)
# a is a string '5.43' and b is float 5.43
print(a)
print(type(a))
print(b)
print(type(b))


# In[19]:


# answer to d)
a = str(float(int(-4.99)))
# a is str '-4.0'
print(a)
print(type(a))


# In[20]:


# answer to e)
a = 12
b = 0
c = str(a) + str(b)
# c is str '120'
print(c)
print(type(c))


# In[21]:


# answer to f)
a = '12'
b = '0'
c = f'{int(a) + int(b)}'
# c is str '12'
print(c)
print(type(c))

