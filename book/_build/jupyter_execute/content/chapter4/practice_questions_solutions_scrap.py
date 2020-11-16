#!/usr/bin/env python
# coding: utf-8

# # Practice Questions (Solutions)

# ## 1.
# Write a function called `get_list_details` that takes a list `x` as its only argument.
# Then the function should print the list, print the sorted list, and return the list sorted.
# For example

# In[1]:


def get_list_details(x):
    print(f'The list is: {x}')
    x.sort()
    print(f'The list sorted is: {x}')
    return x


# In[2]:


get_list_details([10, -4, 5, 10, 78])


# In[3]:


def count_items(x):
    results = {}
    for i in x:
        results[i] = x.count(i)
    return results


# In[4]:


count_items([1,2,3,4,5])


# In[5]:


count_items([1,1,1])


# In[6]:


count_items([1,1,1,2,2,2,2,4])


# In[7]:


def remove_first_and_last(x):
    x.pop(0)
    x.pop()
    return x


# In[8]:


remove_first_and_last([1,2,3,4])


# In[9]:


remove_first_and_last([1, 2])


# In[10]:


remove_first_and_last([-10, 20, 50])


# In[11]:


x = [1, 2, 'hello world', -3, 5]


# In[12]:


x


# In[13]:


[y[1] for y in enumerate(x)]


# In[14]:


[x for i,x in enumerate([7, 5, 6, 9, 4, 5, 2]) if i % 3 == 0]


# In[15]:


instruments = ['guitar', 'drums', 'piano']
prices = [400, 500, 600]
colors = ['red', 'black', 'white']


# In[16]:


[(a,b,c) for a,b,c in zip(instruments, colors, prices)]


# In[17]:


payments = [('Chris', 3245.53), ('Joanna', 3498.43), ('Penny', 134.00), ('Isaac', 583.35),
('Chris', 4300.54), ('Joanna', 3498.43), ('Penny', 957.97), ('Isaac', 0.00),
('Henry', 10.10), ('Jen', 34.45), ('Matt', 0.00)]


# In[18]:


results = {name: 0 for name in [p[0] for p in payments]}
for name, paid in payments:
    results[name] = results[name] + paid


# In[19]:


results


# In[ ]:




