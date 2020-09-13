# Intro to Loops

In this section we are going to introduce the `for` 
loop and `while` loop. Loops can be used to iterate
over sequences (strings and lists for example) 
and to execute statements of code multiple times.

As usual, create a Jupyter Notebook 
named **intro_to_loops** and follow along with
the code examples.

(for-loop)=
## For Loop
The general syntax for the `for` loop is

```
for <var> in <iterable>:
    block_of_statements
```

The `iterable` is something that can be iterated over such as a string, or a list, or a `range`.
We will learn about other objects that are `iterable` throughout this course and we will learn about `range`
in this section later. The `var` is any variable name you chose which represents the object in the `iterable`.
The value of it changes each time through the loop. Looking at a specific
example will make it easier to understand.

family_names = ["Chris", "Joanna", "Penelope", "Isaac", "Hazel"]
print(family_names)

We will write a `for` loop to iterate over
the list `family_names` and print each name one at a time.

for name in family_names:
    print(name)

The variable `name` changed each time through the `for` loop.
The first time through the loop `name` was assigned `'Chris'`,
the second time through the loop `name` was assigned `'Joanna'`,
and so on. On the last time through the loop
`name` was assigned `'Hazel'`. In fact, `name` is still assigned
the string object `'Hazel'`.

print(type(name))
print(name)

There is nothing special about the variable name we use
which changes each time through the loop. In this case we chose
`name` because it makes sense to use that since we were iterating
over names in a list. However, we could of chosen `x` for example or
any valid name for a variable.

for x in family_names:
    print(x)

Notice also that we are using indented blocks of code within the loop.
Anything that gets indented within the `for` loop is executed from
top to bottom each time through the loop. Here is another example.

for name in family_names:
    print(f"{name} is a person in my family.")
    print(f"Their full name is {name} Levy.")
    print(f"1 + 1 is 2")
    1 + 4  # this line is executed but we are not printing it
print("DONE!")

Notice in the above example, any statements within the indented code block
inside the `for` loop are executed each time through the loop.
Whereas the `print('DONE!')` is only executed once
because it was outside the `for` loop.

Let's look at an example of iterating over a `string`
object with a `for` loop. This is possible because
`string` objects in Python are also *iterable*.

hello = "Hello World"
print(hello)

for letter in hello:
    print(letter)

for letter in hello[::-1]:  # reversed string
    print(letter)

## Apending In Loops
It is sometimes useful to create an empty list `[]`,
and to keep appending to it within a loop while iterating over some other
iterable. This will also be a good example to show some `if` statements
within a `for` loop.

Here we define a list called `numbers`.
We want to iterate over `numbers`
and check if the number is greater than 6.
If so, append the number to a list `new_numbers`.

numbers = [9, 6, 4, 3, 6, 10, 12, 65, 8, 4, -10, -6, 7, -8]
new_numbers = []  # we create an empty list so we can append items to it

for num in numbers:
    if num > 6:
        print(f"Adding the item {num} to the list new_numbers.")
        new_numbers.append(num)
        print(f"The list new_numbers is now {new_numbers}.")

new_numbers

Here is another example of using a for loop to get the unique
set of numbers from a list.


numbers = [
    1,
    1,
    1,
    2,
    6,
    7,
    8,
    8,
    8,
    8,
    8,
    10,
    10,
    10,
    9,
    9,
    9,
    0,
    0,
    0,
    2,
    2,
    3,
    3,
    3,
    4,
    5,
]
unique_numbers = []

for x in numbers:
    if x not in unique_numbers:
        unique_numbers.append(x)

print(f"There are {len(unique_numbers)} unique numbers and they are {unique_numbers}")

(intro-range)=
## range()
The `range()` function is used to create an **iterable**
that is a sequence of numbers.

x = range(10)

x

print(type(x))

print(x)

You can iterate over the range with a for loop.

for i in x:
    print(i)

for num in range(5):
    print(num)

The general syntax for `range` is `range(start, stop, step)`

for x in range(10, 20):
    print(x)

for x in range(5, 15, 2):
    print(x)

# Using a range to sum up the numbers from 1 to 100
answer = 0
for i in range(1, 101):  # up to but not including 101
    answer = answer + i
print(answer)  # 1 + 2 + 3 + 4 + ..... + 100

## Nested Loops
You can nest any number of `for` loops within a `for` loop.
Here is an example.

