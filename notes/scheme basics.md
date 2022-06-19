# 1. Scheme expressions

- Primitive expressions: `2 3.3 #t #f + quotient`
- Combinations: `(quotient 10 2) (not #t)`

Combinations are either a call expression or a special form.

## 1.1 Call expressions

Call expressions include an operator and 0 or more operands in parentheses:

``` scheme
> (quotient 10 2)
5
> (quotient (+ 8 7) 5)
3
> (+ (* 3
        (+ (* 2 4)
           (+ 3 5)))
     (+ (- 10 7)
        6))
```

### Arithmetic Operations
- `+`: Returns the sum of all `num`s. Returns `0` if there are none.
``` scheme
(+ [num] ...)
```
- `-`: If there is only one num, return its negation. Otherwise, return the first num minus the sum of the remaining `num`s.
``` scheme
(- <num> ...)
```
- `*`: Returns the product of all nums. Returns 1 if there are none.
``` scheme
(* [num] ...)
```
- `\`: If there are no divisors, return 1 divided by dividend. Otherwise, return dividend divided by the product of the divisors. (Similar to python: `\`)
``` scheme
(/ <dividend> [divisor] ...)
```
- others:
``` scheme
(abs <num>)

(expt <base> <power>)

(modulo <a> <b>)

(quotient <dividend> <divisor>) ; in python : //

(remainder <dividend> <divisor>) ; Differs from modulo in behavior when negative numbers are involved.
```

### Boolean procedures (For Numbers)

except for `>=, <=, <, >, =`, scheme has:
``` scheme
even?	(even? 2)

odd?	(odd? 3)

zero?	(zero? 0) (zero? 0.0)
```

### Boolean procedures (For All data types)

``` scheme
(eq? #t #t)

(not #f)
```

***The only falsey value in Scheme is `#f`, all other values are truthy.*** 

## 1.2 Special forms

A combination that is not a call expression is a special form:

``` scheme
(if <predicate> <consequent> <alternative>) ; If true, the consequent is evaluated and returned.

(define x 5)
(if (zero? x)
    0
    (/ 100 x))

(and <e1> ... <en>) ; returning the first false value. If no e is false, return the last e. If no arguments are provided, return #t.

(define x 15)
(and (> x 10) (< x 20))

(or <e1> ... <en>)

(define <symbol> <expression>)

(define (<symbol> <formal parameters>) <body>)
```
- define procedures: Constructs a new procedure with params as its parameters and the body expressions as its body and binds it to name in the current environment. name must be a valid Scheme symbol. Each param must be a unique valid Scheme symbol.

``` scheme
(define (double x) (* 2 x) )
```

### Cond form

``` python
if x > 10:
    print('big')
elif x > 5:
    print('medium')
else:
    print('small')
```

```scheme
(cond ((> x 10) (print 'big))
    ((> x 5) (print 'medium))
    (else (print 'small)))

# another expression:

(print (cond ((> x 10) 'big)
    ((> x 5) 'medium)
    (else 'small)))
```
### Begin form
``` python
if x > 10:
    print('big')
    print('pie')
else:
    print('small')
    print('fry')
```

``` scheme
(cond ((> x 10) (begin (print 'big) (print 'pie)))
       (else (begin (print 'small) (print 'fry))))
```

### let form

The let special form binds symbols to values temporarily; ***just for one expression***

``` python
a = 3
b = 2 + 2
c = math.sqrt(a * a + b * b)
```
⬆️ a and b are still bound down here
``` scheme
(define c (let ((a 3)
    (b (+ 2 2)))
    (sqrt (+ (* a a) (* b b)))))
```
⬆️ a and b are not bound down here

### lambda expression

``` scheme
(lambda ([param] ...) <body> ...)

(define plus4 (lambda (x) (+ x 4)))
```


# 2. Scheme lists

Scheme lists are linked lists.

Scheme (with the cons form:)
``` scheme
(cons 1 (cons 2 nil))
```
- `nil` is the empty list.

``` scheme
(cons 1 (cons 2 (cons 3 (cons 4 nil))))   ; (1 2 3 4)

(define lst (cons 1 (cons 2 nil)))
(car lst)  ; 1
(cdr lst)  ; (2)
```
- `car`: Procedure that returns the first element of a list
- `cdr`: Procedure that returns the rest of the list

## 2.1 The list procedure

The built-in list procedure takes in an arbitrary number of arguments and constructs a list with the values of these arguments:

``` scheme
(list 1 2 3)                       ; (1 2 3)
(list 1 (list 2 3) 4)              ; (1 (2 3) 4)
(list (cons 1 (cons 2 nil)) 3 4)   ; ((1 2) 3 4)
```

## 2.2 Quotation

Quotation is used to refer to symbols directly:

``` scheme
(define a 1)
(define b 2)
(list a b)    ; (1 2)

(list 'a 'b)  ; (a b)
(list 'a b)   ; (a 2)
```
## 2.3 Quoting lists

```scheme
'(a b c)       ; (a b c)
(car '(a b c)) ; a
(cdr '(a b c)) ; (b c)
```

## 2.4 List procedures

### length
``` scheme
(length '(1 2))   ; 2
(length '())      ; 0
(length nil)      ; 0
(length 123)      ; Error!
```

### null?
```scheme
(null? '())      ; #t
(null? nil)      ; #t
(null? '(1 2))   ; #f
(null? 123)      ; #f
```

### append
``` scheme
(append '(1 2) '(3 4))         ; (1 2 3 4)
(append '(1 2) '(3 4) '(5 6))  ; (1 2 3 4 5 6)
```

### map

`(map <proc> <lst>)`returns a new list created by applying proc to each item in lst

``` scheme
(map abs '(-1 -2 3 4))   ; (1 2 3 4)
(map - '(1 2))           ; (-1 -2)
```

### filter

`(filter <pred> <lst>)` returns a new list consisting only of elements of lst for which pred is true.

``` scheme
(filter even? '(0 1 2 3 4 5))   ; (0 2 4)
(filter odd? '(0 1 2 3 4 5))    ; (1 3 5)
```

### reduce

`(reduce <combiner> <lst>)` returns the result of sequentially combining each element in lst using combiner (a two-arg procedure).

``` scheme
(reduce + '(1 2 3 4 5))         ; (15)
(reduce expt '(1 2 3 4 5))      ; (1)
(reduce expt '(2 3 4 5))        ; (1152921504606846976)
```

### list equality

``` scheme
(define list1 '(a b c))
(define list2 '(a b c))

; For lists, (eq? a b) returns whether a and b are the same list in memory.

(eq? list1 list2)  ; #f

; While (equal? a b) returns whether a and b are equivalent. Two lists are considered equivalent if (car a) is equivalent to (car b) and (cdr a) is equivalent to (cdr b).

(equal? list1 list2)  ; #t
```

# 3. Parsing Scheme

***Parsing***: turning a string representation of an expression into a structured object representing the expression.

<img src=".\assets\week4\parser.png" alt="parser" style="zoom:33%;" />

## 3.1 Lexical analysis
- Iterative process
- Checks for malformed tokens
- Determines types of tokens
- Processes one line at a time

## 3.2 Syntactic analysis
- Tree-recursive process
- Balances parentheses
- Returns tree structure
- Processes multiple lines

## 3.3 Pair Class
The Pair class represents Scheme lists.
``` python
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

# Well-formed list: (second element is either a pair or nil)
s = Pair(1, Pair(2, Pair(3, nil)))
print(s)  # (1 2 3)
len(s)    # 3

# improperly-formed list
print(Pair(1, 2))          # (1 . 2)
print(Pair(1, Pair(2, 3))) # (1 2 . 3)
len(Pair(1, Pair(2, 3)))   # Error!
```

# 4. The Calculator Language

A programming language has:
- Syntax: The legal statements and expressions in the language
- Semantics: The execution/evaluation rule for those statements and expressions

To create a new programming language, you need either one of these:

- Specification: A document describing the precise syntax and semantics of the language
- Canonical Implementation: An interpreter or compiler for the language

## 4.1 Calculator language syntax

<img src=".\assets\week4\caculator-syntax.png" alt="caculator-syntax" style="zoom:33%;" />

## 4.2 Calculator language semantics

The value of a calculator expression is defined recursively.

- ***Primitive***: A number evaluates to itself.
- ***Call***: A call expression evaluates to its argument values combined by an operator.

## 4.3 Evaluating Calculator

***Evaluation***: Turning a structured representation of a program into the expected program output according to the language semantics.

### The eval function

The eval function computes the value of an expression.

It is a generic function that behaves according to the type of the expression (primitive or call).

``` python
def calc_eval(exp):
    if isinstance(exp, (int, float)):
        return exp
    elif isinstance(exp, Pair):
        arguments = exp.second.map(calc_eval)
        return calc_apply(exp.first, arguments)
    else:
        raise TypeError
```

### Applying built-in operators

The apply function applies some operation to a (Scheme) list of argument values

In calculator, all operations are named by built-in operators: `+, -, *, /`

``` python
def calc_apply(operator, args):
    if operator == '+':
        return reduce(add, args, 0)
    elif operator == '-':
        ...
    elif operator == '*':
        ...
    elif operator == '/':
        ...
    else:
        raise TypeError
```

### Raising exceptions

Exceptions can be raised during lexical analysis, syntactic analysis, eval, and apply.

examples:

- ***Lexical analysis***: The token `2.3.4` raises `ValueError("invalid numeral")`
- ***Syntactic analysis***: An extra `')' `raises `SyntaxError("unexpected token")`
- ***Eval***: An empty combination raises `TypeError("() is not a number or call expression")`
- ***Apply***: No arguments to `-` raises` TypeError("- requires at least 1 argument")`

