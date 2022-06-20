# 1. Lexical vs. dynamic scopes

## 1.1 Lexical scope

The standard way in which names are looked up in Scheme and Python.

Lexical (static) scope: The parent of a frame is the frame in which a procedure was defined

``` scheme
(define f (lambda (x) (+ x y)))
(define g (lambda (x y) (f (+ x x))))
(g 3 7) ; Error: unknown identifier: y
```

<img src=".\assets\week4\examplescope.png" alt="examplescope" style="zoom:33%;" />

## 1.2 Dynamic scope

An alternate approach to scoping supported by some languages.

***Dynamic scope***: The parent of a frame is the frame in which a procedure was ***called***

Scheme includes the `mu` special form for dynamic scoping.

``` scheme
(define f (mu (x) (+ x y)))
(define g (lambda (x y) (f (+ x x))))
(g 3 7) ; 13
```

<img src=".\assets\week4\dynamicscope.png" alt="dynamicscope" style="zoom:33%;" />


# 2. Recursion efficiency

## 2.1 Recursion in Scheme

In Scheme interpreters, a ***tail-recursive*** function should only require a ***constant*** number of active frames.


# 3. Tail recursive functions

In a tail recursive function, every recursive call must be a tail call.

If a recursive call is the "last" (***doesn't mean it's the last statement of the whole function***) statement that runs and its returned value is not a part of an expression, the call is a tail call.  

Some compilers will ***overwrites the current frame instead of pushing a new one onto the stack***. (c, java compiler doesn't support this feature)

# 4. Tail call optimization

## 4.1 Thunk

Thunk: An expression wrapped in an ***argument-less*** function.

``` python 
# e.g
thunk1 = lambda: 2 * (3 + 4)
thunk2 = lambda: add(2, 4)
```

## 4.2 Trampolining

Trampoline: A loop that iteratively invokes thunk-returning functions.

``` python
def trampoline(f, *args):
    v = f(*args)
    while callable(v):
        v = v()
    return v

def factorial_thunked(n, k):
    if n == 0:
        return k
    else:
        return lambda: factorial_thunked(n - 1, k * n)

trampoline(factorial_thunked, 3, 1)
```