for i in range(3):
    for j in range(3):
        print(i, j)

# the multiplication table (using digits 0 through 9)
for i in range(10):
    for j in range(10):
        print(f"{i} multiplied by {j} is {i * j}")
        print("----------------------")

## `break` statement

The `break` statement can be used within a loop
to stop the execution of the loop before it is finished.
For example, you might want to "search" for something 
each time through the loop and stop looping over the additional
items once you have found it.

Here is an example of looking the the number `0` in a list
using a `for` loop. We use `break` to stop the iterations
if the `0` is found.

some_stuff = [1, 9, 5, 7, 5.53, 5, 0, "a", "b", True, False]

print("starting the search")

for x in some_stuff:
    print(x)
    if x == 0:
        break  # this will stop the execution of the for loop and go the next section of code

print("ending the search")

## `continue` statement
The `continue` statement can be used to stop the current iteration of
a loop and **continue** with the next iteration. So unlike the `break`
statement it does not stop the entire loop. It just skips the rest of the
code for the current iteration and moves to the next iteration in the loop.
Here is an example.

print(some_stuff)

print("starting the loop")
for thing in some_stuff:
    if thing == "a" or thing == "b" or thing == 5.53:
        continue  # skips the rest of the code in the indented block and moves to the next item in the list
    print(thing)
print("ending the loop")

## `while` loop
Now that we know a little about the `for` loop we are going to 
learn about the `while` loop. The general syntax is


```
while condition:
    block_of_statements
```

The `condition` is a boolean expression or variable.
As long as the `condition` is `True`, the code within
the `block_of_statements` will be executed. As soon
as the `condition` is `False`, the code within the `while` 
loop (which is the `block_of_statements`) will not be executed.
So you have to be careful with `while` loops because if the
`condition` is always `True` it will become an infinite loop
and loop forever!

Let's look at this example.
The variable `i` is initially 0.
So the condition `i < 10` is `True`. Therefore
the code indented within the loop is executed.
It prints `0 is less than 10` and then changes
the variable `i` to 1. Then it goes back
to the top and the condition is now `i < 10` with
the value of `i` as `1` so the condition is `True`
and that code in the loop is repeated again.
Each time through the loop the value of `i` is
incremented by 1. Eventually `i` will be 10 and
the condition `i < 10` will be `False` so the the code
within `while` loop will not be executed anymore.

print('start')
i = 0
while i < 10:
    print(f'{i} is less than 10')
    i = i + 1
print('end')

If the condition for a while loop is `False` to begin with, the code within
the loop is never executed. So the `condition` is always checked before 
starting the loop. For example, nothing here will be printed.

i = -1
while i > 0: # is never True
    print(i) # does not get executed

You can use the `break` and `continue` statements with
`while` loops just like with `for` loops. Here are some examples.

# break statement example
print('starting')
n = 10
while n > 0:
    n = n - 1
    if n == 3 or n == 1:
        break
    print(n)
print('ending')

# continue statement example
print('starting')
n = 10
while n > 0:
    n = n - 1
    if n == 3 or n == 1:
        continue
    print(n)
print('ending')

### infinite `while` loops
If the `condition` within the `while` loop
is always `True` the loop will never terminate
and the code will execute forever. For example,
this loop would never terminate.

```
x = 1
while x > 0:
    print(x)
    x = x + 1
```

You would have to **stop** it manually by killing the program.
If this ever happens in a Jupyter Notebook you can press the stop (square)
button at the top of the notebook to stop the execution of the code.

## `pass` statement
The `pass` statement is not related to loops but this is a good place to learn about it because
we have just learned about the `break` and `continue` statements.
The `pass` statement can be used as a fill in for future code that is not written yet. 
You can use the `pass` statement to avoid getting an error when empty code is not allowed in
indented code blocks. Here are some examples.

a = 2
if a == 2:
    # some code to be written at a later time

print('I am done')

Notice that the above code returns a `IndentationError`. This is because
we have an indented code block and no code is in the block.
It may be the case that we have some complex logic to write but
we want to do it at a later time without the code breaking.
That is, if condition `a == 2` is `True` then we want to **skip** that indented
code block and continue on with the code. This is what the `pass` statement is used
for.

a = 2
if a == 2:
    # some code to be written at a later time
    pass

print('I am done')

Here is another example using `pass`.

for i in range(10):
    if i > 5:
        print(i)
    else:
        # come back to this code later
        pass