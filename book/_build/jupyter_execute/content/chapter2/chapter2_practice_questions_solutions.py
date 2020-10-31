#!/usr/bin/env python
# coding: utf-8

# # Practice Questions (Solutions)
# There is so much new stuff we learned this past chapter.
# We introduced you to boolean data types, comparison operators,
# logical operators, `if`, `elif`, and `else` statements,
# lists, as well as `for` and `while` loops. There is actually
# more we could say about all of these things. But now is a good time
# to get coding. The best way to learn is by doing. Moreover, it is good
# to work on problems which mix all these ideas and tools together. It is going to be
# hard at first! It takes practice. But as you start solving small problems,
# you will learn and become more confident. As you spend more time coding,
# you will learn tricks and things that you can apply to other problems.

# ## 1. 
# 
# Ask the user to enter a number using the `input` function. If the number is even
# then print a message that displays the number and that it is even. If the number is not
# even then change the message to say that the number is odd. For example, if the user enters
# a 10 the message might read `'The number 10 is even'`. If the user enters an odd number such as 13, then
# the message might read `'The number 13 is odd'`.
# 
# ### SOLUTION
#     

# ```
# number = int(input('Please enter a number: '))
# if number % 2 == 0:
#     print(f'The number {number} is even!')
# else:
#     print(f'The number {number} is odd!')
# ```

# ## 2. 
# 
# Suppose you are given a list `nums = [6, 7, 7, 10, 12, 1, 3, 3, 5, 5, 7, 8, 9, 12, 20]`. Write code
# that prints all the numbers that are strictly greater than `5` and strictly less than `9`, one line at a time. The code should work for any list (not just this example list). For example the output should look like this:
# ```
# 6
# 7
# 7
# 7
# 8
# ```
# If the list was for example  `nums = [1,2,6,20]`  the output would be
# ```
# 6
# ```
# If the list was `nums = [1,2,5,20]` then nothing would be printed.
# 
# 
# ### SOLUTION

# In[1]:


nums = [6, 7, 7, 10, 12, 1, 3, 3, 5, 5, 7, 8, 9, 12, 20]
for x in nums:
    if x > 5 and x < 9:
        print(x)


# ## 3. 
# 
# Repeat question number 2 by adding in this difference. Instead of printing the numbers one by one, make a new list that has all the numbers strictly greater than `5` and strictly less than `9` from the original list. Then just print the new list.
# 
# ### SOLUTION

# In[2]:


nums = [6, 7, 7, 10, 12, 1, 3, 3, 5, 5, 7, 8, 9, 12, 20]
numbers = []
for x in nums:
    if x > 5 and x < 9:
        numbers.append(x)
print(numbers)


# ## 4.
# 
# Write code that takes the list `colors = ['green','red','orange','blue','yellow']`
# and prints the first item and the last item in the list. No `for` loop is needed here (just list indexing).
# 
# ### SOLUTION

# In[3]:


colors = ['green','red','orange','blue','yellow']
print(colors[0])
print(colors[-1])


# ## 5.
# 
# Write a program that prints the numbers from 1 to 100. 
# 
# ### SOLUTION

# In[4]:


for i in range(1,101):
    print(i)


# In[5]:


# or we could do this
numbers = []
for i in range(1,101):
    numbers.append(i)
print(numbers)


# In[6]:


# list comprehension - will learn this in the future part of the course
# just showing here because it's a cool solution in just one line
print([i for i in range(1,101)])


# ## 6.
# 
# Write a program that prints the numbers from 1 to 100 but with these modifications. If the number is a multiple of 3 print **Fizz** instead of the number. If the number is a multiple of 5 then print **Buzz**. However, if the number is both a multiple of 3 and a multiple of 5 print **FizzBuzz**. The output should look something like this:
# 
# ```
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# FizzBuzz
# .
# .
# .
# .
# 91
# 92
# Fizz
# 94
# Buzz
# Fizz
# 97
# 98
# Fizz
# Buzz
# ```
# 
# ### SOLUTION
# 
# 
# 

# In[7]:


for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


# ## 7.
# Suppose you have two lists `a` and `b` which may not be the same length.
# Write code which will find the items that are common between both `a`
# and `b` and puts them in a new list `c`. Also make sure that `c` does not have
# the same item more than once (no duplicates). So the list `c` will be a unique
# list of only the items that were in both `a` and `b`. The items you put in `c`
# can be in any order.
# 
# For example,
# 
# ```
# a = [1,2,3,3,5,5,10]
# b = [9,8,5,9,5]
# # then c would be
# [5]
# ```
# 
# ```
# a = ['carrot', 'orange']
# b = ['orange','chris',9,]
# # then c would be
# ['orange']
# ```
# 
# 
# ```
# a = [1,2,3,4,5,7]
# b = [1,2,10]
# # then c would be
# [1,2]
# ```
# 
# ```
# a = [1,2,3,10]
# b = [4,5,6,-6]
# # then c would be
# []
# ```
# 
# ### SOLUTION
# 
# 

# In[8]:


a = [1,2,3,3,5,5,10]
b = [9,8,5,9,5]
c = []
for x in a:
    if x in b and x not in c:
        c.append(x)
print(c)


# ## 8.
# Write a program that iterates/loops over a list of numbers
# and print how many `0`'s are in the list.
# For example if the list was `[1,2,0,10,0]`
# then it would print `2` because there are two `0`'s in the list.
# 
# ### SOLUTION
# 

# In[9]:


list_of_numbers = [1,2,0,10,0]
count = 0
for number in list_of_numbers:
    if number == 0:
        count = count + 1 # count += 1
print(count)


# ## 9.
# Suppose you have two lists of the same length and that there are only numbers in both the lists.
# For example,
# 
# `x = [33, 49, 101, 9]`
# 
# `y = [10, 12, 20, 1000]`
# 
# Write a program that will multiply the numbers from list `x` by the numbers in list `y` element
# wise and then sum the results. In other words, the program should compute
# 
# $$33*10 + 49*12 + 101*20 + 9*1000 = 11938.$$
# 
# The code should work for any lists with numbers that are the same length. Another example would be
# 
# `x = [1, 2, 3, 4]`
# 
# `y = [5, 6, 7, 8]`
# 
# which would lead to
# 
# $$1*5 + 2*6 + 3*7 + 4*8 = 70.$$
# 
# 
# ### Solution

# In[10]:


x = [33, 49, 101, 9]
y = [10, 12, 20, 1000]
result = 0
for i in range(len(x)):
    result += x[i] * y[i] # or simply --->    result = result + x[i] * y[i] 
print(result)


# ## 10.
# 
# Write some code which gets a string from user input.
# Then print something to the screen saying whether the string
# they entered is a palindrome or not. Palindromes are words which are spelled
# the same way frontwards and backwards such as `racecar`, `level`, `rotator` and so on.
# 
# 
# ### SOLUTION
# ```
# word = input('Please enter a word: ')
# if word == word[::-1]:
#     print(f'Yes, {word} is a palindrome')
# else:
#     print(f'No, {word} is not a palindrome')
# ```

# ## 11.
# 
# In this question we will use code to generate a random integer between
# 1 and 10. Then we will ask a user to guess the number.
# The code/program should allow the user to keep guessing 
# until they guess the correct number. Or they can type `'stop'` to quit guessing.
# Also, the program should tell the user after each guess whether they should 
# guess lower or higher. When they guess the correct number the program stops
# or if they type `stop`.
# 
# You can use code below to generate a random integer between 1 and 10.
# Execute this code several times to see different values of `i`.
# We will learn more about `import` and modules (such as `random`) 
# later in the course. For now, just know this can generate a random
# integer between 1 and 10. This is the first step.
# 
# ### SOLUTION

# ```
# import random
# max_number = 10 # make this number higher to make it more challenging
# i = random.randint(1, max_number)
# 
# while True:
#     guess = input(f'Please guess a number between 1 and {max_number}. Type "stop" to quit.')
#     if guess == 'stop':
#         print('See you later!')
#         break
#     
#     guess = int(guess)
#     if guess == i:
#         print('YOU GOT IT!')
#         break
#     elif guess > i:
#         print('That is too high. Guess a lower number. Guess again!')
#     else:
#         print('That is too low. Guess a higher number. Guess again!')
#     
# print('Come back again soon!')
# ```

# ## 12.
# Ask a user to enter a number.
# Then print True if the number is 4 or 5 or 6. Otherwise print False.
# Use the `==` and `or` operators.
# 
# ### SOLUTION
# 
# ```
# number = int(input('please enter a number:'))
# if number == 4 or number == 5 or number == 6:
#     print(True)
# else:
#     print(False)
# ```

# ## 13.
# 
# Get the user to input three numbers
# ```
# a = int(input('enter a number'))
# b = int(input('enter a number'))
# c = int(input('enter a number'))
# ```
# 
# Then write code to print which number is the largest.
# Do not use the built in `max` function (we have not even learned this yet anyway). 
# Just use  logical operators, comparison operators, and `if,else` like statements.
# 
# ### SOLUTION
# ```
# a = int(input('enter a number'))
# b = int(input('enter a number'))
# c = int(input('enter a number'))
# 
# if a >= b:
#     largest = a
# else:
#     largest = b
# 
# if c >= largest:
#     largest = c
# 
# print(f'The largest number is {largest}')
# ```

# ## 14.
# In mathematics there is a famous sequence of numbers called the Fibonacci numbers. This sequence of numbers starts with 0 and 1 like this: 
# 
# $$0,1$$
# 
# To get the next number in the sequence you simply add the previous 2 numbers. So the third number in the sequence would be 0 + 1 = 1. Therefore the first three numbers are 
# 
# $$0,1,1$$ 
# 
# To get the next number in the sequence you add 1 + 1 = 2 so now we have 
# 
# $$0,1,1,2$$ 
# 
# The next number would be 1 + 2 = 3 
# 
# $$0,1,1,2,3$$ 
# 
# And you keep continuing like that, always adding the previous two numbers to get the next number in the sequence, 
# 
# 
# $$0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...$$
# 
# Starting with the first two numbers in the sequence $0,1$, write python code to generate the first 1000 numbers in
# the Fibonacci sequence. Store the 1000 numbers in a list.
# 
# So you can start with the following line of code:
# 
# ### SOLUTION

# In[11]:


sequence = [0,1]

for i in range(1,999):
    next_number = sequence[i] + sequence[i-1]
    sequence.append(next_number)
print(sequence[:100]) # the numbers get very large. You can print them all with print(sequence)


# In[ ]:




