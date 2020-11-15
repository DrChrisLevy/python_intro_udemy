#!/usr/bin/env python
# coding: utf-8

# # Data Structures
# 
# There are many types of data structures in Python.
# Data structures are used for storing and organizing data.
# In this chapter we will learn about some of the most common
# data structures in Python such as lists, tuples, dictionaries, and sets.
# 
# Create a new Jupyter Notebook called **data_structures** and follow along.
# 
# # Lists
# You have already learned about lists and
# have used them a lot. Here we will learn
# some more things about lists. It's important
# to remember that lists are **mutable** which
# means you can edit and them and change them after 
# they are created.
# 
# Here we will learn about some more common
# list methods. We have already learned some list
# methods such as `extend` and `append`. Methods
# are a little different then functions and we will
# learn more about methods when we learn about
# object oriented programming. For now, you can sort
# of think as a method as similar to a function. 
# We will not cover all the list methods but you can
# check the official documentation for more [details](https://docs.python.org/3.9/tutorial/datastructures.html)
# 
# ## `sort`
# We can use the `sort` method to sort a list.
# The `sort` method does not return any value
# and sorts the list in place.

# In[1]:


x = [10,60,90,100,-5]
print(x)


# In[2]:


x.sort()


# In[3]:


print(x)


# To sort it in reverse you can use the `reverse` argument.

# In[4]:


y = [0,1,2,3,4]


# In[5]:


y.sort(reverse=True)


# In[6]:


print(y)


# In[7]:


things = ['apple', 'ape', 'dog', 'cat']
print(things)
things.sort()
print(things)
things.sort(reverse=True)
print(things)


# ## `count`
# The `count` method can count
# the number of times an item is in a list.

# In[8]:


x = [1,2,2,2,3,5]


# In[9]:


x.count(-1)


# In[10]:


x.count(1)


# In[11]:


x.count(3)


# In[12]:


x.count(2)


# ## `pop`
# The `pop` method is used to remove an item
# at a specific index. It removes the item from the
# list and returns the value of the item that was removed.
# If you do not specify the position of the item to remove,
# it will automatically remove the last item in the list.

# In[13]:


y = [10, 20, 30, 40, 50]


# In[14]:


y.pop(2)


# In[15]:


print(y)


# In[16]:


y.pop(1)


# In[17]:


print(y)


# In[18]:


y.pop()


# In[19]:


print(y)


# ## `remove`
# The `remove` method is used to remove the
# first item in a list that is equal to some 
# value (provided as an argument). If there is no
# such value, a `ValueError` is raised.

# In[20]:


some_stuff = ['hello', 'bye', 1, 2, -10, 'good', 'bad', 3.14, 'hello']


# In[21]:


some_stuff.remove('hello')
print(some_stuff)


# In[22]:


some_stuff.remove(3.14)


# In[23]:


some_stuff


# ## List Comprehension
# 
# List comprehensions give you a very convenient way to define lists quickly.
# In this section I will show you several types of examples and you can always
# Google more examples too. As you read and write Python code, you will find you will be
# using list comprehensions all the time.
# 
# Suppose you wanted to create a list with the integers between 0 and 10.
# One approach would be this:

# In[24]:


numbers = []
for i in range(11):
    numbers.append(i)
print(numbers)


# We can accomplish the same thing in one line using list comprehensions.

# In[25]:


numbers = [i for i in range(11)]
print(numbers)


# The general syntax for **list comprehensions** is
# ```
# [expression for item in iterable]
# ```
# 
# Its best to learn these by seeing a bunch of examples.

# In[26]:


[x * x for x in range(5)]


# In[27]:


print([character for character in 'Hello there! Hope you have a great day!'])


# In[28]:


print(numbers)


# In[29]:


[x for x in numbers]


# In[30]:


[x * x for x in numbers]


# In[31]:


[x - x for x in numbers]


# In[32]:


[x + x for x in numbers]


# In[33]:


[str(x) for x in numbers]


# You can even add conditional logic to the list comprehensions.

# In[34]:


numbers = [x for x in range(21)]
print(numbers)
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)


# You can use enumerate in list comprehensions as well:

# In[35]:


some_stuff = ['Chris', True, False, 1, 2, 10.8]


# In[36]:


[x for x in some_stuff]


# In[37]:


[x for i,x in enumerate(some_stuff)]


# In[38]:


[i for i,x in enumerate(some_stuff)]


# In[39]:


[[i,x] for i,x in enumerate(some_stuff)]


# In[40]:


countries = ['Canada', 'USA', 'Mexico']
populations = [38000000, 328000000, 126000000]

country_stats = []
for c, p in zip(countries,populations):
    country_stats.append([c,p])
print(country_stats)


# With list comprehensions you can do the above in one line.

# In[41]:


country_stats = [[c,p] for c,p in zip(countries, populations)]
print(country_stats)


# In[42]:


[x[0] for x in country_stats]


# In[43]:


[x[1] for x in country_stats]


# In[44]:


print(country_stats)


# You can even nest list comprehensions to together.
# For example we can unpack/flatten the `country_stats`
# list like this:

# In[45]:


[value for stats in country_stats for value in stats]


# If we wanted to do that same thing with for loops we would have to do:

# In[46]:


values = []
for stats in country_stats:
    for value in stats:
        values.append(value)
print(values)


# There is probably more we could say about list comprehensions
# but this is a good start. Begin to use them when you code and
# you will get the hang of it.

# # Tuples
# 
# Now we will learn about tuples. Tuples are sort of like lists
# but are **immutable** which means you can not change or edit them
# after creation. Instead of using `[]` brackets you use the round brackets
# `()` which are also called parenthesis.

# In[47]:


x = (1, 2, 3)


# In[48]:


x


# In[49]:


type(x)


# In[50]:


len(x)


# In[51]:


x[0]


# In[52]:


x[2]


# In[53]:


x[-1]


# In[54]:


x


# Seems sort of like a list right? But they are **immutable**. You
# can not change them or their values etc.

# In[55]:


x[0] = 2


# In[ ]:


x.append(10)


# In[56]:


x.pop(1)


# So in that sense, they behave differently then lists.

# When you input a tuple you can do so without entering the round brackets.

# In[57]:


y = 1,1,1


# In[58]:


print(y)


# In[59]:


type(y)


# But it is often a good idea to use the `()` when entering a tuple because
# the code is easier to read. Also, sometimes its necessary.

# You can nest tuples just like you did with lists.

# In[60]:


nested_tuple = ((0, 0), (1, 2), (1, 3), (9, 9))


# In[61]:


nested_tuple[-1]


# In[62]:


nested_tuple[-2]


# In[63]:


nested_tuple[-2][0]


# In[64]:


nested_tuple[-2][1]


# One thing to watch out for is the syntax when creating a tuple with a single element.

# In[65]:


x = (1) # this is not a tuple !


# In[66]:


type(x) # it's just an integer


# In[67]:


print(x)


# To create a tuple with a single element you must put a trailing comma.

# In[68]:


x = (1,)


# In[69]:


type(x)


# In[70]:


print(x)


# In[71]:


x[0]


# In[72]:


x[1] # only has one element so this index is out of range


# Tuple **packing** is when you pack things together in a tuple. For example:

# In[73]:


t = ('hello world', 1, True, False, 'Bye')


# In[74]:


print(t)


# In[75]:


type(t)


# In[76]:


len(t)


# You can unpack the tuple `t` like this for example:

# In[77]:


print(t)
a, b, c, d, e = t


# In[78]:


a


# In[79]:


b


# In[80]:


c


# In[81]:


d


# In[82]:


e


# Tuples are used with enumerate.

# In[83]:


print(some_stuff)


# In[84]:


[type(x) for x in enumerate(some_stuff)]


# In[85]:


[x for x in enumerate(some_stuff)]


# To grab just the second element (or first) in each tuple you could do:

# In[86]:


[b for a,b in enumerate(some_stuff)]


# In[87]:


[a for a,b in enumerate(some_stuff)]


# Here is a list of tuples.

# In[88]:


data = [(0,-1,2), (0,4,8), (-2,-2,5), (4,5,6)]


# In[89]:


for d in data:
    print(d)


# Or we can unpack each tuple in the loop like this:

# In[90]:


for a,b,c in data:
    print(f'{a} + {b} + {c} is {a + b + c}')


# Because `data` is a list we can change it.

# In[91]:


data.append('Chris')


# In[92]:


print(data)


# In[93]:


data.pop(0)


# In[94]:


data


# In[95]:


data[2] = False


# In[96]:


data


# But we still can not change one of the tuple items directly.

# In[97]:


data[0]


# In[98]:


data[0][-1] = 9


# We will work with tuples more later.

# # Dictionaries
# 
# Dictionaries are another type of data structure in Python
# and they are super useful. They are **mutable** so you can
# edit them and change them after they are created. Think of them
# as a "look up" where you look up a **key** and get a **value**.
# Dictionaries are essentially a mapping between keys and values.
# You can define a dictionary by enclosing a comma separated list of **key-value** pairs in curly braces `{}`. You use a colon `:` to separate each key from its associated value.

