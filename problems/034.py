#! /usr/bin/python

import math

def get_factorial_from_zero_to_nine():
    return [ math.factorial(i) for i in range(10)]

def sum_of_digit_factorial(num, factorial_cache):
    return sum([factorial_cache[int(digit)] for digit in str(num)])

def foo():
    factorial_cache = get_factorial_from_zero_to_nine()

    n = 1
    while True:
        if 10**n > factorial_cache[9]*n:
            break
        else:
            n += 1

    result = []

    for i in range(3, 10**(n-1)+1):
        if i == sum_of_digit_factorial(i, factorial_cache):
            print i
            result.append(i)
    print result
    return sum(result)

def main():
    print foo()

if __name__ == '__main__':
    main()
