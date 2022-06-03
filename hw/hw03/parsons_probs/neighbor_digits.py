def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    if num == 0:
        return 0
    cur_digit = num % 10
    next_digit = (num // 10) % 10
    if cur_digit == prev_digit or cur_digit == next_digit:
        return 1 + neighbor_digits(num // 10, cur_digit)
    else:
        return neighbor_digits(num // 10, cur_digit)
        
