# Numerical Data Types

There are different data types in Python. We have already seen 
objects of type string and integer for example. In this section
we are going to focus on data types that are numeric. Numeric
data types are for objects that are numbers. The *integer* type
is an example of a numeric data type.

There are three distinct numeric types in Python: **integers**, **floating point numbers**, 
and **complex numbers**. Integer type and floating point type
are by far the most common type for numbers and that will be
our main focus here. Complex numbers are not used much in Python programming and 
you can Google it if you are interested.

Create a Jupyter Notebook called **numerical_data_types**
and follow along!

## Integer Type

Integers are like whole numbers, but they also include negative numbers.
They do not include fractions or decimals. Here are examples of integer values,

$$...,-6,-5,-4-3,-2,-1,0,1,2,3,4,5,6,...$$

They go on forever in both directions (negative infinity to positive infinity).

x = 10
print(x)
print(type(x))
y = x - 5
print(y)
print(type(y))
y = y * y + y
print(y)
print(type(y))

The `'int'` in `<class 'int'>` stands for integer.

Here is another example of working with integer types.

starting_temperature = 5
ending_temperature = starting_temperature - 7
print(type(starting_temperature))
print(type(ending_temperature))
print(ending_temperature)

## Floating Point Type

*Floating point type* numbers (or just *float* for short)
are numbers with a decimal. Whenever you do
division you end up with a number of type *float*.

a = 10
b = 5
c = a / b
print(c)
print(type(c))
d = b / a
print(d)
print(type(d))

w = 1 / 9
v = 2 / 9
print(w + v)
print(type(w + v))