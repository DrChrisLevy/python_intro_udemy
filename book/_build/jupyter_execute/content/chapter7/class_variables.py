#!/usr/bin/env python
# coding: utf-8

# # Class Variables
# 
# In this section we will learn about class variables.
# We saw in the previous section that you can have multiple
# instances of a class. Each of the instances are objects
# which have their own properties or attributes specific 
# to that instance. Other times though we want attributes
# that are common to the class and shared by all the instances
# of the class. These are called class variables. Let's
# look at an example with a `TransitBus` class.
# 
# 

# In[1]:


class TransitBus:
    def __init__(self, identifier):
        self.identifier = identifier
        self.num_passengers=0
    
    def add_passengers(self, number):
        self.num_passengers += number
    
    def remove_passengers(self, number):
        self.num_passengers -= number 


# In[2]:


bus1 = TransitBus(1)
bus2 = TransitBus(2)
bus3 = TransitBus(3)

bus1.add_passengers(5)
bus2.add_passengers(4)
bus3.add_passengers(13)
bus2.remove_passengers(1)


# In[3]:


bus2.identifier


# In[4]:


bus2.num_passengers


# Above we created three instances of the `TransitBus` class. Each
# object is an instance of a bus. Each bus has it's own identifier 
# and has a certain number of passengers. All the buses can add
# and remove passengers with their `add_passengers` and `remove_passengers`
# methods.
# 
# What if we wanted to keep track of the total number of buses in the system
# as well as the total number of passengers? These would be properties specific
# to the `TransitBus` class in general. They are not specific to any particular instance
# or bus. Also, it would be nice if each bus had the ability to get this information.
# This can be achieved with **class variables**. They are variables that are shared
# across all instances of the class. Let's define two new class variables in the 
# `TransitBus` class, `total_num_passengers` and `total_num_buses`.

# In[5]:


class TransitBus:
    total_num_passengers = 0
    total_num_buses = 0
    
    def __init__(self, identifier):
        self.identifier = identifier
        self.num_passengers=0
    
    def add_passengers(self, number):
        self.num_passengers += number
    
    def remove_passengers(self, number):
        self.num_passengers -= number 


# The first thing to note is where in the code **class variables** are defined. They are defined
# outside the `__init__`. To access class variables you do not even need an instance of the class.

# In[6]:


TransitBus.total_num_buses


# In[7]:


TransitBus.total_num_passengers


# You can not do this with **instance variables** such as `identifier` and `num_passengers`.
# Using `TransitBus.identifier` or `TransitBus.num_passengers` would raise an `AttributeError`.
# This is because we need an instance (an actual bus) of the `TransitBus` first to access the instance variables `num_passengers` and `identifier`.
# 
# Let's create a new bus instance and see how that particular instance can access
# the class variables.

# In[8]:


print('bus1 info')
b1 = TransitBus(1)
b1.add_passengers(10)
b1.remove_passengers(3)
print(b1.identifier)
print(b1.num_passengers)

print('bus2 info')
b2 = TransitBus(2)
b2.add_passengers(20)
b2.remove_passengers(15)
print(b2.identifier)
print(b2.num_passengers)


# Each instance of a class has access to the class variables.

# In[9]:


b1.total_num_buses


# In[10]:


b1.total_num_passengers


# In[11]:


b2.total_num_buses


# In[12]:


b2.total_num_passengers


# We need to update the `TransitBus` logic so that 
# `TransitBus.total_num_buses` and `TransitBus.total_num_passengers`
# are updated each time a new bus is created and each time
# passengers get on or get off the bus. Notice that
# we use the `TransitBus` name to access the class variables.
# For example we used `TransitBus.total_num_buses`. You 
# can also simply use `self.total_num_buses`
# to access the class variables too. Sometimes it can be more
# clear to the reader or maintainer of the code
# to use the class name to reference the class variables.

# In[13]:


class TransitBus:
    total_num_passengers = 0
    total_num_buses = 0
    
    def __init__(self, identifier):
        self.identifier = identifier
        self.num_passengers=0
        TransitBus.total_num_buses += 1
    
    def add_passengers(self, number):
        self.num_passengers += number
        TransitBus.total_num_passengers += number
    
    def remove_passengers(self, number):
        self.num_passengers -= number
        TransitBus.total_num_passengers -= number


# In[ ]:





# In[14]:


print('bus1 info')
b1 = TransitBus(1)
b1.add_passengers(10)
b1.remove_passengers(3)
print(b1.identifier)
print(b1.num_passengers)

print('bus2 info')
b2 = TransitBus(2)
b2.add_passengers(20)
b2.remove_passengers(15)
print(b2.identifier)
print(b2.num_passengers)


# After running the above code there should be a total of 2 buses in the system
# as well as 12 total passengers.

# In[15]:


TransitBus.total_num_buses


# In[16]:


TransitBus.total_num_passengers


# **Class variables** have the same value across every instance of the class.

# In[17]:


print(b1.total_num_buses)
print(b1.total_num_passengers)
print(b2.total_num_buses)
print(b2.total_num_passengers)


# Let's create a new bus and see what happens to the totals.

# In[18]:


b3 = TransitBus(3)
b3.add_passengers(35)


# In[19]:


TransitBus.total_num_buses


# In[20]:


TransitBus.total_num_passengers


# In[21]:


print(b1.total_num_buses)
print(b1.total_num_passengers)
print(b2.total_num_buses)
print(b2.total_num_passengers)
print(b3.total_num_buses)
print(b3.total_num_passengers)


# ## Class Methods
# 
# Now what if we wanted to create a 100 buses in the system and keep track of them
# all in the system? It would not make much sense to create `bus1, bus2, ... bus100` variables.
# Instead, we could just create 100 instances of the `TransitBus` class and keep track of
# the different buses in a class variable. In this case we will keep track of each bus
# in the system within a dictionary. For example, if the transit system had three buses
# in the system this `transit_system` dict could look something like this:

# In[22]:


{'1': {'num_passengers': 5}, '2': {'num_passengers': 10}, '3': {'num_passengers': 20}}


# So it is a dictionary with the keys as the bus identifiers and the values
# with the information about the bus. Let's update the logic of the `TransitBus`
# class. We will add a **class method** called `update_bus_in_system`. A **class method**
# is a method that does need any particular instance of the class to be called.
# You use the `@classmethod` decorator and use `cls` instead of `self`. See the code below to see what is going on.

# In[23]:


class TransitBus:
    total_num_passengers = 0
    total_num_buses = 0
    transit_system = {}
    
    def __init__(self, identifier):
        self.identifier = identifier
        self.num_passengers=0
        TransitBus.total_num_buses += 1
        TransitBus.update_bus_in_system(self.identifier, 0)
    
    @classmethod
    def update_bus_in_system(cls, identifier, num_passengers):
        TransitBus.transit_system[identifier] = {'num_passengers': num_passengers}
    
    def add_passengers(self, number):
        self.num_passengers += number
        TransitBus.total_num_passengers += number
        TransitBus.update_bus_in_system(self.identifier, self.num_passengers)
    
    def remove_passengers(self, number):
        self.num_passengers -= number
        TransitBus.total_num_passengers -= number
        TransitBus.update_bus_in_system(self.identifier, self.num_passengers)


# In[24]:


TransitBus.total_num_buses


# In[25]:


TransitBus.total_num_passengers


# In[26]:


TransitBus.transit_system


# In[27]:


b1 = TransitBus(1)
b2 = TransitBus(2)
b3 = TransitBus(3)


# In[28]:


TransitBus.transit_system


# In[29]:


b1.add_passengers(10)
b2.add_passengers(20)
b3.add_passengers(30)


# In[30]:


TransitBus.transit_system


# In[31]:


b1.remove_passengers(5)
b2.remove_passengers(5)
b3.remove_passengers(5)


# In[32]:


TransitBus.transit_system


# In[33]:


print(b1.num_passengers)
print(b1.total_num_buses)
print(b1.total_num_passengers)


# And we can add another 100 buses to the system.

# In[34]:


import random
for i in range(4, 104):
    bus = TransitBus(identifier=i)
    bus.add_passengers(random.randint(0,35))


# In[35]:


TransitBus.total_num_buses


# In[36]:


TransitBus.total_num_passengers


# In[37]:


TransitBus.transit_system


# The only thing is now you can not access bus `103`, for example, and then add or remove passengers. You need an instance of the bus to do this. 
# 
# Although the `TransitSystem` class is another simple example, hopefully it gets you more familiar with the idea of using classes and also the difference between instance variables and methods and class variable and methods. Feel free to play around with the `TransitSystem` class some more on your own and improve it or add new functionality.
