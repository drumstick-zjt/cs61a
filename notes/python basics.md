# Python Basics

## 1. Arithmetic expressions

- Floating point division (`/`): divides the first number number by the second, evaluating to a number with a decimal point *even if the numbers divide evenly*.
- Floor division (`//`): divides the first number by the second and then rounds down, evaluating to an integer.
- Modulo (`%`): evaluates to the **positive** remainder left over from division.
- **Python doesn't have "++" or "--" operation like C or Java**

## 2. Functions

### 2.1 Defining functions

The most common way to define functions is Python is the `def` statement.

```python
def <name>(<parameters>): 		# ← Function signature
    return <return expression>  # ← Function body
```

example:

```python
def add(num1, num2):
    return num1 + num2
```

### 2.2 Functions in environment diagrams

How Python interprets a def statement:

- It creates a function with the `name` and `parameters.`
- It sets the function body to everything indented after the first line.
- It binds the function name to that function body (similar to an assignment statement).

How Python interprets a function call:

- It creates a new **frame** in the environment.
- It binds the function call's arguments to the parameters in that frame.
  - The arguments in the local in that frame is a copy of the real parameters.
- It executes the body of the function in the new frame.

All Python code is evaluated in the context of an **environment**, which is a sequence of frames.

### 2.3 Name lookup rules

How Python looks up names in a user-defined function:

1. Look it up in the local frame
2. If name isn't in local frame, look it up in the global frame
3. If name isn't in either frame, throw a NameError

***This is simplified since we haven't learned all the Python features that complicate the rules.***

## 3. Control

### 3.1 Side effects

#### 3.1.1 The None Value

The special value `None` represents nothingness in Python. Any function that doesn't explicitly return a value will return `None`.

A **side effect** is when something happens as a result of calling a function besides just returning a value.

The most common side effect is logging to the console, via the built-in `print()` function.

Other common side effects: writing to files, drawing graphics on the screen.

#### 3.1.2 Pure vs. non-pure functions

<img src=".\assets\week1\pure-non-functions.png" alt="pure-non-functions" style="zoom:33%;" />

What will this display?

```python
print(print(1), print(2))
# None None
```

### 3.2 More function features

#### Default arguments

In the function signature, a parameter can specify a **default value**. If that argument isn't passed in, the default value is used instead.

```python
def calculate_dog_age(human_years, multiplier = 7):
    return human_years * multiplier
```

Default arguments can be overridden two ways:

```python
calculate_dog_age(3, 6)
calculate_dog_age(3, multiplier=6)
```

#### Multiple return values

A function can specify multiple return values, separated by commas.

```python
def divide_exact(n, d):
    quotient = n // d
    remainder = n % d
    return quotient, remainder
```

Any code that calls that function must also "unpack it" using commas:

```python
q, r = divide_exact(618, 10)
```

#### Function name as a variable

Unlike any other programming language, python can convey function's name as a variable. Example:

```python
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)
```

### 3.3 Conditionals

A **conditional statement** gives your code a way to execute a different suite of code statements based on whether certain conditions are true or false.

```python
if <condition>:
    <statement>
    ...
elif <condition>:
    <statement>
    ...
elif <condition>:
    <statement>
	...
else:
    <statement>
    ...
```

**By the way, python doesn't have `?:` operation.** 

**The substitute is `[expressionA] if [expressionB] else [expressionC]`**:

```python
res = a if a > b else b
# <==> res = max(a,b)
```

Another thing to remember is that python doesn't have `&&` or `||` or `!`operation, the substitute are `and` 、`or` and `not`.

#### Short circuiting

What do you think will happen if we type the following into Python?

```python
1 / 0
```

Try it out in Python! You should see a `ZeroDivisionError`. But what about this expression?

```python
True or 1 / 0
```

It evaluates to `True` because Python's `and` and `or` operators *short-circuit*. **That is, they don't necessarily evaluate every operand.**

| Operator | Checks if:                 | Evaluates from left to right up to: | Example                                |
| :------- | :------------------------- | :---------------------------------- | :------------------------------------- |
| AND      | All values are true        | The first false value               | `False and 1 / 0` evaluates to `False` |
| OR       | At least one value is true | The first true value                | `True or 1 / 0` evaluates to `True`    |

