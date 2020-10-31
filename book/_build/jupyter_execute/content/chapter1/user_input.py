#!/usr/bin/env python
# coding: utf-8

# # Getting Input From a User
# 
# In Python you can get input from a user with the `input()` function.
# Create a Jupyter Notebook called **user_input** and follow along
# to see how it works. Note that I can not use the `input()` function
# in this book and have it displayed properly. 
# Therefore I will provide a screenshot when using that function.
# 
# In a Jupter Notebook type the following code in a cell
# and then execute the cell.
# 
# `name = input('Enter your name: ')`
# 
# You will be presented with an input box where you
# can enter some text.
# ![user_input](user_input.png) 
# 
# Type your name in the box.
# 
# ![user_input_with_name](user_input_with_name.png)
# 
# Then hit **return** on the keyboard.
# What this does is reads in the input
# as a string (it always converts whatever you enter to a string). 
# Here we store the results with the variable `name` in this
# case. You can than use `name` like any regular Python variable.
# Here we print the type and value of `name`.
# ![user_input_print](user_input_print.png)
# 
# Here is another example:
# ![input_age](input_age.png)
# 
# After typing your age and then hitting return:
# 
# ![input_age_print](input_age_print.png)
# 
# Notice that you entered a number but the type of `age` is string.
# This is because the `input()` function converts whatever
# the user types to a string object. That's it for the `input()`
# function. It provides a simple way to collect input from a user
# which can be fun to play around with in simple programs
# while learning and practicing Python.

# In[ ]:




