# Getting Input From a User

In Python you can get input from a user with the `input()` function.
Create a Jupyter Notebook called **user_input** and follow along
to see how it works. Note that I can not use the `input()` function
in this book and have it displayed properly. 
Therefore I will provide a screenshot when using that function.

In a Jupter Notebook type the following code in a cell
and then execute the cell.

`name = input('Enter your name: ')`

You will be presented with an input box where you
can enter some text.
![user_input](user_input.png) 

Type your name in the box.

![user_input_with_name](user_input_with_name.png)

Then hit **return** on the keyboard.
What this does is reads in the input
as a string (it always converts whatever you enter to a string). 
Here we store the results with the variable `name` in this
case. You can than use `name` like any regular Python variable.
Here we print the type and value of `name`.
![user_input_print](user_input_print.png)

Here is another example:
![input_age](input_age.png)

After typing your age and then hitting return:

![input_age_print](input_age_print.png)

Notice that you entered a number but the type of `age` is string.
This is because the `input()` function converts whatever
the user types to a string object. That's it for the `input()`
function. It provides a simple way to collect input from a user
which can be fun to play around with in simple programs
while learning and practicing Python.

## Converting Between Strings and Floats and Integers

You can convert objects of some data types to other data types in Python.
It's not always the case as we will see. Here we will show some examples
of how to convert between strings, integers, and floats.

First we will define the number 1 as a string.

x_str = '1'
print(x_str)
print(type(x_str))
print(x_str + x_str) # string concatenation. That's why we get 11 and not 2.

Since the string `x_str` is a number, we can convert it to
an integer object by using the `int()` function.

# to convert the variable x_str to an integer object
x_int = int(x_str)
print(x_int)
print(type(x_int))
print(x_int + x_int) # integer addition of 1 + 1 = 2

print(type(x_str))

Note that the underlying object for the variable `x_str` will still be a string.
It's just that we took that string object and converted it into
a new integer object and assigned it to `x_int`. But this did not
change the object type for `x_str` because it's still a string.

To convert an object to a float we can use the `float()` function.

y_int = -2
y_float = float(y_int)
print(y_float)
print(type(y_float))
print(y_float * y_float)

# convert float back to int
print(int(y_float))
print(type(int(y_float)))

# y_float is still a float though
# because we did not change it
print(type(y_float))

When we convert a float to an integer,
the `int()` function will take whatever number is
left of the decimal to be the integer. That is,
it always rounds down. `int(5.99)` would be the integer object
`5`.

pi = 3.14159
# int wrapped around a float will 
# always round the float down to nearest integer.
print(int(pi)) 

str(pi) + str(pi) # string concatenation

pi_str = str(pi)
print(pi_str)

float(pi_str)

# can't convert a string that is a decimal number to an integer.
# int() function expects an integer string or a float, 
# but not a float string.
int(pi_str) 


int('a') # of course you can not convert an letter character to an integer

The above code cells are supposed to give
you some ideas of how to use `str()`, `int()`, and `float()`
functions to convert between string, integer, and float data types. 
If you are ever unsure, just try it out! That is the beauty of interactive Python.
You can just type a simple example and see if it works.

Here is one more example
using the `input()` function. As mentioned earlier,
we have to provide a screenshot because
the `input()` function can not be displayed properly
within this book.

![input_number_100](input_number_100.png)

# if you got this from the input 
# you can remove this line directly below.
number_str = '100' 
print(number_str)
print(type(number_str))
# convert to an integer so we can do integer add below.
number_int = int(number_str) 
print(f'The number {number_int} plus 5.94 is {number_int + 5.94}')