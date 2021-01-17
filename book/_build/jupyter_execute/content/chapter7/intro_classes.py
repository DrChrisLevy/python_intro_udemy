#!/usr/bin/env python
# coding: utf-8

# # Intro to Classes
# 
# A class is like a blueprint or template for an object. 
# Once the class is defined you can create instances
# which are single objects in memory that have
# various data, attributes, and methods which were defined
# for the class. 
# 
# In our first example we will create a `Person` class.
# Think of the `Person` class as being a template which
# gives structure around the details you could store
# or compute about a person in general. For example,
# any one individual person would have an age, height,
# birth date, phone number, email, to name a few things

# ## Defining Classes

# In[1]:


class Person:
    def __init__(self, first_name, last_name, height, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.birth_date = birth_date


# To define a class you start with the `class` keyword followed by the name
# of the class and a colon. Within the class you can define variables and functions
# which are attributes of the class. The `__init__` method is a special method known as
# the constructor. It gets executed once each time you create a new instance of a class.
# 
# The keyword `self` is a special keyword used to represent the instance of the class.
# In general, it gets passed as the first argument to all the methods defined in the class. It can be used
# throughout the class code to refer to any of the classes attributes. Let's create an instance of the `Person` class. When using the class, the `self` keyword argument always gets passed
# implicitly and you do not need to use it explicitly.

# In[2]:


p1 = Person(first_name='Chris', last_name='Levy', height=6, birth_date=1985)


# In[3]:


p1


# In[4]:


type(p1)


# Now we have an instance of the `Person` class, `p1`, created in memory. We can access
# the attributes of the instance, `p1`, with the `.` operator.

# In[5]:


p1.birth_date


# In[6]:


p1.first_name


# In[7]:


p1.last_name


# In[8]:


p1.birth_date


# Now let's create a second person.

# In[9]:


p2 = Person(first_name='Joanna', last_name='Levy', height=5.5, birth_date=1983)


# In[10]:


p2.first_name


# The data for such a simple class could of been stored in a dictionary or some
# other Python object. However, classes provide much more flexibility. For example, we can
# define functions within the class. These functions of the class 
# are called methods of the class and are available as attributes of the instances of the class.
# For example, suppose we wanted a function to get the age of the person. We can modify the 
# `Parent` class like so:

# In[11]:


import datetime
class Person:
    def __init__(self, first_name, last_name, height, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.birth_date = birth_date
    
    def age(self):
        todays_date = datetime.date.today()
        return todays_date.year - self.birth_date
        


# Notice that the function `age` has the first argument `self`. If you need to
# refer to any of the instance attributes within the function then you can do so
# with `self` keyword. It is always the first argument. The keyword `self` is not passed
# as an explicit argument when you go and use the `age` method of the instance. The functions defined in the class are referred to as methods of the instance that is created from the class.

# In[12]:


p1 = Person(first_name='Chris', last_name='Levy', height=6, birth_date=1985)


# In[13]:


p1.age()


# In[14]:


p2 = Person(first_name='Joanna', last_name='Levy', height=5.7, birth_date=1983)


# In[15]:


p2.age()


# In[16]:


print(f'{p1.first_name} {p1.last_name} is {p1.height} feet tall and is {p1.age()} years old.')


# In[17]:


print(f'{p2.first_name} {p2.last_name} is {p2.height} feet tall and is {p2.age()} years old.')


# If for example we found the above print statement useful, we could just create it as a method within the class.

# In[18]:


import datetime

class Person:
    def __init__(self, first_name, last_name, height, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.birth_date = birth_date
    
    def age(self):
        todays_date = datetime.date.today()
        return todays_date.year - self.birth_date
    
    def print_details(self):
        age = self.age()
        print(f'{self.first_name} {self.last_name} is {self.height} feet tall '
              f'and is {self.age()} years old.')


# In[19]:


p1 = Person(first_name='Chris', last_name='Levy', height=6, birth_date=1985)
p2 = Person(first_name='Joanna', last_name='Levy', height=5.7, birth_date=1983)
p1.print_details()
p2.print_details()


# ## Changing Class Instance Attributes
# The instances of the class you create are mutable
# in that you can modify basically anything about the object
# after it is created.
# 

# In[20]:


p1.first_name
p1.last_name


# Here we modify the name, height, and the birth date of the `p1` object. Then whenever 
# `self` is used within the function definitions in the class it uses
# the updated object values for the instance.

# In[21]:


p1.first_name = 'Isaac'
p1.last_name = 'Levy'
p1.birth_date = 2011
p1.height = 4.5


# In[22]:


p1.age()


# In[23]:


p1.print_details()


# ## Bank Account Example
# 
# Let's look at another example of creating a class.
# This class will be called `BankAccount` and will be responsible
# for storing and keeping up to date the details of a persons
# bank account. It will keep track of the amount of
# money in the account, a history of previous transactions,
# and will be able to perform new transactions such as withdrawals 
# and deposits.
# 
# The first step is to choose the name of the class. When naming
# classes in Python it's common to use the `CamelCase` format which just means
# to capitalize the first letter at the beginning of each new word.
# We will use the name `BankAccount` for our class.
# 
# The very minimum code needed to create a class is the following.

# In[24]:


class BankAccount:
    pass


# In[25]:


account = BankAccount()


# This instance of the class, `account` has no data or methods associated with it
# because we have not defined anything within the class `BankAccount`. 
# 
# When we create a bank account it needs to have an initial state which gets computed
# once the instance object of the class is created. This is what the `__init__` method is 
# for. We will pass the name of the person who will own the account as an argument to the 
# constructor method (i.e. the `__init__` method). In the constructor we will also
# set the balance of the account to $0 and the transaction history to an empty list.
# We store the `balance` and the `transaction_history` in `__init__` with `self`. This way
# those values become attributes of the class and we can keep track of them.

# In[26]:


class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transaction_history = []


# In[27]:


account = BankAccount('Chris Levy')
print(account.name, account.balance, account.transaction_history)


# After someone creates an account, they probably want to be able to put some money in. These are called deposits. We will create a `deposit` function which takes the amount of money to deposit and updates `self.balance`. The function does not need to return anything because
# it's simply updating the internal `self.balance`.

# In[28]:


class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transaction_history = []
    
    def deposit(self, amount):
        self.balance = self.balance + amount


# In[29]:


account = BankAccount('Chris Levy')
print(account.name, account.balance, account.transaction_history)


# In[30]:


account.deposit(100)
print(account.name, account.balance, account.transaction_history)


# In[31]:


account.deposit(30)
print(account.name, account.balance, account.transaction_history)


# In[32]:


account.deposit(22)
print(account.name, account.balance, account.transaction_history)


# Above are some examples of deposit transactions which update
# the `balance` associated with the instance of the class. If we create another bank
# account instance it will have it's own data.

# In[33]:


account2 = BankAccount('Isaac')


# In[34]:


account2.deposit(10)


# In[35]:


print(account.name, account.balance, account.transaction_history)


# In[36]:


print(account2.name, account2.balance, account2.transaction_history)


# We want to keep track of every historical transaction for both deposits
# and withdrawals. We need to modify the `deposit` method so that it
# adds the details of the deposit transaction to the history. We will add
# an optional `details` argument. As well, we will store each transaction
# as a dictionary. This way we can add more fields later if we need to. The 
# transactions need to be appended to the list `transaction_history`. It
# also makes sense to add the date and time of the transaction so we will
# use the `datetime` library to do that.

# In[37]:


from datetime import datetime

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transaction_history = []
    
    def deposit(self, amount, details=None):
        self.balance = self.balance + amount
        now = datetime.now()
        transaction = {
            'amount': amount,
            'type': 'deposit',
            'details': details,
            'date': now.strftime("%Y/%m/%d/ %H:%M:%S") # format date as string
        }
        self.transaction_history.append(transaction)


# In[38]:


account = BankAccount('Chris')


# In[39]:


print(account.name, account.balance, account.transaction_history)


# In[40]:


account.deposit(10000, 'Setting up my account.')


# In[41]:


account.balance


# In[42]:


account.transaction_history


# In[43]:


account.deposit(100, 'money I got as a gift.')


# In[44]:


account.balance


# In[45]:


account.transaction_history


# In[46]:


account.deposit(3000)


# In[47]:


account.balance


# In[48]:


account.transaction_history


# Okay, so now we need to create a function for handling withdrawals (taking money
# out of the account). We can create a `withdrawal` method which behaves just like
# the `deposit` method. The only difference is that it should decrease the balance
# and it is typical to store such values as negative.

# In[49]:


from datetime import datetime

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transaction_history = []
    
    def deposit(self, amount, details=None):
        self.balance = self.balance + amount
        now = datetime.now()
        transaction = {
            'amount': amount,
            'type': 'deposit',
            'details': details,
            'date': now.strftime("%Y/%m/%d/ %H:%M:%S") # format date as string
        }
        self.transaction_history.append(transaction)
        
    def withdrawal(self, amount, details=None):
        self.balance = self.balance - amount
        now = datetime.now()
        transaction = {
            'amount': -1 * amount,
            'type': 'withdrawal',
            'details': details,
            'date': now.strftime("%Y/%m/%d/ %H:%M:%S") # format date as string
        }
        self.transaction_history.append(transaction)


# In[50]:


account = BankAccount('Chris')
account.deposit(100, 'setup')
account.deposit(100, 'paid')
account.withdrawal(50, 'food')
account.balance


# In[51]:


account.transaction_history


# The dates are the same because the code got executed together 
# close together in time. Notice that the amount for withdrawals is negative.
# 
# Now there is one more thing we need to handle for withdrawals. What if
# someone tries to withdraw money or make a purchase but there is not
# enough money in the account? Then we need to stop the transaction from
# completing and print a message that says insufficient funds. Let's
# update the `withdrawal` method to handle this logic.

# In[52]:


from datetime import datetime

class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transaction_history = []
    
    def deposit(self, amount, details=None):
        self.balance = self.balance + amount
        now = datetime.now()
        transaction = {
            'amount': amount,
            'type': 'deposit',
            'details': details,
            'date': now.strftime("%Y/%m/%d/ %H:%M:%S") # format date as string
        }
        self.transaction_history.append(transaction)
        
    def withdrawal(self, amount, details=None):
        new_balance = self.balance - amount
        if new_balance < 0:
            print(f'Sorry! You only have ${self.balance} in your account.')
            print(f'You can not complete this transaction of ${amount} at this time.')
            
            # will return None and function will exit.
            # No logic after the return will be executed
            return  
        
        self.balance = new_balance
        now = datetime.now()
        transaction = {
            'amount': -1 * amount,
            'type': 'withdrawal',
            'details': details,
            'date': now.strftime("%Y/%m/%d/ %H:%M:%S") # format date as string
        }
        self.transaction_history.append(transaction)


# In[53]:


account = BankAccount('Chris')


# In[54]:


account.deposit(100)
account.deposit(200)
account.deposit(300)


# In[55]:


account.balance


# In[56]:


account.withdrawal(400)


# In[57]:


account.balance


# In[58]:


account.withdrawal(10)


# In[59]:


account.balance


# In[60]:


account.withdrawal(201)


# In[61]:


account.transaction_history


# The class `BankAccount` we created is quite simple. But I hope you start
# to see why classes are so powerful. It gives you the ability
# to create new objects which can have their own attributes and data
# together in a single place. Most application code in the "real world"
# will be written using the Object-oriented programming (OOP) paradigm which
# is based on using classes. We will not be teaching everything there is to know
# about OOP in this course.
# However, we will go cover some of the basics about working with classes in Python
# so you can get started.
