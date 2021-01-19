#!/usr/bin/env python
# coding: utf-8

# # Class Inheritance
# 
# In this section we will go over an example of class inheritance.
# Class inheritance 
# is when you build classes that are derived from a general base class.
# There is a parent to child relationship where the child class (or subclass)
# retains a similar implementation to the base class (parent class). It's best understood
# through some examples.
# 
# First we will create a Dog and Cat class which are assumed to be pets.

# In[1]:


class Cat:
    def __init__(self, name, age, color, owner, likes_dogs):
        self.name=name
        self.age=age
        self.color=color
        self.owner=owner
        self.likes_dogs=likes_dogs
    
    def speak(self):
        print('meow')
    
    def eat(self):
        print('eat')
        
    def sleep(self):
        print('sleep')
        
class Dog:
    def __init__(self, name, age, color, owner, chases_cats):
        self.name=name
        self.age=age
        self.color=color
        self.owner=owner
        self.chases_cats = chases_cats
    
    def speak(self):
        print('woof')
    
    def eat(self):
        print('eat')
        
    def sleep(self):
        print('sleep')


# In[2]:


cat = Cat(name='Luna', age=4, color='brown', owner='Chris', likes_dogs=False)
dog = Dog(name='Max', age=2, color='white', owner='Isaac', chases_cats=True)
print(cat.name, cat.color, cat.owner, cat.age, cat.likes_dogs)
print(dog.name, dog.color, dog.owner, dog.age, dog.chases_cats)


# You can probably see that the code for the two classes `Cat` and `Dog` is
# very similar and there is a lot of repeated code. This in general is
# not good. If you wanted to change the way `eat` or `sleep` 
# works then you would have to change it in two different places.
# The only real difference is the `speak` method and some arguments in the constructor (`__init__`). Also if we
# wanted to create another animal/pet such as `Bird` we would have to copy
# out a lot of the same methods and attributes from either `Cat` or `Dog`. This
# would result in even more repeated code.
# 
# This is where the idea of class inheritance becomes useful. We can first
# create a base class called `Pet` with all the common attributes and methods
# for pets. There could be more methods and attributes for a `Pet` class
# and feel free to add them. I want to keep the example simple.
# 

# In[3]:


class Pet:
    def __init__(self, name, age, color, owner):
        self.name=name
        self.age=age
        self.color=color
        self.owner=owner
    
    def eat(self):
        print('eat')
        
    def sleep(self):
        print('sleep')


# Then we can subclass this class to create the `Dog` and `Cat` classes.

# In[4]:


class Cat(Pet):
    def __init__(self, name, age, color, owner, likes_dogs):
        super().__init__(name, age, color, owner)
        self.likes_dogs = likes_dogs
    
    def speak(self):
        print('meow')

class Dog(Pet):
    def __init__(self, name, age, color, owner, chases_cats):
        super().__init__(name, age, color, owner)
        self.chases_cats = chases_cats
    
    def speak(self):
        print('woof')


# In[5]:


cat = Cat(name='Luna', age=4, color='brown', owner='Chris', likes_dogs=False)
dog = Dog(name='Max', age=2, color='white', owner='Isaac', chases_cats=True)
print(cat.name, cat.color, cat.owner, cat.age, cat.likes_dogs)
print(dog.name, dog.color, dog.owner, dog.age, dog.chases_cats)


# The main difference is instead of writing `class Dog` you write `class Dog(Pet)` which means
# `Dog` will inherit from the base class `Pet`. Also in the `__init__` (aka constructor)
# you have to call the `super().__init__` method which simply means to call the constructor of the parent class. Then you can add any additional logic to the child class constructor that is required.
# 
# We can even make the code more concise. Notice that we had to repeat all the `Pet` class initialization arguments. We can use `**kwargs` to shorten this up.

# In[6]:


class Cat(Pet):
    def __init__(self, likes_dogs, **kwargs):
        super().__init__(**kwargs)
        self.likes_dogs = likes_dogs
    
    def speak(self):
        print('meow')

class Dog(Pet):
    def __init__(self, chases_cats, **kwargs):
        super().__init__(**kwargs)
        self.chases_cats = chases_cats
    
    def speak(self):
        print('woof')


# In[7]:


cat = Cat(name='Luna', age=4, color='brown', owner='Chris', likes_dogs=False)
dog = Dog(name='Max', age=2, color='white', owner='Isaac', chases_cats=True)
print(cat.name, cat.color, cat.owner, cat.age, cat.likes_dogs)
print(dog.name, dog.color, dog.owner, dog.age, dog.chases_cats)


# We can even add more methods or attributes that are common to only one of the child classes. For example, suppose dogs like to swim and cats do not. Then we can add a swim method to the dog class.

# In[8]:


class Dog(Pet):
    def __init__(self, chases_cats, **kwargs):
        super().__init__(**kwargs)
        self.chases_cats = chases_cats
    
    def speak(self):
        print('woof')
    
    def swim(self):
        print('swim')


# In[9]:


dog = Dog(name='Max', age=2, color='white', owner='Isaac', chases_cats=True)
dog.eat()
dog.sleep()
dog.swim()


# In summary, the child class will have all the same methods and attributes 
# as the parent class as well as the new ones you define in the child class.
# 
# Another thing you can do is override the method from the parent class. For example,
# we have the method `sleep` from the parent class which simply prints `sleep`. We can
# change this implementation for the `Dog` class for example.

# In[10]:


class Dog(Pet):
    def __init__(self, chases_cats, **kwargs):
        super().__init__(**kwargs)
        self.chases_cats = chases_cats
    
    def speak(self):
        print('woof')
    
    def swim(self):
        print('swim')
        
    def sleep(self, hours):
        print(f'sleeping for {hours} hours.')


# In[11]:


cat = Cat(name='Luna', age=4, color='brown', owner='Chris', likes_dogs=False)
dog = Dog(name='Max', age=2, color='white', owner='Isaac', chases_cats=True)
print(cat.name, cat.color, cat.owner, cat.age, cat.likes_dogs)
print(dog.name, dog.color, dog.owner, dog.age, dog.chases_cats)


# In[12]:


cat.sleep()
cat.eat()


# In[13]:


dog.eat()
dog.swim()
dog.sleep(2)


# I hope you now understand a little bit about class inheritance in Python now. 
# 
# There is more
# that could be said and there are entire courses/books which only focus on object-oriented programming (OOP). Just remember that classes are a great way to organize code into similar functions and methods that work together. Classes are templates for how objects should behave. All the functionality and data related to similar objects can be defined in the class. The best way to learn is to write your own simple programs which use classes and also spend time reading other peoples code.