Short-circuiting happens when the operator reaches an operand that allows them to make a conclusion about the expression. For example, `and` will short-circuit as soon as it reaches the first false value because it then knows that not all the values are true.

**If `and` and `or` do not *short-circuit*, they just return the last value**; another way to remember this is that **`and` and `or` always return the last thing they evaluate, whether they short circuit or not**. Keep in mind that `and` and `or` don't always return booleans when using values other than `True` and `False`. The examples are as follows.

<img src=".\assets\week2\short-circuiting.png" alt="short-circuiting" style="zoom:50%;" />

### 3.4 Booleans

A **Boolean value** is either `True` or `False` and is used frequently in computer programs.

An expression can evaluate to a Boolean. Most Boolean expressions use either comparison or logical operators (and or not).

**Truthy and Falsey Values**: It turns out `and` and `or` work on more than just booleans (`True`, `False`). Python values such as `0`, `None`, `''` (the empty string), and `[]` (the empty list) are considered false values. *All* other values are considered true values.

### 3.5 Iteration

#### While loops

The while loop syntax:

```python
while <condition>:
    <statement>
    <statement>
```

It's common to use a **counter variable** whose job is keeping track of the number of iterations.

```python
total = 0
counter = 0
while counter < 5:
  total += pow(2, 1)
  counter += 1
```

To prematurely exit a loop, use the `break` statement:

```python
counter = 100
while counter < 200:
    if counter % 7 == 0:
        first_multiple = counter
        break
    counter += 1
```

## 4. Higher-order Functions

### 4.1 Describing functions

```python
def square(x):
    """Returns the square of X."""
    return x * x
```

| Aspect                                                       | Example                                     |
| :----------------------------------------------------------- | :------------------------------------------ |
| A function's **domain** is the set of all inputs it might possibly take as arguments. | `x` is a number                             |
| A function's **range** is the set of output values it might possibly return. | `square` returns a non-negative real number |
| A pure function's **behavior** is the relationship it creates between input and output. | `square` returns the square of `x`          |

### 4.2 Generalization

The concept of Generalization is to reduce redundant codes.

### 4.3 Higher-order functions(HOF)

#### def

A function that either:

- Takes another function as an argument
- Returns a function as its result

All other functions are considered first-order functions.

#### [Functions as arguments](# Function name as a variable)

#### Functions as return values

Functions defined within other function bodies are bound to names in a local frame.

```python
def make_adder(n):
    """Return a function that takes one argument k
       and returns k + n.
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder
```

Once many simple functions are defined, function *composition* is a natural method of combination to include in our programming language. That is, given two functions `f(x)` and `g(x)`, we might want to define `h(x) = f(g(x))`. We can define function composition using our existing tools:

```python
>>> def compose1(f, g):
        def h(x):
            return f(g(x))
        return h
```

### 4.4 Lambda Syntax

A **lambda expression** is a simple function definition that evaluates to a function.

The syntax:

```python
lambda <parameters>: <expression>
```

A function that takes in `parameters` and returns the result of `expression`.

A lambda version of the `square` function:

```python
square = lambda x: x * x
```

A function that takes in parameter `x` and returns the result of `x * x`.

A lambda expression does **not** contain return statements or any statements at all.

#### Def statements vs. Lambda expressions

<img src=".\assets\week2\lambda.png" alt="lambda" style="zoom:50%;" />

| Both create a function with the same domain, range, and behavior. |
| ------------------------------------------------------------ |
| Both bind that function to the name "square".                |
| Only the `def` statement gives the function an **intrinsic name**, which shows up in environment diagrams but doesn't affect execution (unless the function is printed). |

#### Lambda as argument

It's convenient to use a lambda expression when you are passing in a simple function as an argument to another function.

Instead of...

```python
def cube(k):
    return k ** 3

summation(5, cube)
```

We can use a lambda:

```python
summation(5, lambda k: k ** 3)
```

An example:

```python
lambda x: x if x > 0 else 0
```

### 4.5 *Args

What if you want a function to accept any number of arguments?

That's possible by using the `*args` syntax in the function definition.

```python
def func(*args):
    # Do something with *args
```

One way to use `*args` is to send those arguments into another function.

```python
def min_and_max(*args):
    return min(*args), max(*args)

min_and_max(-2, 33, -40, 400, 321) # -40, 400
```

**Also, *args can be used to forward a HOF.**


```python
def printed(f):
    def print_and_return(*args):
        result = f(*args)
        print('Result:', result)
        return result
    return print_and_return

printed_max = printed(max)
printed_max(-2, 33, -40, 400, 321)
```

## 5. Environments

Every expression is evaluated in the context of an environment.

A name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found.

- Every user-defined **function** has a parent frame. The parent of a **function** is the **frame in which it was defined**.

- Every local **frame** has a parent frame. The parent of a **frame** is the **parent of the called function**

### 5.1 Local Name visibility

**Local names are *not* visible to other (non-nested) functions.**

An environment is a sequence of frames.

The environment created by calling a top-level function consists of one local frame followed by the global frame.

### 5.2 Function currying

**Currying:** Converting a function that takes multiple arguments into a single-argument higher-order function.

A function that currys any two-argument function:

```python
def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
```

```python
make_adder = curry2(add)
make_adder(2)(3)
```

## 6. String formatting

### 6.1 String concatenation

So far, we've been using the + operator for combining string literals with the results of expressions.

```python
artist = "Lil Nas X"
song = "Industry Baby"
place = 2

print("Debuting at #" + str(place) + ": '" + song + "' by " + artist)
```

But that's not ideal:

- Easy to bungle up the + signs
- Hard to grok what the final string will be
- Requires explicitly `str()`ing non-strings

### 6.2 String interpolation

**String interpolation** is the process of combining string literals with the results of expressions.

Available since Python 3.5, **f strings** (formatted string literals) are the best way to do string interpolation.

Just put an `f` in front of the quotes and then put any valid Python expression in curly brackets inside:

```python
artist = "Lil Nas X"
song = "Industry Baby"
place = 2

print(f"Debuting at #{place}: '{song}' by {artist}")
```

Any valid Python expression can go inside the parentheses, and will be executed in the current environment.

```python
greeting = 'Ahoy'
noun = 'Boat'

print(f"{greeting.lower()}, {noun.upper()}yMc{noun}Face")

print(f"{greeting*3}, {noun[0:3]}yMc{noun[-1]}Face")
```

## 7. Exceptions & Decorators

### 7.1 Exceptions

Python raises an exception whenever a runtime error occurs. If an exception is not handled, the program stops executing immediately.

To handle an exception (keep the program running), use a `try` statement.

```python
try:
    <try suite>
except <exception class> as <name>:
    <except suite>
   ...
```

example:

```python
try:
    quot = 10/0
except ZeroDivisionError as e:
    print('handling a', type(e))
    quot = 0
return q
```

#### Assert Statements

Assert statements raise an exception of type `AssertionError`

Assertions are designed to be used liberally. They can be ignored to increase efficiency by running Python with the "-O" flag; "O" stands for optimized.

```shell
$ python3 -O test.py
```

#### Raise Statements

Any type of exception can be raised with a `raise` statement.

```python
raise <expression>
```

\<expression> must evaluate to a subclass of `BaseException` or an instance of one.

Exceptions are constructed like any other object. E.g., `TypeError('Bad argument!')`.

### 7.2 Decorators

The notation:

```python
@ATTR
def aFunc(...):
    ...
```

is essentially equivalent to:

```python
def aFunc(...):
    ...
aFunc = ATTR(aFunc)
```

`ATTR` can be any expression, not just a single function name.

## 8. Containers

### 8.1 Lists

#### Def

Lists can hold any Python values, separated by commas: 

```python
members = []
members = ["Pamela", "Tinu", "Brenda", "Kaya"]
ages_of_kids = [1, 2, 7]
prices = [79.99, 49.99, 89.99]
digits = [2//2, 2+2+2+2, 2, 2*2*2]
remixed = ["Pamela", 7, 79.99, 2*2*2]
```

#### Length

Use the global `len()` function to find the length of a list.

```python
attendees = ["Tammy", "Shonda", "Tina"]

print(len(attendees))   #  3
```

#### Accessing list items (bracket)

Negative indices are also possible:

```python
letters = ['A', 'B', 'C']
# Index:   0     1     2
letters[-1]  # 'C'
letters[-2]  # 'B'
letters[-3]  # 'A'
letters[-4]  # 🚫 Error!
```

#### Accessing list items (func)

```python
from operator import getitem

getitem(letters, 0)
```

#### List concatenation

Add two lists together using the `+` operator:

```python
boba_prices = [5.50, 6.50, 7.50]
smoothie_prices = [7.00, 7.50]
all_prices = boba_prices + smoothie_prices
```

Or the `add` function:

```python
from operator import add

boba_prices = [5.50, 6.50, 7.50]
smoothie_prices = [7.00, 7.50]
all_prices = add(boba_prices, smoothie_prices)
```

#### List repetition

Concatenate the same list multiple times using the `*` operator:

```python
boba_prices = [5.50, 6.50, 7.50]
more_boba = boba_prices * 3
```

Or the `mul` function:

```python
from operator import mul

boba_prices = [5.50, 6.50, 7.50]
more_boba = mul(boba_prices, 3)
```

#### Nested Lists

Since Python lists can contain any values, an item can itself be a list.

```python
gymnasts = [ ["Brittany", 9.15, 9.4, 9.3, 9.2],
                ["Lea", 9, 8.8, 9.1, 9.5],
                ["Maya", 9.2, 8.7, 9.2, 8.8] ]
```

> pay attention to len(gymnasts) or len(gymnasts[0]).
>
> accessing by` [][]`.

### 8.2 Containment

#### Containment operator

Use the `in` operator to test if value is inside a container:

```python
digits = [2, 8, 3, 1, 8, 5, 3, 0, 7, 1]

1 in digits # True

3 in digits # True

4 in digits # False

not (4 in digits) # True
```

#### For statements

##### basic

```python
for <name> in <expression>:
    <suite>
```

1. Evaluate the header `<expression>`, which must yield an iterable value (a sequence)
2. For each element in that sequence, in order:
   1. Bind `<name>` to that element in the current frame
   2. Execute the `<suite>`

##### Sequence unpacking in for statements

```python
pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]
same_count = 0

for x, y in pairs:
    if x == y:
        same_count = same_count + 1
```

#### Ranges

A range represents a sequence of ***integers***.

```
range(-2, 3) # -2, -1, 0, 1, 2
range(6) # 0,1,2,3,4,5
```

### 8.3 List Comprehension

A way to create a new list by "mapping" an existing list.

#### short version

```python
[<map exp> for <name> in <iter exp>]

odds = [1, 3, 5, 7, 9]
evens = [(num + 1) for num in odds]
```

#### Long version (with filter):

```python
[<map exp> for <name> in <iter exp> if <filter exp>]

temps = [60, 65, 71, 67, 77, 89]
hot = [temp for temp in temps if temp > 70]
```

#### List comprehension execution procedure

- Add a new frame with the current frame as its parent.
- Create an empty result list that is the value of the expression.
- For each element in the iterable value of `<iter exp>`:
  - Bind `<name>` to that element in the new frame from step 1.
  - If `<filter exp>` evaluates to a true value, then add the value of `<map exp>` to the result list.

#### Example

```python
def divisors(n):
    """Returns all the divisors of N.

    >>> divisors(12)
    [1, 2, 3, 4, 6]
    """
    return [x for x in range(1, n) if n % x == 0]

def front(s, f):
    """Return S but with elements chosen by F at the front.

    >>> front(range(10), lambda x: x % 2 == 1)  # odds in front
    [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    """
    return [e for e in s if f(e)] + [e for e in s if not f(e)]
```

### 8.4 String literal

Multi-line strings automatically insert new lines:

```python
"""The Zen of Python
claims, Readability counts.
Read more: import this."""
# 'The Zen of Python\nclaims, Readability counts.\nRead more: import this.'
```

#### length

```python
s = 'abc'
a = len(s) # a = 3
```

#### Differences between strings & lists

- A single-character string is the same as the character itself.
- The `in` operator will match substrings.

```python
initial = 'P'
initial[0] == initial  # True

'W' in 'Where\'s Waldo'      # True
'Waldo' in  'Where\'s Waldo' # True
```

## 9. Dictionaries + More Lists

### 9.1 Dictionaries 

A `dict` is a mapping of key-value pairs.

```python
states = {
	"CA": "California",
	"DE": "Delaware",
	"NY": "New York",
	"TX": "Texas",
	"WY": "Wyoming"
}

# Dictionaries support similar operations as lists/strings:
>>> len(states)
>>> 5
>>> "CA" in states
>>> True
>>> "ZZ" in states
>>> False
```

#### Accessing a dict

```python
words = {
	"más": "more",
	"otro": "other",
	"agua": "water"
}
# Ways to access a value by key:
>>> words["otro"]
>>> 'other'

>>> words["pavo"]
KeyError: pavo

>>> words.get("pavo", "🤔")
'🤔'
# if exits key "pavo", return its value, else return "🤔"
```

#### Dict Rules

- A key **cannot** be a list or dictionary (or any other mutable type)
- The values can be any type.
- All keys in a dictionary are distinct.

#### Dict Iterations

```python
insects = {"spiders": 8, "centipedes": 100, "bees": 6}
for name in insects:
    print(insects[name])
```

Keys are iterated over in the order they are first added.

#### Dict Comprehensions

```python
{key: value for <name> in <iter exp>}

{x: x*x for x in range(3,6)}

def index(keys, values, match):
    """Return a dictionary from keys k to a list of values v for which 
    match(k, v) is a true value.
    
    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {k: [v for v in values if match(k, v)] for k in keys}
```

### 9.2 List Diagrams

Lists are represented as a row of index-labeled adjacent boxes, one per element.

For nested lists, each box either contains a primitive value or points to a compound value.

### 9.3 Slicing

#### Syntax

Slicing a list creates a new list with a subsequence of the original list.

```python
letters = ["A", "B", "C", "D", "E", "F"]
        #   0    1    2    3    4    5

sublist1 = letters[1:]    # ['B', 'C', 'D', 'E', 'F']
sublist2 = letters[1:4]   # ['B', 'C', 'D']
```

Slicing also works for strings.

```python
compound_word = "cortaúñas"

word1 = compound_word[:5]    # "corta"
word2 = compound_word[5:]   # "úñas"
```

#### Copying whole lists

Slicing a whole list copies a list:

```python
listA = [2, 3]
listB = listA # only give reference, still point to the same list

listC = listA[:] # copy a new list
listA[0] = 4
listB[1] = 5
```

`list()` creates a new list containing existing elements from any iterable:

```python
listA = [2, 3]
listB = listA

listC = list(listA) # same as listC = listA[:]
listA[0] = 4
listB[1] = 5
```

### 9.4 Built-ins for iterables

#### Functions that process iterables

The following built-in functions work for lists, strings, dicts, and any other **iterable** data type.

| Function                                                     | Description                                                  |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| `sum(iterable, start)`                                       | Returns the sum of values in `iterable`, initializing sum to `start` |
| [`all(iterable)`](https://docs.python.org/3/library/functions.html#all) | Return `True` if all elements of `iterable` are true (or if `iterable` is empty) |
| [`any(iterable)`](https://docs.python.org/3/library/functions.html#any) | Return `True` if any element of `iterable` is true. Return `False` if `iterable` is empty. |
| `max(iterable, key=None)`                                    | Return the max value in `iterable`                           |
| `min(iterable, key=None)`                                    | Return the min value in `iterable`                           |

- A **key** function can decide how to compare each value:

  ```python
  coords = [ [37, -144], [-22, -115], [56, -163] ]
  max(coords, key=lambda coord: coord[0])  # [56, -163]
  min(coords, key=lambda coord: coord[0])  #  [-22, -115]
  
  gymnasts = [ ["Brittany", 9.15, 9.4, 9.3, 9.2],
      ["Lea", 9, 8.8, 9.1, 9.5],
      ["Maya", 9.2, 8.7, 9.2, 8.8] ]
  min(gymnasts, key=lambda scores: min(scores[1:]))    # ["Maya", ...]
  max(gymnasts, key=lambda scores: sum(scores[1:], 0)) # ["Brittany", ...]
  ```

### 9.5 Lists' Recursion

#### Recursively sum a list

```python
def sum_nums(nums):
    """Returns the sum of the numbers in NUMS.
    >>> sum_nums([6, 24, 1984])
    2014
    >>> sum_nums([-32, 0, 32])
    0
    """ 
    if nums == []:
        return 0
    else:
        return nums[0] + sum_nums( nums[1:] )
```

When recursively processing lists, the base case is often the empty list and the recursive case is often all-but-the-first items.

#### Recursively reversing a string

```python
def reverse(s):
    """Returns a string with the letters of S
    in the inverse order.
    >>> reverse('ward')
    'draw'
    """
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]
```

When recursively processing strings, the base case is typically an empty string or single-character string, and the recursive case is often all-but-the-first characters.

#### Recursion on different data types

| data type | base case condition    | current item    | recursive case arg |
| --------- | ---------------------- | --------------- | ------------------ |
| lists     | `== []` ,`len(L) == 0` | `L[0]` ,`L[-1]` | `L[1:]` ,`L[:-1]`  |
| Strings   | `== ''` ,`len(S) == 1` | `S[0]`          | `S[1:]` ,`S[:-1]`  |

## 10. Mutability

### 10.1 Objects

Every value in Python is an object.

### 10.2 List Mutation

- `append()` adds a single element to a list.

- `extend(Iterable)` adds all the elements in one list to a list.

  ```python
  s = [2, 3]
  t = [5, 6]
  s.extend(4) # 🚫 Error: 4 is not an iterable!
  s.extend(t)
  t = 0
  ```

- `pop()` removes and returns the last element.

- `remove(arg)` removes the first element equal to the argument.

- use slicing

  ```python
  L = [1, 2, 3, 4, 5]
  
  L[2] = 6
  
  L[1:3] = [9, 8]
  
  L[2:4] = []            # Deleting elements
  
  L[1:1] = [2, 3, 4, 5]  # Inserting elements
  
  L[len(L):] = [10, 11]  # Appending
  
  L = L + [20, 30]
  
  L[0:0] = range(-3, 0)  # Prepending
  ```

### 10.3 Dict Mutation

- add key-values: `users["profpamela"] = "b3stp@ssEvErDontHackMe"`

### 10.4 Tuples

#### def

A **tuple** is an *immutable* sequence. It's like a list, but no mutation allowed.

```python
# an empty tuple
empty = ()
# or
empty = tuple()

# A tuple with multiple elements:
conditions = ('rain', 'shine')
# or
conditions = 'rain', 'shine'

# A tuple with a single element
oogly = (61,)
# or
oogly = 61,
```

#### Operations

Many of list's read-only operations work on tuples.

```python
('come', '☂') + ('or', '☼')  # ('come', '☂', 'or', '☼')

'wally' in ('wall-e', 'wallace', 'waldo')  # True

rainbow = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
roy = rainbow[:3]  # ('red', 'orange', 'yellow')
```

### 10.5 Immutability vs. Mutability

An **immutable** value is unchanging once created.

- Immutable types (part): int, float, string, tuple.

  ```python
  a_tuple = (1, 2)
  a_tuple[0] = 3                  # 🚫 Error! Tuple items cannot be set.
  a_string = "Hi y'all"
  a_string[1] = "I"               # 🚫 Error! String elements cannot be set.
  ```

- Mutable types (part): list, dict.

#### Name change vs. mutation

The value of an expression can change due to either changes in names *or* mutations in objects.

#### Mutables inside immutables

An immutable sequence may still change if it contains a mutable value as an element.

```python
t = (1, [2, 3])
t[1][0] = 99
t[1][1] = "Problems"
```

#### Equality of contents vs. Identity of objects

```python
list1 = [1,2,3]
list2 = [1,2,3]
```

**Equality**: `exp0 == exp1`
evaluates to `True` if both `exp0` and `exp1` evaluate to objects containing equal values

```python
list1 == list2  # True
```

**Identity**: `exp0 is exp1`
evaluates to `True` if both `exp0` and `exp1` evaluate to the same object Identical objects always have equal values.

```python
list1 is list2  # False
```

### 10.6 Mutation in function calls

**A function can change the value of any object in its scope.**

```python
def do_stuff_to(four):
	# What can we put here?
	four[0] += 1'
    
four = [1, 2, 3, 4]
print(four[0]) # 1
do_stuff_to(four)
print(four[0]) # 2
```

even without arguments

```
def do_other_stuff():
	four[3] = 99

four = [1, 2, 3, 4]
print(four[3]) # 4
do_other_stuff()
print(four[3]) # 99
```

### 10.7 Immutability in function calls

Immutable values are protected from mutation.

### 10.8 Mutable default arguments

A default argument value is part of a function value, *not* generated by a call.

```python
def f(s=[]):
    s.append(3)
    return len(s)

f() # 1
f() # 2
f() # 3
```

Each time the function is called, `s` is bound to the same value.

<img src=".\assets\week3\mutable-default-arguments.png" alt="lambda" style="zoom:50%;" />

## 11. OOP





