# Here is an example of a dictionary with a persons name as the key and their
# age as the value.

# In[99]:


ages = {'Chris': 35, 'Joanna': 37, 'Penny': 11}


# In[100]:


print(ages)


# In[101]:


type(ages)


# In[102]:


len(ages)


# ## `keys()`
# To list the keys in a dictionary you can use the `keys()` method.

# In[103]:


ages.keys()


# In[104]:


list(ages.keys())


# ## `values()`
# To get the values you can use the `values()` method.

# In[105]:


ages.values()


# In[106]:


list(ages.values())


# If you wrap a dictionary within `list` you will only get the keys.

# In[107]:


list(ages)


# ## Extracting and Storing Values
# So the dictionary is a **mapping** between the *key* and the *value*.
# 
# **KEY** **-------->** **VALUE**
# 
# `'Chris'` **-------->** `35`
# 
# `'Joanna'` **-------->** `37`
# 
# `'Penny'` **-------->** `11`
# 
# The two main operations your perform on a dictionary are
# 
# 1. extracting the value given the key
# 
# 2. storing a value with some key  
# 

# To extract the value of a key you do this:

# In[108]:


ages['Penny']


# It is sort of like getting the value at a position of a list.
# But instead of indexing the position, which is an integer, you
# use the *key* as the index.

# In[109]:


ages['Chris']


# In[110]:


ages['Joanna']


# If you try to get the value of a key that is not in the dictionary
# you will get an error. In particular, a `KeyError`.

# In[111]:


ages['Hazel']


# Dictionaries are **mutable** so we can keep adding additional key value pairs.
# This is how you store a value with some key.

# In[112]:


ages['Hazel'] = 7


# In[113]:


print(ages)


# In[114]:


ages['Isaac'] = 9


# In[115]:


print(ages)


# In[116]:


print(list(ages.keys()))


# In[117]:


print(list(ages.values()))


# In[118]:


ages['Isaac']


# In[119]:


ages['Hazel']


# ## `in` 
# You can use the `in` membership operator to see if a key is in a dictionary
# or if a value is in the dictionary. More common to check if a key is in a dictionary though.

# In[120]:


names = ['Larry', 'Joanna', 'Karen', 'Hazel', 'Isaac', 'Penny', 'Chris', 'Matt', 'Jen']


# In[121]:


len(names)


# In[122]:


ages


# In[123]:


'Chris' in ages # is checking if 'Chris' is one of the keys


# In[124]:


'Matt' in ages


# In[125]:


35 in ages


# In[126]:


35 in ages.values()


# In[127]:


'Chris' in ages.keys()


# In[128]:


9 in ages # same as 9 in ages.keys()


# In[129]:


9 in ages.keys()


# In[130]:


9 in ages.values()


# In[131]:


names


# In[132]:


ages


# In[133]:


for name in names:
    if name in ages:
        print(f'{name} is in the dictionary ages and their age is {ages[name]}.')
    else:
        print(f'{name} is not in the dictionary ages so we do not know their age.')


# ## Different ways to create
# There are multiple ways to create/build dictionaries. We saw one above where we
# we just explicitly defined the initial dictionary within the curly braces `{}`.
# 
# You can use `dict` to build a dictionary from a list of key-value pairs.

# In[134]:


list_of_ages = [('Joanna', 37), ('Chris', 35), ('Penny', 11)] # list of tuples


# In[135]:


dict(list_of_ages)


# If the keys are simple strings then you can even use keyword arguments like this.

# In[136]:


dict(Joanna=1, Chris=35, Penny=11) # only works when the keys will be strings


# You can use **dict comprehension** to build dictionaries too. Suppose we wanted to create
# a dictionary with the keys as integers and the values as those integers squared (the number times it self).

# In[137]:


numbers_squared = {
    0: 0 * 0, 
    1: 1 * 1, 
    2: 2 * 2, 
    3: 3 * 3,
    4: 4 * 4,
    5: 5 * 5,
    6: 6 * 6,
    7: 7 * 7,
    8: 8 * 8,
    9: 9 * 9
}
numbers_squared


# In[138]:


numbers_squared[6]


# We can use a dict comprehension to generate the above dictionary.

# In[139]:


{x: x * x for x in range(10)}


# ## Looping techniques
# Now we will look at some looping techniques when working
# with dictionaries.

# In[140]:


ages


# In[141]:


numbers_squared


# In[142]:


# this will only give the keys
for k in ages:
    print(k)


# In[143]:


# this will only give the keys
for k in numbers_squared:
    print(k)


# In[144]:


for k in ages:
    print(k, ages[k])


# In[145]:


for k in numbers_squared:
    print(k, numbers_squared[k])


# You can use `items()` method to iterate over a dictionary
# and get the key and value at the same time.

# In[146]:


for k,v in ages.items():
    print(k,v)


# In[147]:


for k,v in numbers_squared.items():
    print(k,v)


# You can create an empty dictionary like this

# In[148]:


ages = {}


# In[149]:


print(ages)


# In[150]:


names_list = ['Larry', 'Joanna', 'Karen', 'Hazel', 'Isaac', 'Penny', 'Chris', 'Matt', 'Jen']


# In[151]:


ages_list = [60, 37, 58, 7, 9, 11, 35, 38, 40]


# In[152]:


for name,age in zip(names_list,ages_list):
    print(name,age)


# We can add these names and ages to the empty dict ages,
# and populate it within a loop.

# In[153]:


ages = {}
for name,age in zip(names_list,ages_list):
    ages[name] = age


# In[154]:


ages


# ## Keys are unique

# In[155]:


list(ages.keys())


# In[156]:


list(ages.values())


# In[157]:


ages['Larry']


# In[158]:


ages['Chris']


# In[159]:


ages['Henry'] # not a key in the dict


# In[160]:


# add the key and a value
ages['Henry'] = 'eleven years old'


# In[161]:


ages


# There can not be **duplicate** keys in a dictionary. The keys
# must be unique. So if you assign a value to a key that
# is already in the dictionary it will be updated.

# In[162]:


ages['Henry']


# In[163]:


ages['Henry'] = 11


# In[164]:


ages


# In[165]:


for k, v in ages.items():
    print(f'{k} is {v} years old.')
    


# # Sets
# 
# Python sets are quite simple but can be very useful in certain situations. A set is an unordered collection with no duplicate elements. 

# In[166]:


fruits_list = [ 'oranges', 'grapefruits', 'mandarins', 'limes', 'limes', 'apple', 'apple']
print(fruits_list)


# With a regular list, like the list of `fruits_list` above, you can have duplicates.
# You can use `set` to get the unique items.

# In[167]:


fruits_set = set(fruits_list)
print(fruits_set)
type(fruits_set)


# You see that a set is a list of item between curly braces `{}`.

# In[168]:


my_set_of_stuff = {'Hello', 10, 20, True, False, 3.1459, 'a', False, True, 20}
my_set_of_stuff # see how the duplicates were removed


# You can create an empty set like this:

# In[169]:


x = set()


# In[170]:


type(x)


# Don't use `{}` to create any empty set because it will actually create an empty dictionary.

# In[171]:


y = {}


# In[172]:


type(y)


# ## `add()`
# You can use the `add()` method to add items to a set.

# In[173]:


x = set() # empty set


# In[174]:


x.add('HELLO')


# In[175]:


x


# In[176]:


x.add(True)


# In[177]:


x


# In[178]:


x.add(True) # is already in the set


# In[179]:


x


# In[180]:


for i in range(11):
    if 3 < i < 7:
        x.add(i)
        


# In[181]:


len(x)


# In[182]:


x


# In[183]:


5 in x


# In[184]:


4 in x


# In[185]:


7 in x


# ## `remove`

# In[186]:


print(x)


# In[187]:


x.remove(8) # not in the set so raises error


# In[188]:


x.remove('HELLO')


# In[189]:


x


# In[190]:


x.remove(5)


# In[191]:


x


# Like many of the different data structures introduced here, there is more that could be said. Google is your friend when it comes to learning Python. It's not possible to cover every single topic here. The objective here is to introduce you to the main concepts so you can use these tools when building programs. Then when you get stuck or need some extra functionality, you can do some searching with Google about more information related to these data structures.
# 
# We will end this chapter by returning to functions and 
# learning about `*args` and `**kwargs`. I left this topic until now because
# it requires some knowledge of tuples and dictionaries.
# 
# # Function `*args` and `**kwargs`
# 
# In this section we show how you can have a variable number of
# positional arguments or keyword arguments with the use of
# `*args` and `**kwargs`. Sometimes you don't know exactly the future
# use cases of a function or you may need to have support for additional
# arguments without defining them up front. These are examples where 
# you can use a variable number of arguments which means
# you do not specify the exact number of arguments. Let's look at some examples.

# ## `*args`
# 
# `*args` is used for positional arguments.

# In[192]:


def add_numbers(a, b):
    return a + b


# In[193]:


add_numbers(1,2)


# The above function takes two arguments and adds them together.
# But what if we wanted to have any number of arguments and add them all
# together? You can do that with the unpacking operator `*`. First we will
# use `*args` which supports any number of positional arguments.
# The function will not add the arguments yet. First we will
# see that by using`*args`, you can pass any number of positional arguments
# and `args` is a tuple in the function definition.

# In[194]:


def add_numbers(*args):
    print(args)
    print(type(args))


# In[195]:


add_numbers()


# In[196]:


add_numbers(1)


# In[197]:


add_numbers(1,2)


# In[198]:


add_numbers(1,2,4)


# In[199]:


add_numbers(1,2,4,-9)


# You see? We can pass any number of positional arguments
# to the function and they are all available within a variable name 
# called `args` which is a tuple. So to actually add the numbers
# we can just sum the elements in the tuple.

# In[200]:


def add_numbers(*args):
    return sum(args)


# In[201]:


add_numbers()


# In[202]:


add_numbers(1,2,3)


# In[203]:


add_numbers(10,20,30,40,50,60)


# Here is another example.

# In[204]:


def do_stuff_with_args(*args):
    print(f'You passed {len(args)} positional arguments.')
    print(f'These positional arguments are available in the tuple {args}.')
    for i,x in enumerate(args):
        print(f'The argument at position {i} is {x}.')
    print('We will return the last argument:')
    return args[-1]


# In[205]:


do_stuff_with_args(1,2,3)


# In[206]:


do_stuff_with_args('HI', 'BYE', True, False, 3.14159)


# And it's typical to use the name `args` but you can actually use any name at all
# provided that you use the unpacking `*` operator. For example:

# In[207]:


def do_stuff_with_args(*stuff):
    print(f'You passed {len(stuff)} arguments.')
    print(f'There are available in the tuple {stuff}')
    for i,x in enumerate(stuff):
        print(f'The argument at position {i} is {x}')
    print('We will return the last argument:')
    return stuff[-1]


# In[208]:


do_stuff_with_args(3+4,6+4)


# ## `**kwargs`
# 
# `**kwargs` is similar to `*args` but instead is used for 
# a variable number of keyword arguments. Instead of a tuple,
# `kwargs` is a dictionary.

# In[209]:


def get_person_details(**kwargs):
    print(kwargs)
    print(type(kwargs))


# In[210]:


get_person_details(name='Chris', age=36, city='Halifax')


# In[211]:


def get_person_details(**kwargs):
    for k,v in kwargs.items():
        print(f'The argument {k} has the value {v}.')
        


# In[212]:


get_person_details(name='Chris', age=36, city='Halifax')


# So that's how you can pass a variable number (i.e. any number)
# of keyword arguments using `**kwargs`. And you can use any other name
# as long as you use the `**`. For example

# In[213]:


def get_person_details(**details):
    for k,v in details.items():
        print(f'The argument {k} has the value {v}.')
        


# In[214]:


get_person_details(name='Chris', age=36, city='Halifax', country='Canada')


# It's just common to see `*args` and `**kwargs` but you can use any names
# for these that you want. 
# 
# - `*` is for positional arguments and are accessed with a tuple 
# - `**` is for keyword arguments and are accessed with a dictionary

# ## Ordering of arguments
# 
# We saw in an earlier section that positional
# arguments must come before keyword arguments.
# So that means `*args` must come before `**kwargs`.

# In[215]:


def get_person_details(*args, **kwargs):
    print(args)
    print(kwargs)


# In[216]:


get_person_details('Chris', 36, city='Halifax', country='Canada')


# Just remember that positional arguments
# come before keyword arguments. In general the ordering for arguments is:
# 
#  - regular positional arguments
#  - *args
#  - regular keyword arguments
#  - **kwargs
#  
# Like in this example:

# In[217]:


def get_person_details(name, age, *args, country='Canada', **kwargs):
    print(f'Name is {name}.')
    print(f'Age is {age}.')
    print(f'Country is {country}.')
    
    print(f'Other positional arguments given were: {args}.')
    
    print(f'Other keyword arguments given were:')
    for k,v in kwargs.items():
        print(f'{k}: {v}')


# In[218]:


get_person_details('Chris',
                   35,
                   'Short hair',
                   '6 feet tall', 
                   hair_color='brown', 
                   eye_color='blue',
                   sport='basketball',
                   movie='LOTR')


# Okay so that's an introduction to `*args` and `**kwargs`. I'm sure
# we will use them later throughout the course. It's good to be aware of them.

# In[ ]:




