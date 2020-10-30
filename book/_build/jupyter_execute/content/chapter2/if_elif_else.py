#!/usr/bin/env python
# coding: utf-8

# (if-elif-else)=
# # `if`, `elif`, and `else` statements
# 
# In this section we will learn about `if`, `elif`, and `else` statements in Python.
# This is where things start to get interesting because now we will have
# the ability to use more complex logic and decision making in our
# Python code examples and programs.
# 
# Create a new Jupyter Notebook called **if_elif_else_statements**. Follow along
# and write the code! You are encouraged to tinker with the code, change it, and even
# break it! It's the only way to learn!
# 
# ## `if` statement
# 
# The syntax in general for the `if` statement is:
# 
# ```
# if condition:
#     statements_to_execute
# ```
# 
# The `condition` is any valid python expression that evaluates to `True` or `False`. 
# If the `condition` evaluates to `True`, then the statements in the `statements_to_execute` 
# are executed. Otherwise the `statements_to_execute` are skipped all together. Notice also the use of the 
# colon `:` after the `condition`.
# 
# This is the first time we are seeing the use of white space and *indentation*.
# The use of white space and indentation is very important in Python. 
# An indented white space (tab on keyboard) is used to start a block of code or statements
# and any code that is indented at that level is executed together as a *block of code*.
# 
# To start practicing with `if`, `elif`, and `else` statements,
# we will use the example of a student receiving a final grade
# and determining if they pass or not. The logic will begin
# very simple but then we continue to add to it.
# To start, suppose a grade of 50% is a passing grade.
# So if a student gets less than 50% they fail
# and if they get over 50% or over they pass.
# 
# This is what we want the Python code to do in our first example.
# If the final grade is greater than or equal to 50, the code
# will print a message with their grade and the fact that they passed.
# We will also print a good bye message at the end.
# Here is what that would look like using the `if` statement.

# In[1]:


final_grade = 60
if final_grade >= 50:
    print(f'Your final grade was {final_grade} so you passed!')
    
print('Good Bye, see you next year.')


# Since the expression `final_grade >= 50` is `True`, the **indented statement block** (the line with the print)
# is executed. The alternative would be if
# `final_grade >= 50` is `False`. In that case the **indented statement block**
# would be skipped all together and not executed. Here is an example where `final_grade` is less than 50
# so the indented statement block is skipped and it goes straight to the good bye message.

# In[2]:


final_grade = 49
if final_grade >= 50:
    print(f'Your final grade was {final_grade} so you passed!')
    
print('Good Bye, see you next year.')


# Before continuing to the next example, play around with the above example.
# Try changing the `final_grade` to different values and seeing 
# when the `if` block of code gets executed.

# ## `else` statement
# 
# In the previous example we saw that if the condition (`final_grade >= 50`) was
# `True` then the next indented code block was executed. If the conditon was `False`
# then it was skipped. There are times when we want to
# execute some alternative logic when the `condition` is `False`.
# This is what the `else` statement is for. The general syntax is:
# 
# ```
# if condition:
#     # executed if condition is True
#     statements_to_execute 
# else:
#     # executed if condition is False
#     alternative_statements_to_execute 
# ```
# 
# Lets add to our example by using the `else` statement.
# Now, if the student has a failing grade (less than 50) than
# it prints a message saying the student failed.

# In[3]:


final_grade = 49
if final_grade >= 50:
    print(f'Your final grade was {final_grade} so you passed!')
else:
    print(f'Your final grade was {final_grade}. You failed. Try harder next time.')    
    
print('Good Bye, see you next year.')


# So just to say it one more time. If the `condition` is `True` then the first indented
# block of statements is executed. Otherwise, the statements indented after the `else`
# statement are executed. Never will it be the case that both blocks are executed. It's one or the other only.
# Check it out in the above example by changing the `final_grade` to 50 or greater.

# ## `elif` statements
# 
# The `elif` statement is short for **else if**. It is used when we want to check for multiple conditions.
# If the first condition for `if` is `False`, then next condition for the `elif` block will be checked.
# If the `elif` condition is `True` than the indented statements for that `elif` block are executed.
# If the `elif` condition if `False` than the code in the `else` block is executed. 
# There can be multiple `elif` statements. Among the `if` statements, `elif` statements, 
# and `else` statements, only one block of statements will be executed. 
# The `if` block can have only one `else` block but can have multiple `elif` blocks.
# The general syntax is:
# 
# ```
# if first_condition:
#     # executed if first_condition is True
#     first_statements_to_execute 
# elif second_condition:
#     # executed if first_condition is False and second_condition is True
#     second_statements_to_execute 
# elif third_condition:
#     # executed if first_condition is False and second_condition is False and third_condition is True
#     third_statements_to_execute 
# .
# .
# .
# else:
#     alternative_statements_to_execute # executed if all conditions above are False
# ```
# 
# It's really important to remember that only one of the indented block
# statements will get executed (not multiple blocks). It all depends on what
# `condition` is `True`. If all the conditions are `False` than the `else`
# block gets executed.
# 
# Let's evolve our example with displaying the students grade.
# Now we will display a slightly different message based on the students `final_grade`.

# In[4]:


final_grade = 90
if final_grade >= 90:
    print(f'Your final grade was {final_grade}. You did amazing work! You passed!')
elif final_grade >= 80:
    print(f'Your final grade was {final_grade}. You did really good work! You passed!')
elif final_grade >= 70:
    print(f'Your final grade was {final_grade}. You did good work! You passed!')
elif final_grade >= 50:
    print(f'Your final grade was {final_grade}. You did okay work. You passed.')
else:
    print(f'Your final grade was {final_grade}. You failed. Try harder next time.')    
   
    
print('Good Bye, see you next year.')


# In the above example we added multiple `elif` statements to show how they work.
# Take some time to play around with the code by changing the `final_grade` to different values such as
# `95`, `90`, `80`, `75`, `70`, `50`, and `45`. Execute the code for these different values
# and take note of what print statement gets executed.
# 
# In closing, when using `if`, `elif`, and `else` statements, you always start with an `if` statement.
# Both the `elif` and `else` statements are optional. There can be multiple `elif` statements and only
# one `else`. Remember to use the colon `:` after each condition as well as the indented white space.
# 
# Here are a few simple examples that you can play around with.
# 
# ## Example 1: `if`

# In[5]:


x = 'HELLO' # change to 'hello' to make the print statement execute
if x == 'hello':
    print('hello world')


# ## Example 2: `if`  `else`

# In[6]:


x = 6 # change to different values to see what blocks below get executed.
if x + 5 > 10:
    print(f'{x+5} is strictly larger than 10.')
else:
    print(f'{x+5} is not strictly larger than 10.')


# ## Example 3: `if` `elif` `else`

# In[7]:


x = 0.1 # change to different values to see what blocks below get executed.
if x > 0:
    print(f'{x} is positive.')
elif x < 0:
    print(f'{x} is negative.')
else:
    print(f'{x} is zero.')


# ## Example 4: multiple `True` conditions
# Remember that even if multiple conditions are `True`, only
# one of the blocks will be executed (the first condition for which it is `True`).

# In[8]:


x = 101
if x >= 100:
    print(f'{x} is big.')
elif x > 0:
    print(f'{x} is positive.')
elif x < 0:
    print(f'{x} is negative.')
else:
    print(f'{x} is zero')


# ## Example 5: `else` is optional
# Remember that `elif` and `else` are optional.

# In[9]:


x = 0
if x >= 100:
    print(f'{x} is big.')
elif x > 0:
    print(f'{x} is positive.')
elif x < 0:
    print(f'{x} is negative.')
    


# ## Example 6: 
# 
# Here we will look at another example to practice
# with the `if`, `elif`, and `else` statements. Suppose an employee 
# has to work on Monday, Wednesday, and Friday and has to wear
# a different color uniform on each of those days. Red on Monday,
# blue on Wednesday, and green on Friday. Also suppose they have to remember
# to bring lunch on Monday and Wednesday but not on Fridays. We will write a simple
# program that prints what color to wear and if the employee needs to bring
# food, based on the day of the week.

# In[10]:


day = 'Friday' # can change to any day of the week. Capitalize only the first letter. 

if day == 'Monday':
    print('You need to wear red today.')
    print('You also need to bring food.')
elif day == 'Wednesday':
    print('You need to wear blue today.')
    print('You also need to bring food.')
elif day == 'Friday':
    print('You need to wear green today.')
    print('You do not need to bring food.')
else:
    print('You do not work today. Have a good day off.')    


# Try changing the `day` to different days of the week
# and executing the above code to see how it all works.

# ## Nested `if` statements
# 
# When you are working with indented code blocks, you can write any valid
# Python code within those indented code blocks. This means for example that
# you can *nest* `if`, `elif`, and `else` statements within one another.
# When you have an `if` statement inside 
# another `if` statement and so on, this is called *nesting*.
# Here is a simple example.

# In[11]:


x = 15 # run the code with x as 15, 7, 4, and -2 to see the different blocks executed
if x > 5:
    print(f'{x} is larger than 5')
    if x > 10:
        print('and is also larger than 10')
    else:
        print('but is not larger than 10')
else:
    print(f'{x} is smaller than 5')
    if x < 0:
        print('and is also negative')
        
    


# Before going onto the next section spend some time
# playing around with `if`, `elif`, and `else` statements.
# Keep it simple and try to get the syntax down and memorized.
