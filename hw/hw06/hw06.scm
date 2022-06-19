(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (ascending? lst) (cond ((null? lst) #t) ((null? (cdr lst)) #t) (else (if (> (car lst) (cadr lst)) #f (ascending? (cdr lst))))))

(define (interleave lst1 lst2) (cond 
    ((and (not (null? lst1)) (not (null? lst2))) (append (cons (car lst1) (cons (car lst2) nil)) (interleave (cdr lst1) (cdr lst2))) )  
    ((null? lst1) lst2) 
    ((null? lst2) lst1)
    ))

(define (my-filter func lst) (cond
    ((null? lst) nil)
    ((func (car lst)) (append (cons (car lst) nil) (my-filter func (cdr lst))))
    (else (my-filter func (cdr lst)))
    ))

(define (no-repeats lst) (cond
    ((null? lst) nil)
    (else (append (cons (car lst) nil) (no-repeats (my-filter (lambda (x) (not (= (car lst) x))) (cdr lst)))))
    ))