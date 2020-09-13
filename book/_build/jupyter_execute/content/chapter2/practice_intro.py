# Practice Questions
There is so much new stuff we learned this past chapter.
We introduced you to boolean data types, comparison operators,
logical operators, `if`, `elif`, and `else` statements,
lists, as well as `for` and `while` loops. There is actually
more we could say about all of these things. But now is a good time
to get coding. The best way to learn is by doing. Moreover, it is good
to work on problems which mix all these ideas and tools together. It is going to be
hard at first! It takes practice. But as you start solving small problems,
you will learn and become more confident. As you spend more time coding,
you will learn tricks and things that you can apply to other problems.

## 1. 

Ask the user to enter a number using the `input` function. If the number is even
then print a message that displays the number and that it is even. If the number is not
even then change the message to say that the number is odd. For example, if the user enters
a 10 the message might read `'The number 10 is even'`. If the user enters an odd number such as 13, then
the message might read `'The number 13 is odd'`.

### HINT

Try the question first before revealing the hint.

```{toggle}
The `input()` function always returns a string. You can convert a string to an integer using
the `int()` function. You can read this [section](mod-operator) if you forget how to check if a number is even. Finally, refer back to this [section](if-elif-else) on how to use `if` and `else`.
```
    

## 2. 

Suppose you are given a list `nums = [6, 7, 7, 10, 12, 1, 3, 3, 5, 5, 7, 8, 9, 12, 20]`. Write code
that prints all the numbers that are strictly greater than `5` and strictly less than `9`, one line at a time. The code should work for any list (not just this example list). For example the output should look like this:
```
6
7
7
7
8
```
If the list was for example `nums = [1,2,5,20]` the output would be
```
6
```
If the list was `nums = [1,2,6,20]` then nothing would be printed.


### HINT 

Try the question first before revealing the hint.

```{toggle}
Read the [section](for-loop) on `for` loops to recall how to iterate through items in a list.
You will want to make use of the logical `and` [operator](and-operator) as well as `if else` [section](if-elif-else).
```

## 3. 

Repeat question number 2 by adding in this difference. Instead of printing the numbers one by one, make a new list that has all the numbers strictly greater than `5` and strictly less than `9` from the original list. Then just print the new list.

### HINT 

Try the question first before revealing the hint.

```{toggle}
You can refer back to the section on the `.append()` [method](append-list).
```



nums = [6, 7, 7, 10, 12, 1, 3, 3, 5, 5, 7, 8, 9, 12, 20]
new_nums = []
for x in nums:
    # if the number is between 5 and 9, then append x to new_nums
    pass # this just indicates unfinished code and pass is used to simply skip over

## 4.

Write code that takes the list `colors = ['green','red','orange','blue','yellow']`
and prints the first item and the last item in the list. Use `print(colors)` before
and after your code to make sure it worked! No `for` loop is needed here (just list indexing).

### HINT 

Try the question first before revealing the hint.


```{toggle}
Check out the [section](list-index-slice) on how to access values in a list by indexing and or slicing.
```

## 5.

Write a program that prints the numbers from 1 to 100. 

### HINT

Try the question first before revealing the hint.



```{toggle}
Use the [range](intro-range) function.
```

## 6.

Write a program that prints the numbers from 1 to 100 but with these modifications. If the number is a multiple of 3 print **Fizz** instead of the number. If the number is a multiple of 5 then print **Buzz**. However, if the number is both a multiple of 3 and a multiple of 5 print **FizzBuzz**. The output should look something like this:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
.
.
.
.
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
```

### HINT

Try the question first before revealing the hint




for i in range(1,101):
    # if i is divisible by 3 and i is divisible by 5 then print('FizzBuzz')
    # else if i is divisible by 3 then print('Fizz')
    # else if i is divisible by 5 then print('Buzz')
    # else then print i
    pass

## 7.
Suppose you have two lists `a` and `b` which may not be the same length.
Write code which will find the items that are common between both `a`
and `b` and puts them in a new list `c`. Also make sure that `c` does not have
the same item more than once (no duplicates). So the list `c` will be a unique
list of only the items that were in both `a` and `b`. The items you put in `c`
can be in any order.

For example,

```
a = [1,2,3,3,5,5,10]
b = [9,8,5,9,5]
# then c would be
c = [5]
```

```
a = ['carrot', 'orange']
b = ['orange','chris',True]
# then c would be
c = ['orange']
```


```
a = [1,2,3,4,5,7]
b = [1,2,10]
# then c would be
c = [1,2]
```

```
a = [1,2,3,True]
b = [4,5,6,False]
# then c would be
c = []
```

### HINT

Try the question first before revealing the hint.

```{toggle}
You will want to review the sections on [appending to a list](append-list), [membership operators](membership-operators), and [stuff](for-loop) about `for` loops.

There is another hint below but have another good attempt before looking.
```



# define the list a and b. You will want to test some different lists.
a = [1,2,3]
b = [2,4,3]
# define an empty list c
for item in a:
    # if item in b and item not in c then append item to c
    pass

## 8.
Write a program that iterates/loops over a list of items
and print how many `0`'s are in the list.
For example if the list was `[True, False, 'hello', 1,2,0,10,0]`
then it would print `2` because there are two `0`'s in the list.

### HINT

Try the question first before revealing the hint.


num_zeroes = 0
list_of_stuff = [True, False, 'hello', 1,2,0,10,0]
for x in list_of_stuff:
    # check if x is 0. If so, then increase num_zeroes by 1
    pass

## 9.
Suppose you have two lists of the same length and that there are only numbers in both the lists.
For example,

`x = [33, 49, 101, 9]`

`y = [10, 12, 20, 1000]`

Write a program that will multiply the numbers from list `x` by the numbers in list `y` element
wise and then sum the results. In other words, the program should compute

$$33*10 + 49*12 + 101*20 + 9*1000 = 11938.$$

The code should work for any lists with numbers that are the same length. Another example would be

`x = [1, 2, 3, 4]`

`y = [5, 6, 7, 8]`

which would lead to

$$1*5 + 2*6 + 3*7 + 4*8 = 70.$$


### HINT

Try the question first before revealing the hint.


x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
length = len(x)

result = 0
for i in range(length):
    # i is the index/position
    # workout x[i] * y[i] and add to result each time through loop.
    pass

## 10.

Write some code which gets a string from user input.
Then print something to the screen saying whether the string
they entered is a palindrome or not. Palindromes are words which are spelled
the same way frontwards and backwards such as `racecar`, `level`, `rotator` and so on.


### HINT

Try the question first before revealing the hint.

```{toggle}
Remember you can reverse a string `x` by doing `x[::-1]`.
```

## 11.

In this question we will use code to generate a random integer between
1 and 10. Then we will ask a user to guess the number.
The code/program should allow the user to keep guessing 
until they guess the correct number. Or they can type `'stop'` to quit guessing.
Also, the program should tell the user after each guess whether they should 
guess lower or higher. When they guess the correct number the program stops
or if they type `stop`.

You can use code below to generate a random integer between 1 and 10.
Execute this code several times to see different values of `i`.
We will learn more about `import` and modules (such as `random`) 
later in the course. For now, just know this can generate a random
integer between 1 and 10. This is the first step.

import random
i = random.randint(1, 10)
print(i)

Next, use a loop and the `input` function to ask the user to guess a number between 1 and 10.
If they guess too low, then print that the guess it to low and get them to guess again.
If they guess too high, then print that the guess is to high and get them to guess again.
If they guess the correct number (the value of `i`) then print that they got it and stop the program.

### HINT

Try the question first before revealing the hint.

```{toggle}
You will need to use a `while` loop because you do not know how many guess are required.
```

import random
i = random.randint(1, 10)

# remove the far left comments.

# while True:
#     guess = input('Guess a number between 1 and 10. Type "stop" to exit.')
#     # Then do some logic like this
#     # if guess == stop then break the loop and print a message saying all done.
#     # Otherwise, guess should be a number. Remember you need to convert inputs to integers.
#     # Check if the guess is the same as i or too high or too low and use break in proper place.
#     pass

import random
i = random.randint(1, 10)

# remove the far left comments.

# while True:
#     guess = input('Guess a number between 1 and 10. Type "stop" to exit.')
#     if guess == 'stop':
#         print('See you later!')
#         break
#     # convert to integer
#     guess = int(guess)
#     # finish the logic by checking guess with the random value i
#     pass

## 12.
Ask a user to enter a number.
Then print True if the number is 4 or 5 or 6. Otherwise print False.
Use the `==` and `or` operators.

## 13.

Get the user to input three numbers
```
a = int(input('enter a number'))
b = int(input('enter a number'))
c = int(input('enter a number'))
```

Then write code to print which number is the largest.
Do not use the built in `max` function (we have not even learned this yet anyway). 
Just use  logical operators, comparison operators, and `if,else` like statements.