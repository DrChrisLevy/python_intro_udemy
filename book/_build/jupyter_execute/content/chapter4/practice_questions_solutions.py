#!/usr/bin/env python
# coding: utf-8

# # Practice Questions (Solutions)

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
# 
# ### Solution

# In[1]:


def get_list_details(l):
    print(f'The list is {l}.')
    l.sort()
    print(f'The list sorted is {l}.')
    return l

get_list_details([10, -4, 5, 10, 78])


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
# ### Solution

# In[2]:


def count_items_v1(x):
    counts = {}
    for i in x:
        count = x.count(i)
        counts[i] = count
    return counts

# this method is better because it only counts each unique number once
def count_items_v2(x):
    counts = {}
    unique_numbers = set(x) # b/c of this step here
    for i in unique_numbers:
        counts[i] = x.count(i)
        print(i, x.count(i))
    return counts


# In[3]:


count_items_v2([1, 2, 3, 4, 5])


# In[4]:


count_items_v2([1, 1, 1])


# In[5]:


count_items_v2([1, 1, 1, 2, 2, 2, 2, 4])


# ## 3.
# 
# Write a function that takes a list as input and removes the first
# item and the last item from the list. The function should return a tuple of length two.
# The first item in the tuple should be the list without the items that were removed. 
# The second item in the tuple should be the list with only the two numbers that were removed. You should use the `pop()` method.
# 
# For example,
# 
# `remove_first_and_last([1,2,3,4])` would return `([2, 3], [1, 4])`.
# 
# `remove_first_and_last([1, 2])` would return `([], [1, 2])`.
# 
# `remove_first_and_last([-10, 20, 50])` would return `([20], [-10, 50])`.
# 
# ### Solution

# In[6]:


def remove_first_and_last(w):
    numbers_removed = [w.pop(0), w.pop()]
    return w, numbers_removed # can put tuple brackets i.e. () if you want
    
    


# In[7]:


remove_first_and_last([1,2,3,4])


# In[8]:


remove_first_and_last([1,2])


# In[9]:


remove_first_and_last([-10, 20, 50])


# ## 4.
# 
# a) Use list comprehensions to create a list of integers between (and including) 16 and 57.
# 
# b) Use list comprehensions to create a list of **odd** integers between (and including) 11 and 31.
# 
# c) Given the list `x = [1, 2, 'hello world', -3, 5]` use list comprehensions and `enumerate` to create a new list `[(0, 1), (1, 2), (2, 'hello world'), (3, -3), (4, 5)]`.
# 
# d) Given a list of numbers in a variable called `numbers`, use list comprehensions to extract all the numbers with a position/index that is a multiple of 3. For example, if `numbers` was the list `[7, 5, 6, 9, 4, 5, 2]` then the list comprehension would create the list `[7, 9, 2]` because those numbers were at positions 0,3,6. Remember that you can use conditionals in list comprehensions and you can use `n % 3 == 0` to check if a number `n` is a multiple of 3. Also, you will want to use `enumerate` in the list comprehension so that you have the position of each item. 
# 
# ### Solution

# #### a)

# In[10]:


[x for x in range(16,58)]


# #### b)

# In[11]:


[x for x in range(11,32) if x % 2 == 1]


# #### c)

# In[12]:


x = [1, 2, 'hello world', -3, 5]
[z for z in enumerate(x)]


# #### d)

# In[13]:


numbers = [7, 5, 6, 9, 4, 5, 2]
[x for i,x in enumerate(numbers) if i % 3 == 0]


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
# 
# ### Solution

# #### a)

# In[14]:


(5,7,8,6436.5325,'hello world', True, False, [1,2,3,4], (9,9,9,9,9))


# #### b)

# In[15]:


x = ('hello there', False, [9,8,7])


# In[16]:


a,b,c = x
print(a)
print(b)
print(c)


# #### c)
# 

# In[17]:


a=(1,2,3)
b=(4,5,6,6)
c = a + b
c


# #### d)

# In[18]:


def is_in_tuple(numbers, num):
    if num in numbers:
        print(f'YES, {num} is in {numbers}.')
    else:
        print(f'NO, {num} is not in {numbers}.')
    


# In[19]:


is_in_tuple((1,2,8,5,7), 8)


# In[20]:


is_in_tuple((1,2,8,5,7), 123)


# ## 6.
# 
# Given the following lists for example:

# In[21]:


instruments = ['guitar', 'drums', 'piano']
prices = [400, 500, 600]
colors = ['red', 'black', 'white']


# Write code that merges them together and creates a list of tuples like this
# 
# ```[('guitar', 'red', 400), ('drums', 'black', 500), ('piano', 'white', 600)]```
# 
# Your code should work on any three lists in this format. Try doing this question with
# and without using list comprehensions. Also, use the `zip()` method.
# 
# ### Solution

# In[22]:


# without list comprehension and unpacking
results = []
for instrument, price, color in zip(instruments, prices, colors):
    results.append((instrument, color, price))
print(results)

# without list comprehension and no packing
results = []
for x in zip(instruments, colors, prices):
    results.append(x)
print(results)


# In[23]:


# with list comprehensions
[x for x in zip(instruments, colors, prices)]


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
# 
# ### Solution

# In[24]:


def total_payments(data):
    names = set([d[0] for d in data])
    sum_payments = {name: 0 for name in names}
    
    for name, payment in data:
        sum_payments[name] = sum_payments[name] + payment
    return sum_payments


# In[25]:


data = [('Chris', 3245.53), ('Joanna', 3498.43), ('Penny', 134.00), ('Isaac', 583.35),
('Chris', 4300.54), ('Joanna', 3498.43), ('Penny', 957.97), ('Isaac', 0.00),
('Henry', 10.10), ('Jen', 34.45), ('Matt', 0.00)]

total_payments(data)


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
# 
# ### Solution

# In[26]:


data = [
 {'name': 'Steph Curry',
 'team': 'Golden State Warriors',
 'points_per_game': 23.5},
 
 {'name': 'Lebron James',
 'team': 'Los Angeles Lakers',
 'points_per_game': 27.1},
 
 {'name': 'James Harden',
 'team': 'Houstan Rockets',
 'points_per_game': 25.2},
 
 {'name': 'Kawhi Leonard',
 'team': 'Los Angeles Clippers',
 'points_per_game': 18.7},
 
 {'name': 'Paul George',
 'team': 'Los Angeles Clippers',
 'points_per_game': 20.0},
 
 {'name': 'Kevin Durant',
 'team': 'Brooklyn Nets',
 'points_per_game': 27.0}
]
data


# In[27]:


list(set([d['name'] for d in data]))


# In[28]:


list(set([d['team'] for d in data]))


# In[29]:


# highest score
highest_score = data[0]
for d in data[1:]:
    if d['points_per_game'] >= highest_score['points_per_game']:
        highest_score = d
print(highest_score)
    
    


# In[30]:


# lowest score
lowest_score = data[0]
for d in data[1:]:
    if d['points_per_game'] <= lowest_score['points_per_game']:
        lowest_score = d
print(lowest_score)
    
    


# In[31]:


scores = [d['points_per_game'] for d in data]
scores.sort()
print(scores)
mean = sum(scores)/len(scores)
print(mean)


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
# 
# ### Solution

# In[32]:


def stats(*numbers):
    smallest = min(numbers)
    largest = max(numbers)
    average = sum(numbers)/len(numbers)
    return (smallest, largest, average)


# In[33]:


stats(9,5,6,10,4)


# In[34]:


stats(2,4)


# In[35]:


stats(12.423,86.234, 98375, 100.2345)


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

# In[36]:


def get_car_details(year, make, **kwargs):
    kwargs['year'] = year
    kwargs['make'] = make
    return kwargs


# In[37]:


get_car_details(2009, 'BMW', color='black')


# In[38]:


get_car_details(2009, 'honda')


# In[39]:


get_car_details(2020, 'ford', color='red', doors=4)

