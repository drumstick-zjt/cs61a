def k_in_num(k, num):
    """
    Complete k_in_num, a function which returns True if num has the digit k and
    returns False if num does not have the digit k. 0 is considered to have no
    digits.

    >>> k_in_num(3, 123) # .Case 1
    True
    >>> k_in_num(2, 123) # .Case 2
    True
    >>> k_in_num(5, 123) # .Case 3
    False
    >>> k_in_num(0, 0) # .Case 4
    False
    """
    res = False
    if k == 0:
        res = False
    else:
        while num != 0:
            last_digit = num % 10
            if (last_digit == k):
                res = True
                break
            else:
                num = num // 10
    return res



    
    
