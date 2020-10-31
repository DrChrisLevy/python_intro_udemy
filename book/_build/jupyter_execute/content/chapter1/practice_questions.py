#!/usr/bin/env python
# coding: utf-8

# # Practice Questions
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

# **3.** 
# 
# Print the string **She sells seashells by the seashore**.

# **4.**
# 
# Print a multiline string. It can be any string at all with multiple lines.

# **5.**  
# 
# Why does this code raise an error: `'100' + 100`

# **6.** 
# 
# Suppose you had these two variables defined:

# In[1]:


day_one = 'Monday'
day_two = 'Tuesday'


# Use the variables `day_one` and `day_two`, along with **string concatenation** to print the string:
# **The Day after Monday is Tuesday**. Do not use *f-strings* but use string concatenation.

# **7.**  
# 
# Repeat question 6 but using *f-strings* instead of string concatenation.

# **8.** 
# 
# If this code was executed, what would be the *value* and the *type* of 
# the variable `x`? What would be the *value* and the *type* of 
# the variable `y`? Do this question without writing any code first.
# Then type it out and execute it in Python to check your answer.

# In[2]:


y = 10
x = (y / y) - y
y = x + (2 * x)


# **9.**  
# 
# Write code that takes a number as input from a user and then adds 5 to it. Print the final result.

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

# **11.** 

# In[3]:


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

# **12.** 

# In[4]:


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

# **13.** 
# 
# Write code that gets three numbers from a user input and 
#     stores the values in variables named `a`, `b`, and `c`.
#     Then print a string that displays the sum of $a + b + c$ as a floating point number.
#     For example, if they entered $a=1, b=2, c=3$ then the code will print $6.0$.

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
