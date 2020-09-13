# `if`, `elif`, and `else` statements

In this section we will learn about `if`, `elif`, and `else` statements and logic in Python.
This is where things start to get interesting because now we will have
the ability to use more complex logic and decision making in our
Python code examples.


## `if` statement

The syntax in general for the `if` statement is:

```
if condition:
    indentedStatementBlock
```

The `condition` is any valid python expression that evaluates to `True` or `False`. 
If the `condition` evaluates to `True`, then the statements in the `indentedStatementBlock` 
are executed. Otherwise the `indentedStatementBlock` is skipped all together.

This is the first time we are seeing the use of white space and *indentation*.
The use of white space and indentation is very important in Python. 
An indented white space is used to start a block of code or statements
and any code that is indented at that level is executed together as a *block of code*.

To start practicing with `if`, `elif`, and `else` statements,
we will use the example of a student receiving a final grade
and determining if they pass or not. The logic will begin
very simple but then we will make it more advanced as we learn more.
To start, suppose a grade of 50% is a passing grade.
So if a student gets less than 50% they fail
and if they get over 50% they pass.

This is what we want the Python code to do in our first example.
If the final grade is greater than or equal to 50 the code
will print a message with their grade and the fact that they passed.
Here is what that would look like using the `if` statement.

final_grade = 60
if final_grade >= 50:
    print(f'Your final grade was {final_grade} so you passed!')

Since the expression `final_grade >= 50` is `True`, the **indented statement block**
is executed and in this case we are printing something. The alternative would be if
`final_grade >= 50` is `False`. In that case the **indented statement block**
would be skipped all together and not executed.

final_grade = 49
if final_grade >= 50:
    print(f'Your final grade was {final_grade} so you passed!')

You see, nothing was printed.

## `else` statement







