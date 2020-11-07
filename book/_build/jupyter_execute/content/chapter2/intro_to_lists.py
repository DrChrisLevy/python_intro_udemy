#!/usr/bin/env python
# coding: utf-8

# # Intro to Lists
# 
# In this section we are going to learn about the **list**
# data type in Python. Python lists are examples of
# sequence types because they behave like a sequence 
# (an ordered collection of objects).
# 
# Here we define two lists so we can learn by example.
# Be sure to create a Jupyter Notebook and call it
# **intro_to_lists** and follow along.

# In[1]:


fruits = ['apple', 'orange', 'banana']
numbers = [1,2,3,4]


# In[2]:


type(fruits)


# In[3]:


type(numbers)


# A **list** in Python is just a list of objects
# separated by commas and enclosed between two square
# brackets `[]`. The objects within the list can
# be of any data type. Here is another list with 
# strings, integers, floats, and boolean data types mixed together.

# In[4]:


another_list = ['hello world', 3.1459, -10, 0, 'hey', 1 + 5, True, False]
print(type(another_list))
print(another_list)


# Here is an empty list.

# In[5]:


[]


# Here is a list with duplicates, which is totally fine.

# In[6]:


[1,2,1,1,2,2,2,2,'chris','hello',True,False,False,True,True,2,2,2]


# (list-index-slice)=
# ## List Indexing and Slicing
# We can index and slice lists 
# the same way we did with strings.
# Here are examples. Note that the syntax is the exact same.

# In[7]:


print(fruits)


# In[8]:


fruits[0]


# In[9]:


fruits[1]


# In[10]:


fruits[2]


# In[11]:


fruits[-1]


# In[12]:


fruits[-2]


# In[13]:


fruits[0:2]


# In[14]:


fruits[0:10]


# In[15]:


fruits[10] # error because outside the index range


# In[ ]:


print(another_list)


# In[16]:


another_list[::2] # from start to end and taking every 2nd element


# In[17]:


another_list[::-1] # reversed list


# ## `len()` function
# You can use the `len` function to get
# the number of items in an object.
# The types of objects we have seen 
# for which we can use `len()` are *strings* and 
# *lists*.

# In[18]:


# getting the length of a list
print(numbers)
print(len(numbers)) # there are 4 items in the list


# In[19]:


print(another_list)
print(len(another_list)) # there are 8 items in the list


# In[20]:


# getting the length of a string
x = 'Hello World !'
print(len(x)) # there are 13 characters in the string


# (append-list)=
# ## `append()` to List
# 
# The list object is an example of a mutable object.
# This means you can change it after it's created.
# For example, you can append items to a list, remove items from a list,
# and so on. Simply put, a **mutable** object can be changed 
# after it is created, and an **immutable** object can not. 
# Examples of objects we have seen so far which are **immutable** are
# integer, string, and float objects. Lists however are 
# **mutable**. 
# 
# Let's define a list and then add items to it with the `append()` method.
# A *method* is sort of like a *function* but different. Do not worry about
# it for now. Just know there exists a *method* called `append` and here you will see
# how to use it.

# In[21]:


my_list = ['sunny day',-5]
print(len(my_list))
print(my_list)


# In[22]:


my_list.append(2.71)
print(len(my_list))
print(my_list)


# In[23]:


my_list.append('bye')
my_list 


# Notice that the `append()` method modifies the list in place.
# There is no need to assign the result to another new variable name.

# ## List Concatenation with `+`
# Just like we concatenated strings with the `+` operator,
# we can also do a similar thing with lists.

# In[24]:


a = [1,2,3]
b = [4,5,6]
c = a + b
print(a)
print(b)
print(c)


# In[25]:


c = a + a + a + a
print(c)


# ## `extend()` method
# The `extend()` method adds all the elements of a list to the end of the list.
# It modifies the list in place. Let's look at an example.

# In[26]:


# we already defined these two lists
print(f'a is {a}')
print(f'b is {b}')


# In[27]:


a.extend(b)
print(b) # b stays the same
print(a) # the items from b were added to a


# ## Lists are Mutable
# We just saw that lists are mutable which can lead
# to some "confusing" behavior for beginners in Python.
# We will learn more about this sort of thing as the course
# progresses. Here is another example of 
# editing/changing a list after it's created.
# It will change any variable that is a reference to that object.

# In[ ]:





# In[28]:


list1 = [1,2,3]
list2 = list1
print(list1)
print(list2)

list2.append(99) # changes the object in place. Does not create a new object.
print(list2)

print(list1) # list1 and list2 both are references to the same object and are both mutable


# In[29]:


# here is another example using .extend
list1 = [1,2,3]
list2 = list1
print(list1)
print(list2)

list2.extend([4,5,6]) # changes the object in place. Does not create a new object.
print(list2)

print(list1) # list1 and list2 both are references to the same object and are both mutable


# In[30]:


# here is another example using  + 
list1 = [1,2,3]
list2 = list1
print(list1)
print(list2)

list2 = list1 + [4,5,6] # this + operator creates a NEW object
print(list2)

print(list1) # list1 and list2 are references to different objects


# (membership-operators)=
# ## Membership Operators (`in`, `not in`)
# 
# We can use the operators `in` and `not in` to
# check if something is in a list or even in a string.
# It returns a boolean value `True` or `False`.

# In[31]:


print(my_list)


# In[32]:


-2 in my_list # the object -2 is not one of the items in my_list


# In[33]:


-2 not in my_list # the object -2 is not one of the items in my_list


# In[34]:


4 in my_list # the object 4 is not one of the items in my_list


# In[35]:


4 not in my_list # the object 4 is not one of the items in my_list


# In[36]:


'sunny day' in my_list # the object 'sunny day' is one of the items in my_list


# In[37]:


'sunny day' not in my_list # the object 'sunny day' is one of the items in my_list


# In[38]:


2.71 in my_list # the object 2.71 is one of the items in my_list


# In[39]:


2.71 not in my_list # the object 2.71 is one of the items in my_list


# In[40]:


name = 'chris'
if name in my_list:
    print(f'{name} is IN the list {my_list}')
else:
    print(f'{name} is NOT IN the list {my_list}')
    


# You can also use the `in` and `not in` operators with strings.

# In[41]:


s = 'chris is nice'
print(s)


# In[42]:


'chris' in s


# In[43]:


'Chris' in s # because of the capital C


# In[44]:


'is  ' not in s # because two spaces 


# In[45]:


'is is ni' in s


# (change-value-list)=
# ## Change Item Value in List
# We just saw how lists objects are **mutable**.
# This means you can change them or edit them
# after they are created. You can change the item
# in a list using indexing and assignment with the `=` 
# operator.

# In[46]:


print(my_list)


# In[47]:


print(my_list[1])


# In[48]:


my_list[1] = 5 # we are changing the item at index 1 to 5.


# In[49]:


print(my_list)


# In[50]:


my_list[-1] = 'chris'


# In[51]:


my_list


# In[52]:


my_list.append(5*6)
my_list


# In[53]:


new_list = [1,2,3]


# In[54]:


my_list.append(new_list) # you can append any object to the list my_list, even another list new_list!


# In[55]:


my_list


# In[56]:


my_list[-1]


# In[57]:


my_list[-1].append(4)


# In[58]:


my_list


# In[59]:


new_list # oh wow it changed! We will talk more about this later.


# In[60]:


[1, 2, 3, 4] in my_list


# There is a lot more to learn about lists but we will do so later.

# In[ ]:




