#!/usr/bin/env python
# coding: utf-8

# # Intro to Functions
# 
# Create a new Jupyter Notebook called **intro_to_functions** and follow along!
# 
# So what is a function anyway? 
# 
# ```{admonition} Functions
# In the Python programming language, a function is a block of reusable code that is typically used to perform a single process or action. Functions are the main building blocks of the programs and applications you create. By using functions, your code will have better modularity and will be easier to reuse. 
# ```
# 
# Python has many built in functions and you can also create your own functions. Functions are not completely new to you and you have already been using functions whether or not you know it. Here are examples of functions, built into Python, that you have
# been using throughout this book and course so far:
# 
# - `print()`
# - `str()`
# - `int()`
# - `float()`
# - `type()`
# - `len()`
# - `range()`
# 
# So what do these **functions** all have in common? Well to begin, they all have **names**. For example, the
# name of the `print()` function is `print`. They can be used or **called** and when you **call** them 
# you always use the brackets `()`. The functions listed above all took input **arguments** which is the stuff you
# type inside the brackets `()`. Another name for **arguments** is **parameters**. In all the cases, the functions performed some action or process by executing a block of Python code internal to that function.
# 
# For example we can use the `len()` function to get the length of a string or a list.

# In[1]:


x = len('Hello')
print(x)


# In[2]:


x = len([0,1,2,3,4])
print(x)


# # Built-in Python Functions
# 
# Python has a number of functions built into it that are always available. You can get a list
# [here](https://docs.python.org/3/library/functions.html) for example. Using this link, you can click
# on the different functions to see what they do and how they are defined in the documentation.
# We will cover some of them here.
# 
# ## `abs()`
# Used to get the absolute value of a number.

# In[3]:


abs(5)


# In[4]:


abs(-5)


# ## `max()` and `min()`
# The `max()` function will return the largest number in an iterable
# and the `min()` function will return the smallest. 
# There are different ways to use these. For example:

# In[5]:


max(1,2) # an example of passing two arguments


# In[6]:


min(1,2)


# In[7]:


max(1,2,5,8) # an example of passing four arguments


# In[8]:


min(1,2,5,8)


# In[9]:


max([1,10,12,10,50,-10,100,-100,1000]) # an example of passing a single list argument


# In[10]:


min([1,10,12,10,50,-10,100,-100,1000]) # an example of passing a single list argument


# ## `round()`
# This function can be used to round to the nearest integer
# or round to a specific number of decimal points.

# In[11]:


round(3.14)


# In[12]:


round(2.51)


# In[13]:


round(3.14,0)


# In[14]:


round(2.51,0)


# In[15]:


round(3.1459,2)


# In[16]:


round(10.12346,4)


# In[17]:


round(10.12344,4)


# ## `sum()`
# For example, to get the sum of the numbers in an iterable (such as a list).

# In[18]:


sum([1,2,3])


# (enumerate)=
# ## `enumerate()`
# This function is very useful when looping over lists and so on.
# Consider the following loop:

# In[19]:


for x in [0,2,4,6,8,10]:
    print(x)


# Often when iterating over a list you not only want
# the value of the item but also the index posiiton of the item
# in the list. This is where `enumerate()` is useful.
# You can use it like this:

# In[20]:


for i, x in enumerate([0,2,4,6,8,10]):
    print(i,x)


# I think this is the first time we have seen a loop with more than
# one variable name. Here we are using `i,x`. The `i` is the index
# position for the item and `x` is the value. For example:

# In[21]:


for i, x in enumerate([0,2,4,6,8,10]):
    print(f'The position of the item is {i} and the value of the item is {x}.')


# ## `zip()`
# This is a neat little function. Here are a couple examples of using it.
# Don't worry too much about the details for now.

# In[22]:


x = [1,2,3]
y = [4,5,6]

for i,j in zip(x,y):
    print(i,j)


# In[23]:


x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
for a,b,c in zip(x,y,z):
    print(a,b,c)


# # Defining your own functions
# It is very common to define your own functions in Python.
# When you are creating programs and applications
# it's normal to have lots of functions defined across
# multiple files. 
# 
# ## DRY (Don't Repeat Yourself)
# 
# One reason for using functions is so you **don't repeat yourself**. 
# This is such a common expression across coding and software engineering
# it even has its own acronym, **DRY**. If you have a block of code
# that is used in multiple places then it's good to create a function for it.
# Then you don't have to copy/paste the code block in every place you want to use
# it. You just need to call the function when and where it's required. 
# Also, if you need to change the function logic,
# you only need to change it in a single place which is in the function definition.
# Let's look at an example with the following code. I know this example is simple
# but try and imagine having more complicated code repeated through out larger projects.
# The same ideas/tools we use here apply to bigger projects as well.

# In[24]:


name1 = 'Isaac'
age1 = 9
name2 = 'Chris'
age2 = 35
name3 = 'Joanna'
age3 = 37
name4 = 'Penelope'
age4 = 10
name5 = 'Hazel'
age5 = 7

print(f'{name1} is {age1} years old.')
print(f'{name2} is {age2} years old.')
print(f'{name3} is {age3} years old.')
print(f'{name4} is {age4} years old.')
print(f'{name5} is {age5} years old.')


# In the above code we have a very similar `print` statement that is 
# repeated multiple times. We can take that logic and put it into
# a function. The function can take two arguments `name` and `age`
# and then print the string. Here is how you define a function to
# do that.

# In[25]:


def print_person_info(name, age):
    print(f'{name} is {age} years old.')


# Every function you define in Python begins with `def`, and next you write the name of the function. In this case the name was `print_person_info`. Next, you write the brackets `()`. You can leave the part within the `()` blank if there are no inputs/arguments/parameters (all mean same thing). In this case we need two arguments `name` and `age`. Then you write a `:` followed by a new line and then the indented code block with the function logic. 
# 
# When you execute code that is a function definition, it does not actually execute the code in the function.
# It just defines it. The code in the function is not executed until the function is actually used or called.
# 
# The previous code above with the 5 print statements can be written like this. Notice that the code appears "cleaner" and more *readable*.

# In[26]:


name1 = 'Isaac'
age1 = 9
name2 = 'Chris'
age2 = 35
name3 = 'Joanna'
age3 = 37
name4 = 'Penelope'
age4 = 10
name5 = 'Hazel'
age5 = 7

print_person_info(name1, age1)
print_person_info(name2, age2)
print_person_info(name3, age3)
print_person_info(name4, age4)
print_person_info(name5, age5)


# Also, suppose we wanted to change the string that is printed. Instead of changing it in 5 places,
# we can just change it in one single place, the function definition. Let's add some more words to
# the string/sentence that is printed.

# In[27]:


def print_person_info(name, age):
    print(f'{name} is {age} years old and they are a very nice person.')


# In[28]:


name1 = 'Isaac'
age1 = 9
name2 = 'Chris'
age2 = 35
name3 = 'Joanna'
age3 = 37
name4 = 'Penelope'
age4 = 10
name5 = 'Hazel'
age5 = 7

print_person_info(name1, age1)
print_person_info(name2, age2)
print_person_info(name3, age3)
print_person_info(name4, age4)
print_person_info(name5, age5)


# We are still repeating ourselves in the code and it can be made shorter and simpler with
# the use of lists and loops. First we will convert the ages and names into a single list
# of lists like this:

# In[29]:


people = [['Isaac', 9], ['Chris', 35], ['Joanna', 37], ['Penelope', 10], ['Hazel', 7]]


# Above we defined a list where each item in the list is also a list.
# Make sure this makes sense to you before continuing.

# In[30]:


print(people[0])
print(people[-1])
print(people[0][0])
print(people[-1][-1])


# So now we can write the simplified code all together like this:

# In[31]:


def print_person_info(name, age):
    print(f'{name} is {age} years old and they are a very nice person.')
    
people = [['Isaac', 9], ['Chris', 35], ['Joanna', 37], ['Penelope', 10], ['Hazel', 7]]
for person in people:
    print_person_info(person[0],person[1])


# We went from code that was about 15 lines long and had lots of repetition to code that is
# 6 lines long and has no repetition. All by using a user defined function and a `for` loop.
# The code is more readable and easier to maintain. 

# ## Let's start simple
# 
# Okay so lets dive more into what functions in Python are 
# and how to define them. Lets start simple with functions
# that do not have any arguments/parameters/inputs (these
# terms all mean the same thing). The general syntax
# for a function with no arguments is
# 
# ```
# def function_name():
#     code_for_function_logic
# ```
# 
# Here are two functions which both execute the same logic.
# The only difference is that they have different function
# names.

# In[32]:


def hello_world1():
    print('Hello World!')
    
def hello_world2():
    print('Hello World!')


# Notice that when you execute the above code nothing is printed.
# This is because the code within the functions is not executed
# when the functions are defined. The above code simply
# defines the functions so that you can access the functions
# by name in your code and call them, like this:

# In[33]:


hello_world1()
hello_world2()


# Above we saw how to use/call the functions. You use the function name and you also require 
# the brackets `()`.
# 
# You can not use a function before having it
# defined and available to the Python program/code.
# For example,

# In[34]:


hello_world3()


# Our Python interpreter (the thing that reads and executes the code)
# has no idea what `hello_world3` is and returns a `NameError`.
# You need to define the function before you use it.

# In[35]:


def hello_world3():
    print('Hello World!')
hello_world3()


# ## Test your Functions!
# You can have a bug in your function code and you
# may not even know it until you go and use/call the function. 
# 
# ```{admonition} Bug
# In programming, a bug is a common term which simply means error, mistake,
# or some problem with the code. Most bugs are due to human error in writing
# the code. Debugging is the act of finding and removing such bugs in the code.
# ```
# 
# Lets look at a simple example.
# When doing division you can never divide by 0.
# If you attempt this in Python you will get an error.

# In[36]:


1 / 0


# In[37]:


def do_something():
    x = 1
    y = 2
    print(x + y)
    z = 1 / 0


# You see the bug in the function definition above? The
# error is when we do `z = 1 / 0`. The code before that line is fine.
# When we execute the above code there is no error
# because the code above is simply defining the function. The code within the function is not executed.
# It will not be executed until you call the function (which means to use it).

# In[38]:


do_something()


# Notice that the code began to execute and `3` was printed.
# But then when it goes to execute the line `z = 1 / 0`
# an error occurs.
# Python attempts to tell you where the error is. 
# It says there is an error in the function `do_something()`
# and it tells you the issue is at line 5 in the function definition
# when it does `z = 1 / 0`. It
# also gives you specifics about the error which is a `ZeroDivisionError`.
# 
# Always remember to test your functions.

# ## Local variables
# 
# Variables that are defined within a function definition
# are local to that function and can only be accessed within
# the function.
# They can not be accessed outside function definition in
# other code.

# In[39]:


def add_w_and_q():
    w = 10
    q = 20
    print(f'{q} + {w} is equal to {q + w}')


# In[40]:


add_w_and_q()


# In[41]:


print(w)


# In[42]:


print(q)


# Those errors are because `w` and `q` are only defined local
# to the function definition `add_w_and_q()`. This idea is known
# as local variables and you will often here coders refer
# to the *local scope*. It just means the scope of those
# variables are local to the function definition.
# 
# If you have a variable defined outside a function,
# it can actually be accessed within the local
# function definition.

# In[43]:


def add_w_and_q():
    w = 10
    q = 20
    print(f'{q} + {w} is equal to {q + w}. The value of x is {x}.')


# In[44]:


x = 5
add_w_and_q()


# In[ ]:





# It's not usually a good idea to have variables
# defined in a function that are also defined outside
# the function. It can be harder to keep track of things.
# Consider this example. In this example when we print the
# value of `x` in the function definition it will take the value
# of `x` defined in the function. Outside the function it will use 
# the value of `x` defined outside the function. In general,
# try to avoid this coding pattern.

# In[45]:


def print_local_x_value():
    x = -99
    print(f'The value of x defined in the function is {x}.')


# In[46]:


x = 5
print_local_x_value()
print(f'The value of x outside the function is {x}')
x = 33
print_local_x_value()
print(f'The value of x outside the function is {x}')


# ## `return` statement
# 
# So far we know that functions execute a block of code
# and that code can do anything we want it to.
# In the above examples we were simply printing something.
# A lot of the time we want the function to return
# a Python object. To do this we use the `return` statement.

# In[47]:


def add_x_and_y():
    x = 1
    y = 2
    result = x + y
    return result


# In[48]:


add_x_and_y()


# In[49]:


z = add_x_and_y()


# In[50]:


print(z)


# This is very common to do with the use of functions.
# The function will perform some computation
# and we want to get the result back.
# 
# A function can have multiple `return` statements within its definition.
# For example, you might return different values
# depending on some internal logic to the function.
# However, only one `return` statement can ever be
# executed in any function at once. Whichever `return`
# statement is executed first will be the one that is used.
# As soon as the `return` statement is executed,
# any remaining code in the function definition 
# will be skipped over. For example:

# In[51]:


def example_return():
    x = 10
    y = 20
    
    if x == 10: # this condition is True
        return x # code gets to this return statement first so will be executed 
    
    if y == 20: # this condition is True
        return y # will never be executed 


# In[52]:


example_return()


# ## Positional Arguments

# Consider the following function `subtract_numbers`.

# In[53]:


def subtract_numbers():
    x = 5
    y = 3
    return x - y


# In[54]:


subtract_numbers()


# The function is very limited in its use cases
# because it only can subtract `5-3` and always will
# return `2`. What if we could pass any two numbers
# as input to the function and get back the result 
# when we do the first number subtract the second number?
# We can accomplish this with **arguments**. Arguments
# are also called **parameters** and both words mean the same
# thing. The arguments are the inputs to the function
# and you define and pass them within the brackets `()`
# of the function.
# 
# Here we define the function `subtract_numbers` to take
# two arguments `x` and `y` which must be passed to the
# function when calling it.

# In[55]:


def subtract_numbers(x, y):
    return x - y


# This will raise an error because we did not pass
# any values for the arguments.

# In[56]:


subtract_numbers()


# You must provide the value of the arguments.
# When we call the function in this way,
# the arguments are called **positional**
# arguments because the order/position in which they
# are entered/passed matters. The first argument is
# the value for `x` and the second argument is the
# value for `y`.

# In[57]:


subtract_numbers(10, 7)


# In[58]:


subtract_numbers(7, 10)


# In[59]:


subtract_numbers(10, 20)


# In[60]:


subtract_numbers(20, 10)


# Here is a function that returns `True` if the number is even and `False` otherwise.

# In[61]:


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    


# In[62]:


is_even(9)


# In[63]:


is_even(8)


# ## Keyword Arguments
# 
# We just learned about positional arguments where the position/order
# of the arguments is important. You can also use **keyword** arguments
# in which you provide the argument name and the value when calling the function.
# Lets change the definition of `subtract_numbers` to take three arguments
# and subtract `x - y - z` and return the result.

# In[64]:


def subtract_numbers(x, y, z):
    result = x - y - z
    print(f'{x} take away {y} take away {z} is {result}')
    return result


# This is an example of passing positional arguments.

# In[65]:


subtract_numbers(10, 5, 3)


# Here is an example of calling the same function
# but now with **keyword arguments**.
# With **keyword** arguments you provide
# the argument name on the left of the `=`
# and the value on the right.

# In[66]:


subtract_numbers(x=10, y=5, z=3)


# When using all keyword arguments you can pass the arguments
# in any order. Notice that we get the same result as above.

# In[67]:


subtract_numbers(z=3, x=10, y=5)


# You can also mix positional arguments and keyword arguments
# but **positional arguments must be specified before keyword arguments**.
# For example:

# In[68]:


subtract_numbers(10, 5, z=3)


# In[69]:


subtract_numbers(10, y=5, z=3)


# You can not put keyword arguments before positional arguments.

# In[70]:


subtract_numbers(x=10, y=5, 3)


# ## Default arguments
# It is often convenient to define default values for arguments.
# These are called default arguments. Consider the following
# function which computes the cost of something after taxes
# given the cost before tax and the tax rate. We will assume
# the `tax_rate` is a float between 0 and 1. So a value of
# `0.15` for `tax_rate` means 15% tax.

# In[71]:


def cost_after_tax(cost_before_tax, tax_rate):
    total_cost = cost_before_tax + tax_rate * cost_before_tax
    return total_cost


# In[72]:


cost_after_tax(100, 0.15)


# In[73]:


cost_after_tax(cost_before_tax=500, tax_rate=0.50)


# In[74]:


cost_after_tax(tax_rate=.25, cost_before_tax=1000)


# In[75]:


cost_after_tax(100, tax_rate=0.35)


# The above examples show different examples
# of calling the function with just positional arguments, just keyword arguments,
# and a mixture of both.
# 
# But what if we wanted to have a default tax value? For example,
# depending on where you live the tax rate is probably very consistent.
# For example, the tax rate might be 15%. Then you don't want to have to
# provide that argument every time you use the function. But you will want
# the ability to change it when it suits your needs. This is the use case of
# **default** arguments. When you define your function you can provide
# default arguments by providing the argument name on the left of the `=`
# sign and the default value on the right. Like this:

# In[76]:


def cost_after_tax(cost_before_tax, tax_rate=0.15):
    total_cost = cost_before_tax + tax_rate * cost_before_tax
    return total_cost


# In[77]:


cost_after_tax(100)


# In[78]:


cost_after_tax(cost_before_tax=100)


# Since there is not a default value for `cost_before_tax` it must be provided.

# In[79]:


cost_after_tax()


# So if we don't provide the value for `tax_rate` it will default to 0.15.
# If we provide it, then that provided value will be used.

# In[80]:


cost_after_tax(100, 0.2)


# ## Docstrings
# 
# Docstrings are strings which document your functions. 
# They are like comments in your code that tell you
# about a function, its arguments, and its return values.
# It's really important to document code because code is
# read more than it is written.
# 
# Remember we can use `#` to create in line comments
# in our Python code. But docstrings for a function are different.
# You can create them with `""""""`. 
# These docstrings are built-in strings that
# help you and other users of your code document thee code. 
# Python also has a built in function `help()` that 
# can print the docstring of a function. Try
# executing `help(str)` or `help(float)` and so on.
# You will see the functions documentation printed.

# In[ ]:





# In[81]:


def my_func(a,b,c):
    """One line intro.
    
    Longer description if needed.
    
    :param int a: descripton for the first argument/parameter
    :param int b: descripton for the second argument/parameter
    :param int c: descripton for the third argument/parameter
    :return: description for what the function returns
    """
    
    return a + b + c


# In[82]:


help(my_func)


# There is a lot more to say about docstrings but will save this until
# later when we start to use a proper editor to write Python code.
# For now, feel free to document your functions with docstrings but
# stick to the format above. The syntax, use of `:` and spacing and new lines
# is quite important. We will use docstrings in the below examples too.

# # Examples
# In this section we will show some examples which use functions. Spend time reading the code, typing the code, and using the code. 
# This is a good way to learn.
# By going through these examples, hopefully you will get more comfortable
# with the idea of working with functions and defining your own.
# 
# ## Example 1
# This is an example of a function that does not return anything.

# In[83]:


def greeting(name, message):
    """Print a simple greeting message.
    
    :param str name: The name of the person to greet.
    :param str message: A simple message to print to the user.
    """
    print(f'Hello {name}!')
    print(message)


# In[84]:


help(greeting)


# In[85]:


greeting('Chris','Good morning! I hope you have a great day!')


# In[86]:


greeting(message='Do not forget your lunch today for school.', name='Isaac')


# In[87]:


greeting('Hazel', message='Good Bye!')


# ## Example 2
# This function computes the area of a circle given it's radius.
# 

# In[88]:


def area_circle(radius):
    """Compute the area of a circle."""
    
    pi = 3.1459
    area = pi * radius * radius
    return area


# In[89]:


area_circle(2.5)


# In[90]:


area_circle(radius=1)


# ## Example 3
# A function to return a random list of numbers
# of any length where all the numbers are between
# a minimum and maximum value.

# In[91]:


import random

def generate_random_list(list_length, minimum, maximum):
    """Generate a list of random integers.
    
    The length of the list can be specified as well
    as the range (minium, maximum) of the numbers that will be used.
    
    :param int list_length: The length of the list to be returned.
    :param int minimum: The smallest possible value for any of the numbers.
    :param int maximum: The largest possible value for any of the numbers.
    :return: The list of random numbers.
    :rtype: list
    """
    
    list_of_numbers = []
    for i in range(list_length):
        random_int = random.randint(minimum, maximum)
        list_of_numbers.append(random_int)
    return list_of_numbers


# In[92]:


generate_random_list(7, 0, 10)


# In[93]:


generate_random_list(list_length=10, minimum=100, maximum=109)


# In[94]:


generate_random_list(2, 100000, maximum=200000)


# ## Example 4
# 
# In this example we will create a few functions. One for determining if a number is 
# prime, another for getting the list of prime numbers up to a specific number, and the final
# one for finding the first so many primes. Remember a prime number is any number larger than 1
# that is only divisible by 1 and itself. For example, here are some prime numbers
# 
# $$2,3,5,7,11,13,17,19,23,29,...$$
# 
# It is certainly possibly to code all the logic in a single function. However, it's a better
# design for functions to be responsible for a single task. This way those functions can
# used again in other programs for particular tasks and it generally makes the code easier
# to read and easier to test and debug. So always keep that in mind when coding. Try and think
# of your functions as individual units that are responsible for doing one thing specific thing.
# It's not a hard rule but a good general rule of thumb.
# This is also a great example of our user defined function calling 
# another user defined function (a perfectly normal and common thing to do).

# In[95]:


def is_prime(number):
    """Determines if a number is prime or not
    
    Assumes number >= 2.
    """
    if number <=3:
        return True
            
    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

def find_primes_up_to(up_to=100):
    """Returns a list of all the prime numbers up to some point."""
    primes = []
    for i in range(2, up_to + 1):
        if is_prime(i):
            primes.append(i)
    return primes            

def find_first_n_primes(n=100):
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes
        


# In[96]:


is_prime(2)


# In[97]:


is_prime(3)


# In[98]:


is_prime(4)


# In[99]:


is_prime(53)


# In[100]:


is_prime(100)


# In[101]:


find_primes_up_to()


# In[102]:


find_primes_up_to(40)


# In[103]:


find_primes_up_to(10000)[-5:]


# In[104]:


find_first_n_primes(10)


# In[105]:


find_first_n_primes(20)


# In[106]:


find_first_n_primes(1000)[-1] # the 1000th prime number


# In[ ]:




