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

