#!/usr/bin/env python
# coding: utf-8

# # Practice Questions

# ## 1.
# 
# Write a function called `get_list_details` that takes a list as its only argument.
# Then the function should print the list, print the sorted list, and return the list sorted.
# For example:
# 
# ```
# get_list_details([10, -4, 5, 10, 78])
# ```
# 
# would print the output
# 
# The list is: [10, -4, 5, 10, 78]
# 
# The list sorted is: [-4, 5, 10, 10, 78]
# 
# 
# and would return [-4, 5, 10, 10, 78].

# ## 2.
# 
# In this chapter we learned the `count()` method for lists
# which returns the number of times an item is in a list.
# Using the `count` function and dictionaries, write a function which takes a list of numbers as input and returns
# a dictionary with the keys as the numbers in the list and
# the values as the number of times those numbers appear in the list.
# 
# For example,
# 
# `count_items([1, 2, 3, 4, 5])` would return `{1: 1, 2: 1, 3: 1, 4: 1, 5: 1}`.
# 
# 
# `count_items([1, 1, 1])` would return `{1: 3}`.
# 
# `count_items([1, 1, 1, 2, 2, 2, 2, 4])` would return `{1: 3, 2: 4, 4: 1}`.
# 
# 
# 

# ## 3.
# 
# Write a function that takes a list as input and removes the first
# item and the last item in the list. Then the list with the removed
# items is returned. You should use the `pop()` method.
# 
# For example,
# 
# `remove_first_and_last([1,2,3,4])` would return `[2, 3]`.
# 
# `remove_first_and_last([1, 2])` would return `[]`.
# 
# `remove_first_and_last([-10, 20, 50])` would return `[20]`.

# ## 4.
# 
# a) Use list comprehensions to create a list of integers between (and including) 16 and 57.
# 
# b) Use list comprehensions to create a list of **odd** integers between (and including) 11 and 31.
# 
# c) Given the list `x = [1, 2, 'hello world', -3, 5]` use list comprehensions and `enumerate` to create a new list `[(0, 1), (1, 2), (2, 'hello world'), (3, -3), (4, 5)]`.
# 
# d) Given a list of numbers in a variable called `numbers`, use list comprehensions to extract all the numbers with a position/index that is a multiple of 3. For example, if `numbers` was the list `[7, 5, 6, 9, 4, 5, 2]` then the list comprehension would create the list `[7, 9, 2]` because those numbers were at positions 0,3,6. Remember that you can use conditionals in list comprehensions and you can use `n % 3 == 0` to check if a number `n` is a multiple of 3. Also, you will want to use `enumerate` in the list comprehension so that you have the position of each item. 

# ## 5.
# 
# a) Create a tuple with different data types in it.
# 
# b) Create a tuple of length 3 and then unpack the values into three variables `a,b,c`.
# 
# c) Given two tuples `a` and `b`, create a new tuple `c` with the elements from `a` and `b`.
# For example if `a=(1,2,3)` and `b=(4,5,6,6)` then `c` would be `(1,2,3,4,5,6,6)`.
# 
# d) Create a function that takes two arguments. The first argument is a tuple of numbers. The second argument is a number. The function should print a message which says if the number (second argument) is in the tuple (first argument) or not.

# ## 6.
# 
# Given the following lists for example:

# In[1]:


instruments = ['guitar', 'drums', 'piano']
prices = [400, 500, 600]
colors = ['red', 'black', 'white']


# Write code that merges them together and creates a list of tuples like this
# 
# ```[('guitar', 'red', 400), ('drums', 'black', 500), ('piano', 'white', 600)]```
# 
# Your code should work on any three lists in this format. Try doing this question with
# and without using list comprehensions. Also, use the `zip()` method.

# ## 7.
# 
# Write a function which takes a **list of tuples** as input where each tuple is of the form
# `(PERSON_NAME, PAID_AMOUNT)`. `PERSON_NAME` is a string and `PAID_AMOUNT` is a number. For instance `('Chris', 3245.53)` is an example of a tuple that could be in the list. An example of the input list with multiple tuples could be
# 
# ```
# [('Chris', 3245.53), ('Joanna', 3498.43), ('Penny', 134.00), ('Isaac', 583.35),
# ('Chris', 4300.54), ('Joanna', 3498.43), ('Penny', 957.97), ('Isaac', 0.00),
# ('Henry', 10.10), ('Jen', 34.45), ('Matt', 0.00)]
# ```
# 
# Each tuple indicates how much money the person was paid. If the name appears more than once it means that person was paid multiple times. The function should take the list of tuples as input and return a dictionary. The keys of the dictionary should be the names and the values should be the total sum of the money they were paid. For example, for the above input list example the output returned by the function should be:
# 
# ```
# {'Chris': 7546.07,
#  'Joanna': 6996.86,
#  'Penny': 1091.97,
#  'Isaac': 583.35,
#  'Henry': 10.1,
#  'Jen': 34.45,
#  'Matt': 0.0}
# ```

# ## 8.
# 
# In this question you can assume you have data which is a list of NBA players. Assume the data is a list of dictionaries formatted like this, where each dictionary in the list contains details about a single player.
# 
# ```
# [
#  {'name': 'Steph Curry',
#  'team': 'Golden State Warriors',
#  'points_per_game': 23.5},
#  
#  {'name': 'Lebron James',
#  'team': 'Los Angeles Lakers',
#  'points_per_game': 27.1},
#  
#  {'name': 'James Harden',
#  'team': 'Houstan Rockets',
#  'points_per_game': 25.2},
#  
#  {'name': 'Kawhi Leonard',
#  'team': 'Los Angeles Clippers',
#  'points_per_game': 18.7},
#  
#  {'name': 'Paul George',
#  'team': 'Los Angeles Clippers',
#  'points_per_game': 20.0},
#  
#  {'name': 'Kevin Durant',
#  'team': 'Brooklyn Nets',
#  'points_per_game': 27.0}
# ]
# ```
# 
# Write Python code which does the following:
# 
# - gets the unique list of player names
# - gets the unique list of team names
# - gets the dictionary for the person with the highest points_per_game 
# - gets the dictionary for the person with the lowest points_per_game 
# - creates a list with all the points_per_game values sorted from smallest to largest.
#     - finds the mean/average of the list of points_per_game values
# 
# You can display the results however you want and feel free to write 
# some functions as well.

# ## 9.
# 
# Write a function which can take any number of positional arguments as input
# and assume all the arguments are numbers. The function should return a tuple
# of length 3 with the smallest number, largest number, and the average of the numbers.
# 
# For example,
# 
# `stats(9,5,6,10,4)` should return `(4, 10, 6.8)`
# 
# `stats(2,4)` should return `(2, 4, 3)`
# 
# `stats(12.423,86.234, 98375, 100.2345)` should return `(12.423, 98375, 24643.472875000003)`

# ## 10.
# 
# Write a function `get_car_details` which takes 2 required positional arguments `year` and `make` and any variable number of additional keyword arguments. Then the function should return a dictionary with the details about the car. For example:
# 
# `get_car_details(2009, 'honda')` should return 
# 
# ```
# {'year': 2009, 'make': 'honda'}
# ```
# 
# 
# `get_car_details(2009, 'honda', color='black')` should return 
# 
# ```
# {'color': 'black', 'year': 2009, 'make': 'honda'}
# ```
# 
# `get_car_details(2020, 'ford', color='red', doors=4)` should return
# 
# ```
# {'color': 'red', 'doors': 4, 'year': 2020, 'make': 'ford'}
# ```
# 
# `get_car_details(color='blue')` should raise a `TypeError` because it's missing the
# two required positional arguments `year` and `make`.

# In[ ]:




