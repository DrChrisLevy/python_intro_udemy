# Intro to Functions

So what is a function anyway? 

```{admonition} Functions
In the Python programming language, a function is a block of reusable code that is typically used to perform a single process or action. Functions are the main building blocks of the programs and applications you create. By using functions, your code will have better modularity and will be easier to reuse. 
```

Python has many built in functions and you can also create your own functions. Functions are not completely new to you and you have already been using functions whether or not you know it. Here are examples of functions, built into Python, that you have
been using throughout this book and course so far:

- `print()`
- `str()`
- `int()`
- `float()`
- `type()`
- `len()`
- `range()`

So what do these **functions** all have in common? Well to begin, they all have **names**. For example, the
name of the `print()` function is `print`. They can be used or **called** and when you **call** them 
you always use the brackets `()`. The functions listed above all took input **arguments** which is the stuff you
type inside the brackets `()`. Another name for **arguments** is **parameters**. In all the cases, the functions performed some action or process by executing a block of Python code internal to that function.

For example we can use the `len()` function to get the length of a string or a list.

x = len('Hello')
print(x)

x = len([0,1,2,3,4])
print(x)

## Built-in Python Functions

Python has a number of functions built into it that are always available. You can get a list
[here](https://docs.python.org/3/library/functions.html) for example. Using this link, you can click
on the different functions to see what they do and how they are defined in the documentation.
We will cover some of them here.

### `abs()`
Used to get the absolute value of a number.

abs(5)

abs(-5)

### `max()` and `min()`
The `max()` function will return the largest number in an iterable
and the `min()` function will return the smallest. 
There are different ways to use these. For example:

max(1,2) # an example of passing two arguments

min(1,2)

max(1,2,5,8) # an example of passing four arguments

min(1,2,5,8)

max([1,10,12,10,50,-10,100,-100,1000]) # an example of passing a single list argument

min([1,10,12,10,50,-10,100,-100,1000]) # an example of passing a single list argument

### `round()`
This function can be used to round to the nearest integer
or round to a specific number of decimal points.

round(3.14)

round(2.51)

round(3.14,0)

round(2.51,0)

round(3.1459,2)

round(10.12346,4)

round(10.12344,4)

### `sum()`
For example, to get the sum of the numbers in an iterable (such as a list).

sum([1,2,3])

### `enumerate()`
This function is very useful when looping over lists and so on.
Consider the following loop:

for x in [0,2,4,6,8,10]:
    print(x)

Often when iterating over a list you not only want
the value of the item but also the index posiiton of the item
in the list. This is where `enumerate()` is useful.
You can use it like this:

for i, x in enumerate([0,2,4,6,8,10]):
    print(i,x)

I think this is the first time we have seen a loop with more than
one variable name. Here we are using `i,x`. The `i` is the index
position for the item and `x` is the value. For example:

for i, x in enumerate([0,2,4,6,8,10]):
    print(f'The position of the item is {i} and the value of the item is {x}.')

### `zip()`
This is a neat little function. Here are a couple examples of using it.
Don't worry too much about the details for now.

x = [1,2,3]
y = [4,5,6]

for i,j in zip(x,y):
    print(i,j)

x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
for a,b,c in zip(x,y,z):
    print(a,b,c)

## Defining your own functions


