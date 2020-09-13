# More on Strings

In this section we will learn more about strings. Create a 
new Jupter Notebook and name it **string_formatting_and_indexing**
so you can follow along with the code.

## String Formatting

It is often the case that we want to substitute some variable
or Python expression into a string. This is called string formatting.
There is multiple ways to do this
in Python. There is the "old way" of doing it and the newer way
in Python 3.6. The easiest method is to use *f-strings* which will use a lot
in this book. But here we will first show the old way of doing it to
because you might see it while reading Python code.

### String Formatting with the (% Operator)

This is the old way of doing it and we will not use
it much. But it's still good to know about.
The `%s` is used to substitute the value
of the variable `name` into the string.
So if you ever see this in Python code
that is what is happening (string formatting).



name = 'chris'
print('my name is %s' %name)

### String Formatting with .format
This is a newer way of formatting strings.
Again, we will not use this method because
we will opt to use **f-strings**. It's
still good to know about. You can
see the syntax is nicer because 
it does not require the use of `%s`.


print('my name is {}'.format(name))

### f-strings

This is the preferred method to
format strings and substitute 
variables and other Python expressions 
into strings. Learn and know this method
because it is very useful!.
They are called **string literals**
or **f-strings**. Here is an example.

print(f'my name is {name}')

And that's it! You simply put an `f`
at the beginning of the string in front of the quote.
You then use the braces `{}` and put the Python expression
between the braces. Here are some more examples.

print(f'one plus two is {1 + 2}')

name = "Chris"
age = 35
province = 'Nova Scotia'
country = 'Canada'
print(f"Hey there! My name is {name} and I am from {province}, {country}. I am {age} years old.")

Notice in the above example we were able to substitute an integer object, `age` directly 
into the string with the use of **f-strings**. If we had to do the above with
string concatenation it would look more complex. We would also have to convert the 
the `age` to a string with the `str()` function. But when using **f-strings** Python
will take care of these smaller details.

print("Hey there! My name is "  + name + " and I am from " +  province + ", " + country + ". I am " + str(age) + " years old.")

It is much easier to code it using the `f-string` method! 

The f-strings work in multiline strings too.

my_multi_line_string = f"""
Name: {name}

Age: {age}

Province: {province}

Country: {country}
"""
print(my_multi_line_string)

## Indexing and Slicing Strings

Python strings are sequences made up of one or more individual characters.
You can access a specific character in a string at any position
by using its index. Index numbers allow us to access specific characters within a string.
You use the square brackets `[]` and the index number to get a character at the
position/index in the string.
Let's look at some examples. 
```{note}
We will start using Python comments in our code.
Comments are lines in your python code that are not
executed. They are any line that begins with a `#` symbol.
Comments can be used to explain Python code, make it more readable,
and can prevent execution when testing.
```

# These lines are an example of a Python comment. It is
# text in your Python code that is not executed. 
# You can make comments through out your 
# code to make it more readable and explain certain things.

# Here is an example of indexing a string to get specific characters at
# a position/index.

hello_str = 'Hello World!'
print(hello_str)

print(hello_str[0]) # counting and indexing in Python always starts at 0
print(hello_str[1])
print(hello_str[2])
print(hello_str[3])
print(hello_str[4])
print(hello_str[5])
print(hello_str[6])
print(hello_str[7])
print(hello_str[8])
print(hello_str[9])
print(hello_str[10])
print(hello_str[11])

If we try to index a string at a position that
is outside the length of the string we will get an index error.
The string in the above example, `hello_str` has a length of 12
because it has 12 characters. `hello_str[0]` is the first character,
`hello_str[1]` is the second character, and `hello_str[11]` is the last character.
Here we try and access `hello_str[12]` which will raise an error.
It's an `IndexError` because we are trying to access index 12
which is outside the range of the string.

hello_str[12]

You can even use negative numbers for indexes
starting with `-1` which will be the index
for the last character of a string. 
`-2` will be the index for the second last
character and so on.

print(hello_str[-1])
print(hello_str[-2])
print(hello_str[-3])
print(hello_str[-4])
print(hello_str[-5])
print(hello_str[-6])
print(hello_str[-7])
print(hello_str[-8])
print(hello_str[-9])
print(hello_str[-10])
print(hello_str[-11])
print(hello_str[-12]) 

print(f"""The first character of '{hello_str}' is {hello_str[0]},
the 5th character is {hello_str[4]} and the last character is 
{hello_str[-1]}.""")

You can also access a slice of a string using the notation
`[a:b]` which will get every character from index `a`
up to index `b` but **not** including `b`.

print(hello_str[0:5]) # gets the characters at index 0,1,2,3,4

print(hello_str[6:11]) # gets the characters at index 6,7,8,9,10,

print(hello_str[6:]) # will index everything from index 6 and after

print(hello_str[6:20]) # when slicing, you can access outside the range and it won't throw an error

print(hello_str[-5:-2]) # you can even use negative indexes when slicing

We can also set a **stride** when slicing strings.
By default this stride is equal to one as we have not been specifying it 
in the above examples.

# This third number 2 is called the stride.
# Here we are using a stride of 2.
# It starts at index 0, up to and not including index 12,
# and takes every second character along the way.
# If the stride is 3 it takes every third character and so on.
print(hello_str[0:12:2]) 

print(hello_str[0:12:1]) # stride of 1 does no skipping
print(hello_str[0:12]) # stride of 1 by default
print(hello_str[0:12:3]) # stride of 3 example

You can even set a negative value for the stride.

print(hello_str[-1:-12:-2])
print(hello_str[::-2]) # same thing as directly above.
print(hello_str[::-1]) # a stride of -1 is an easy way to reverse a string.