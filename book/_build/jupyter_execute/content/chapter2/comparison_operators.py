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