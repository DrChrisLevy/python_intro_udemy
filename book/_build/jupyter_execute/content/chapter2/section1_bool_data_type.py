# Boolean Data Types

In computer programming, a **boolean** data type is a data type that
can have one of *two* values which are usually denoted as *true*
and *false*. In Python the syntax for these two values are `True`
and `False`. These two values are built into the Python
programming language and are of type **boolean** or **bool**
for short.

Create a new Jupyter Notebook and call it **booleans_comparison_logical_operators**.
Type out the code as you read and go through this. Play around with code
because it will help you to learn!

True

False

type(True)

type(False)

They are case sensitive. If you try writing for example, `true`, or `FALSE`, or some variation
you will get an error.

So why is this important? Well, often programs are made up
of lots of tiny decisions that depend on various outcomes.
For example, you might want to perform some logic *if something is `True`*
or perform different logic *if something is `False`*. This is why
boolean data types are so important.

You may be wondering how does something evaluate to `True` or `False`? 
To start learning more about this we are going to introduce
the Python *comparision operators*.

# Comparison Operators

Comparison operators are used to compare the values
of two objects. For example, you might want to compare

- is `a` equal to `b`:   `a == b`
- is `a` not equal to `b`:   `a != b`
- is `a` greater than `b`:   `a > b`
- is `a` less than `b`:   `a < b`
- is `a` greater than or equal to `b`:   `a >= b`
- is `a` less than or equal to `b`:   ` a <= b`

## `==` operator
First we will learn how to check if two things are *equal*
in Python. To do this we use the operator `==`.
When comparing two objects with `==`, it will return 
`True` if the two values are equal otherwise it will return
`False`. Here are some examples. Notice that the return type
of each expression is a Boolean data type (`True` or `False`).

1 == 1 

1 == 2

'hello world' == 'hello world'

'Hello world' == 'hello world' # not the same string because capital H on the left

a = 'string'
b = 10
a == b

a = 5
b = 6
c = 3
d = 14

print(a + b)
print(d - c)
print(a + b == d - c)

str1 = "a b c d e f"[::2] # from index 0 to end with a stride of 2
print(str1)

str2 = "a  b  c  d  e  f"[0::3] # from index 0 to end with a stride of 3
print(str1)

# str1 and str1 are the same value
str1 == str2

True == False # they are not equal so returns False

True == True

False == False

## `!=` operator

The operator `!=` checks if two things
are *not equal*. It returns `True` if they
are not equal and `False` otherwise.


1 != 1

True != False

True != True

False != False

str(40) + str(40) != 4040

str(40) + str(40) != '4040'

40 + 40 != 80

40 + 40 != '80'

3.14 != 6.28 / 2

## `>` operator
This is the *greater than* operator: `>`.
It returns `True` if the value on the left
is *greater* than the value on the right.
Otherwise it returns `False`.

2 > 1 # yes, 2 is greater than 1

1 > 2 # no, 1 is not greater than 2

2 > 2

0 > -2

-2 > -5 + 4

## `<` operator

This is the *less than* operator: `<`.
It returns `True` if the value on the left
is *less* than the value on the right.
Otherwise it returns `False`.

2 < 1 # no, 2 is not less than 1

1 < 2 # yes, 1 is less than 2

2 < 2

0 < -2

-2 < -5 + 4

## `>=` operator

This is the *greater than or equal to* operator: `>=`.
It returns `True` if the value on the left
is *greater than or equal to* the value on the right.
Otherwise it returns `False`.

5 >= 5

5 >= 3

## `<=` operator

This is the *less than or equal to* operator: `<=`.
It returns `True` if the value on the left
is *less than or equal to* the value on the right.
Otherwise it returns `False`.

-2 <= -2

-2 <= -1

# Logical Operators

The three logical operators in Python are `and`, `or`, and `not`. They are used to combine
the `True` or `False` values of variables or expressions into a result that is 
either `True` or `False`. Let's look at some examples.

## `and` operator

x = 5 
print(x > 3 and x < 10) # both are True so result is True

print(x > 3 and x < 0) # one is True and other is False so result is False

print(x < 0 and x > 3) # one is False and other is True so result is False

print(x < 0 and x > 3) # one is False and other is True so result is False

print(x < 0 and x < 3) # both are False so result is False

The above examples were with numbers but the logical operators
can be used with any valid Python expressions that are either
`True` or `False`. For the `and` operator, the result is 
only `True` if both things are `True`. If there is at least one
`False` then the result is `False`. This should be clear from
the English Language. If someone said you could have a cookie
if you *cleaned your room* **and** *cleaned the dishes*, then you
would know you would have to do both things to get the cookie.

True and True

True and False

False and True

False and False

You can chain multiple logical operators together.
And it is often wise to use `()` to keep things clear.
For example,

('hello' == 'hello') and (5 != 6) and (5 > -1) and ('A' != 0) # True and True and True and True is True

('hello' == 'hellooo') and (5 != 6) and (5 > -1) and ('A' != 0) # False and True and True and True is False

When chaining multiple `and`s together, the result is `True` if all the intermediate results are `True`.

## `or` operator

With the `or` operator, the resulting expression is `True` if there is at least
one `True`. Otherwise it is `False`.

True or False

False or True

True or True

False or False

a = 'cat'
b = 'dog'
c = a

a == b or c == a # False or True is True

c == a or a == b # True or False is True

(5 == 5) or ( 0 > 1) or ( 5 == 4) or (10 > -5) or (10 != 10) # at least one is True so result is True

## `not` operator

The `not` operator takes any expression that is `True` or `False` and
simply flips it to the opposite.

not True

not False

not (1 == 1)

not (5 < 4)

not (-4 < -4)

not ('hello' == 'hello')

# Simple Practice Using Operators

We will be using these comparison and logical operators a lot. Take some time now to understand 
what each means and their differences. All of the expressions below will evaluate to either `True` or `False`.
Try them first before checking in python. Make sure you understand why each one 
is either `True` or `False`. These are all examples of boolean expressions. Boolean expressions
are expressions which evaluate to either True or False.

`5 == 5`

`5 >= 5`

`5 <= 5`

` 5 < 6`

`'4' + '3' == 7`

`str(10) + str(10) == '1010'`

`'a' + 'b' == 'a b'`

`5 + int('123') == 5123`

`str(5) + '5' == '55'`

`(5 > 3) and (5 > 4)`

`(5 > 3) and (4 < 5)`

`(5 > 3) or (5 > 4)`

`(2 < 1) or (3 < 1)`

`1 == 1`

`not (1 == 1)`

`5 > 3 or 3 < 5`

`not (5 > 3 or 3 < 5)`

`(not 3 == 5) and not (4 == 4)`

`not ( (True or False) and (False and True) )`

`not (True or False) == not True and not False`

`not (True and True) == not True or not True`