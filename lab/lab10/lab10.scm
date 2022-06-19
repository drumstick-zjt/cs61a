(define (over-or-under num1 num2) (cond ((< num1 num2) -1) ((= num1 num2) 0) (else 1)) )

(define (make-adder num) (lambda (inc) (+ num inc)))

(define (composed f g) (lambda (x) (f (g x))))

(define (square n) (* n n))

(define (pow base exp) (cond ((= exp 0) 1) ((= exp 1) base) (else (if (even? exp) (square (pow base (/ exp 2))) (* base (square (pow base (quotient exp 2))))))))
