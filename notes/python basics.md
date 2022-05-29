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

#### 3.2.1  Default arguments

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

#### 3.2.2 Multiple return values

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

#### 3.2.3 Function name as a variable

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

### Short circuiting

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

#### 3.5.1 While loops

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

#### 4.3.1 definition

A function that either:

- Takes another function as an argument
- Returns a function as its result

All other functions are considered first-order functions.

#### 4.3.2 [Functions as arguments](#3.2.3 Function name as a variable)

#### 4.3.3 Functions as return values

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

#### 4.4.1 Def statements vs. Lambda expressions

![lambda](.\assets\week2\lambda.png)

| Both create a function with the same domain, range, and behavior. |
| ------------------------------------------------------------ |
| Both bind that function to the name "square".                |
| Only the `def` statement gives the function an **intrinsic name**, which shows up in environment diagrams but doesn't affect execution (unless the function is printed). |

#### 4.4.2 Lambda as argument

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

Also, *args can be used to forward a HOF.


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

Local names are *not* visible to other (non-nested) functions.

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













