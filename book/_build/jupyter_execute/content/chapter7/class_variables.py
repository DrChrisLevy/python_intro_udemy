#!/usr/bin/env python
# coding: utf-8

# # Class Variables and Methods
# 
# In this section we will learn about class variables and class methods.
# We saw in the previous section that you can have multiple
# instances of a class. Each of the instances are objects
# which have their own properties or attributes specific 
# to that instance. Other times though we want attributes
# that are common to the class and shared by all the instances
# of the class. These are called class variables and class methods. Let's
# look at an example with a `TransitBus` class to learn these concepts.
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


# Now what if we wanted to create a 100 buses in the system and keep track of them
# all in the system? It would not make much sense to create `bus1, bus2, ... bus100` variables.
# Instead, we could just create 100 instances of the `TransitBus` class and keep track of
# the different buses in a class variable. In this case we will keep track of each bus
# in the system within a dictionary. For example, if the transit system had three buses
# in the system this `transit_system` dictionary could look something like this:

# In[22]:


{'1': {'num_passengers': 5}, '2': {'num_passengers': 10}, '3': {'num_passengers': 20}}


# So it is a dictionary with the keys as the bus identifiers and the values
# with the information about the bus. Let's update the logic of the `TransitBus`
# class by adding this new class variable `transit_system`.

# In[23]:


class TransitBus:
    total_num_passengers = 0
    total_num_buses = 0
    transit_system = {}
    
    def __init__(self, identifier):
        self.identifier = identifier
        self.num_passengers=0
        TransitBus.total_num_buses += 1
        self.update_bus_in_system()
    
    def update_bus_in_system(self):
        TransitBus.transit_system[self.identifier] = {'num_passengers': self.num_passengers}
    
    def add_passengers(self, number):
        self.num_passengers += number
        TransitBus.total_num_passengers += number
        self.update_bus_in_system()
    
    def remove_passengers(self, number):
        self.num_passengers -= number
        TransitBus.total_num_passengers -= number
        self.update_bus_in_system()


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


# ## Class Methods
# We will add a **class method** called `transit_stats`. A **class method**
# is a method that does need any particular instance of the class to be called.
# You use the `@classmethod` decorator and use `cls` instead of `self`. See the code below to see what is going on. We will also add a `reset_system` class method which removes
# all the buses from the system.

# In[34]:


class TransitBus:
    total_num_passengers = 0
    total_num_buses = 0
    transit_system = {}
    
    def __init__(self, identifier):
        self.identifier = identifier
        self.num_passengers=0
        TransitBus.total_num_buses += 1
        self.update_bus_in_system()
    
    def update_bus_in_system(self):
        TransitBus.transit_system[self.identifier] = {'num_passengers': self.num_passengers}
    
    def add_passengers(self, number):
        self.num_passengers += number
        TransitBus.total_num_passengers += number
        self.update_bus_in_system()
    
    def remove_passengers(self, number):
        self.num_passengers -= number
        TransitBus.total_num_passengers -= number
        self.update_bus_in_system()
    
    @classmethod
    def transit_stats(cls):
        avg_person_per_bus = cls.total_num_passengers / cls.total_num_buses
        num_empty_buses = len([v for (k,v) in cls.transit_system.items() if not v['num_passengers']])
        return {'total_num_passengers': cls.total_num_passengers,
               'total_num_buses': cls.total_num_buses,
               'num_empty_buses': num_empty_buses,
               'avg_person_per_bus': avg_person_per_bus}
    
    @classmethod
    def reset_system(cls):
        cls.total_num_passengers = 0
        cls.total_num_buses = 0
        cls.transit_system = {}
        
    


# Lets create 2000 buses in the system where each bus has a random number of
# people between 0 and 45. Then we will remove a random
# number of passengers. First we will reset the transit system.

# In[35]:


TransitBus.reset_system()


# In[36]:


import random
for i in range(1, 2001):
    bus = TransitBus(identifier=i)
    bus.add_passengers(random.randint(0,45))
    bus.remove_passengers(random.randint(0, bus.num_passengers))


# Here are the first 10 buses in the system.

# In[37]:


[(k,v) for k,v in TransitBus.transit_system.items() if k in range(1,11)]


# And now we can get the transit stats.

# In[38]:


TransitBus.transit_stats()


# Although the `TransitBus` class is another simple example, hopefully it gets you more familiar with the idea of using classes and also the difference between instance variables and methods and class variable and methods. Feel free to play around with the `TransitBus` class some more on your own and improve it or add new functionality.
