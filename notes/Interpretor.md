# 1. Special forms

## 1.1 Scheme evaluation

The scheme_eval function chooses behavior based on expression form
- Symbols are looked up in the current environment
- Self-evaluating expressions (booleans, numbers, nil) are returned as values
- All other legal expressions are represented as ***Scheme lists***, called combinations.
    - `(<operator> <operand 0> ... <operand k>)`

### Evaluating combinations

The special forms can all be identified by the first element:
``` scheme
(if <predicate> <consequent> <alternative>)
(lambda (<formal-parameters>) <body>)
(define <name> <expression>)
```

Any combination that is not a known special form must be a call expression.


# 2. Logical forms

Logical forms are special forms that may only evaluate some sub-expressions

- If expression: `(if <predicate> <consequent> <alternative>)`
- And and or: `(and <e1> ... <en>)`, `(or <e1> ... <en>)`
- Cond expression: `(cond (<p1> <e1>) ... (<pn> <en>) (else <e>))`

The value of an if expression is the value of a sub-expression:
- Evaluate the predicate
- Choose a sub-expression
- Evaluate that sub-expression to get the value of the whole expression

# 3. Quotation

- `'<expression>` is shorthand for `(quote <expression>)`
    - `'(1 2)` is equivalent to `(quote (1 2))`

The `scheme_read` parser converts `'` to a combination that starts with `quote`.

The quote special form evaluates to the quoted expression, ***which is not evaluated.***

e.g: `(quote (+ 1 2))` evaluates to the three-element Scheme list `(+ 1 2)`


# 4. Lambda expressions

## 4.1 Frames

A frame represents an environment by having a parent frame.

A frame is an instance of a `Frame` object, which has `lookup` and `define` methods.

## 4.2 Define expressions

Define binds a symbol to a value in the first frame of the current environment.

`(define <name> <expression>)`:

- Evaluate the `<expression>`
- Bind `<name>` to its value in the current frame

Procedure definition is shorthand of define with a lambda expression.

`(define (<name> <formal parameters>) <body>)`

`(define <name> (lambda (<formal parameters>) <body>))`

## 4.3 Lambda Expressions

Lambda expressions evaluate to user-defined procedures.

`(lambda (<formal-parameters>) <body> ... )`

``` python
class LambdaProcedure:
    def __init__(self, formals, body, env):
        self.formals = formals  # A scheme list of symbols
        self.body = body        # A scheme list of expressions
        self.env = env          # A Frame instance
```

## 4.4 Applying User-Defined Procedures

To apply a user-defined procedure, create a new frame in which formal parameters are bound to argument values, whose parent is the env attribute of the procedure.

Evaluate the body of the procedure in the environment that starts with this new frame.

``` scheme
(define (demo s)
    (if (null? s)
        '(3)
        (cons (car s) (demo (cdr s)))))
(demo (list 1 2))
```

