#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This cell is just to get the image module from our notebooks section to work.
import sys
sys.path.append('../../../notebooks/')


# # Errors and Exceptions
# 
# In this section we are going to look at common errors in Python, how they can occur, and how to handle them. These are the type of errors that actually make your code break and stop executing.
# 
# ## Syntax Errors
# Syntax errors are quite common when you begin coding in Python.
# Here is an example where we attempt to write a for loop but we forget
# the `:`.

# In[2]:


for i in range(2)
    print(i)


# The `SyntaxError` is the type of error that is raised and the little arrow `^` is pointing
# to the first place in the code to where the error is detected. To fix it, we can add the `:` after the closing bracket.

# In[3]:


for i in range(2):
    print(i)


# ## Exceptions
# There are many types of other errors that can occur in your code
# even if the code has proper syntax. Errors that are detected in the
# code during execution are called **exceptions**. 
# 
# For the next example we will use the *image* module we wrote
# and you will need that virtual environment activated if you
# want to run this code.

# In[4]:


from image.image import get_image_content
image_url = 'https://broken_image_url.jpg'
image_content = get_image_content(image_url)


# The above error is rather long because the *requests* library actually tries to 
# download the image content several times and that is why the error is repeated
# more than once. In this case we get a 
# `ConnectionError`, `MaxRetryError`, `NewConnectionError`, `gaierror`. There is part of the error message which shows the context in the code where the exception occurred, in the form of a stack traceback. Here is a screen short of one such part of the stack traceback:
# 
# ![image_stack_trace](image_stack_trace.png)
# 

# In the above screen shot it tells you where the error happened in the code.
# First it shows you the error occured at line 3 in the Notebook cell,
# `image_content = get_image_content(image_url)`. Next it goes a bit deeper and tells
# you the file in which the error occured. In this case it was in the Python file `~/python_intro_udemy/notebooks/image/image.py`. The error occurred in line 8 of the file
# and within the function `get_image_content`. Finally, it goes even further into the *requests*
# library source code and says there was an error when using the `get` function.
# 
# When errors occur, it is quite normal for the printout to be long because they show the complete path
# of the problem. Lets look at some other simpler and yet very common errors built into Python.
# 
# Whenever we divide by 0 a `ZeroDivisionError` is raised.

# In[5]:


5 * (10/0)


# Whenever we try and access a key in a dictionary that is not present,
# a `KeyError` is raised.

# In[6]:


my_dict = {'chris': 35}
my_dict['mike']


# If we try and access a variable that is not defined, a `NameError` is raised.

# In[7]:


4 * my_var + 5


# Here is an example of a `TypeError` in which we try and add a string
# and an integer.

# In[8]:


'10' + 10


# Here is an example of a `ValueError` in which we attempt to convert
# a string to an integer.

# In[9]:


int('chris')


# The above exceptions are just several of the many different [built-in](https://docs.python.org/3/library/exceptions.html#bltin-exceptions) exceptions 
# in Python. It will take time to get use to them and familiar with what they mean.

# ## Handling Exceptions
# 
# In most cases we want our code to raise Exceptions and have errors occur when something
# goes wrong. This way we can figure out the case that caused the error and potentially change the logic within our code. For example, you may get your code to run successfully for many different cases. But then later on there is an edge case that occurs and the code raises an error. Then you can go back and modify your code to handle that edge case.
# 
# However, in some cases we may want to handle selected exceptions directly. We can do this
# with the `try` statement. Let's look at an example. Suppose we are reading some data into a list and we are expecting
# that list to be numbers in the form of strings. In the code below we loop over a list of number strings, convert the string to an integer, add one to the integer, and then print the result.

# In[10]:


for x in ['1', '2', '3', '4', '5', 'hello world', '7', '8', None, '10']:
    print(int(x) + 1)
        


# The code first fails when we get to the string `'hello world'` because we can not convert that to an integer and therefore a `ValueError` is raised. The code will break and the loop will terminate. In some cases we want to handle such errors, take some action, and let the code continue its execution. For example, in this case we could print a simple message and then continue with the rest of the items in the list.
# 
# To do this, we can use a `try` statement and handle specifically any `ValueError` that gets raised.

# In[11]:


for x in ['1', '2', '3', '4', '5', 'hello world', '7', '8', None, '10']:
    try:
        print(int(x) + 1)
    except ValueError:
        print(f'Can not convert "{x}" to integer. Moving onto the next item.')


# You can see that the code did not error out on the `'hello world'` item and moved on to the next items. But now there is another type of error, a `TypeError`, because we tried to convert `None` to an integer. We can also handle this error too like this:

# In[12]:


for x in ['1', '2', '3', '4', '5', 'hello world', '7', '8', None, '10']:
    try:
        print(int(x) + 1)
    except ValueError:
        print(f'Can not convert "{x}" to integer. Moving onto the next item.')
    except TypeError:
        print(f'Can not convert "{x}" to integer. Moving onto the next item.')


# When handling exceptions it is good to handle very specific errors (`ValueError` or `TypeError` for example) like we did above
# by trying to catch either a `ValueError` or `TypeError`. It is possible to catch any generic
# exception with `except Exception` but it is bad practice to have such a generic exception. For example:

# In[13]:


for x in ['1', '2', '3', '4', '5', 'hello world', '7', '8', None, '10']:
    try:
        print(int(x) + 1)
    except Exception:
        print(f'Can not convert "{x}" to integer. Moving onto the next item.')


# It's generally not good to have such a generic exception because it can hide real
# issues that may need to be handled in a different way.

# In genreral, the `try` statement works like this:
# 
# - First, you write the the `try` clause which is the block of statements between the `try` and `except` keywords. This code is executed first.
# 
# ```
# try:
#     try_clause_code_block
# except SomeException:
#     exception_clause_code_block
# ```
# 
# - If no exceptions occur during the execution of the `try_clause_code_block`  then the `except` clause is skipped and execution of the `try` statement is complete.
# 
# - If an exception occurs during execution of the code in the `try_clause_code_block`, the rest of the `try` clause is skipped. 
#     - If the error that is raised matches the exception named after the `except` keyword, the `exception_clause_code_block` is executed.
#     - If the error raised does not match the exception named after the `exception` keyword then the code `exception_clause_code_block` does not get executed. The exception will be raised.
# - A `try` statement may have more than one except clause. But only one of the exception blocks can be executed (whichever comes first).
# 
# ```
# try:
#     try_clause_code_block
# except SomeException1:
#     exception_clause_code_block1
# except SomeException2:
#     exception_clause_code_block2
# except SomeException3:
#     exception_clause_code_block3
# ```
# 

# ### Examples
# Here are some simple examples of exception handling just to get the hang of how it works.

# In[ ]:





# In[ ]:




