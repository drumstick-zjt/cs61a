# Debugging Techniques

## 1. Running doctests

Python has a great way to quickly write tests for your code. These are called doctests, and look like this:

```python
def foo(x):
    """A random function.

    >>> foo(4)
    4
    >>> foo(5)
    5
    """
```

The lines in the docstring that look like interpreter outputs are the **doctests**. To run them, go to your terminal and type:

```shell
$ python3 -m doctest file.py
```

This effectively loads your file into the Python interpreter, and checks to see if each doctest input (e.g. `foo(4)`) is the same as the specified output (e.g. `4`). If it isn't, a message will tell you which doctests you failed.

The command line tool has a `-v` option that stands for *verbose*.

```shell
$ python3 -m doctest file.py -v
```

## 2. Writing your own tests

In addition to doctests, you can write your own tests. There are two ways to do this: (1) write additional doctests, or (2) write testing functions.

To write more doctests, simply follow the style of existing doctests. You can also write your own functions (much like the `take_turn_test` function from Project 1).

Some advice in writing tests:

- **Write some tests before you write code**: this is called test-driven development. Writing down how you expect the function to behave first -- this can guide you when writing the actual code.
- **Write more tests after you write code**: once you are sure your code passes the initial doctests, write some more tests to take care of edge cases.
- **Test edge cases**: make sure your code works for all special cases.

## 3. Using `print` statements

When you first learn how to program, it can be hard to spot bugs in your code. One common practice is to add `print` statements. For example, let's say the following function `foo` keeps returning the wrong thing:

We can add a print statement before the return to check what `some_function` is returning:

```python
def foo(x):
    result = some_function(x)
    print('DEBUG: result is', result)
    return other_function(result)
```

#### Long-term debugging

The `print` statements described above are meant for quick debugging of one-time errors -- after figuring out the error, you would remove all the `print` statements.

However, sometimes we would like to leave the debugging code if we need to periodically test our file. It can get kind of annoying if every time we run our file, debugging messages pop up. One way to avoid this is to use a global `debug` variable:

```python
debug = True

def foo(n):
i = 0
while i < n:
    i += func(i)
    if debug:
        print('DEBUG: i is', i)
```

Now, whenever we want to do some debugging, we can set the global `debug` variable to `True`, and when we don't want to see any debugging input, we can turn it to `False` (such a variable is called a "flag").

## 3. Interactive Debugging

One way a lot of programmers like to investigate their code is by use of an interactive REPL. That is, a terminal where you can directly run functions and inspect their outputs.

Typically, to accomplish this, you can run:

```shell
$ python -i file.py
```

and one then has a session of python where all the definitions of `file.py` have already been executed.

## 4. Using `assert` statements

Python has a feature known as an `assert` statement, which lets you test that a condition is true, and print an error message otherwise in a single line. This is useful if you know that certain conditions need to be true at certain points in your program. For example, if you are writing a function that takes in an integer and doubles it, it might be useful to ensure that your input is in fact an integer. You can then write the following code.

```python
def double(x):
    assert isinstance(x, int), "The input to double(x) must be an integer"
    return 2 * x
```

Note that we aren't really debugging the `double` function here, what we're doing is ensuring that anyone who calls `double` is doing so with the right arguments. For example, if we have a function `g` that takes in a string and a number and adds the length of the string to twice the number, and it is implemented like so:

```python
def g(x, y):
    return double(x) + y # should be double(y) + len(x)
```

Instead of getting a weird error about not being able to add a string and a number, we get a clean error that the argument to `double` must be an integer. This allows us to quickly narrow down the problem.

One *major* benefit of assert statements is that they are more than a debugging tool, **you can leave them in code permanantly.** **A key principle in software development is that it is generally better for code to crash than produce an incorrect result**, and having asserts in your code makes it far more likely that your code will crash if it has a bug in it.

