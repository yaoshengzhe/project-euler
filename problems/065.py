#! /usr/bin/python

from util.prime import is_prime

import itertools
import fractions
import math

def get_convergent_at(n):
    if n % 3 == 1:
        return 2 * (n / 3 + 1)
    else:
        return 1

def foo():
    val = -1
    n = 100
    for n in reversed(range(n-1)):
        if val == -1:
            val = fractions.Fraction(get_convergent_at(n))
        else:
            val = 1/val + get_convergent_at(n)

    val =  2 + 1/val
    return  sum([ int(ch) for ch in str(val.numerator)])

def main():
    print foo()

if __name__ == '__main__':
    main()
