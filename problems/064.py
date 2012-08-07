#! /usr/bin/python

from util.prime import is_prime

import itertools
import fractions
import math

def is_perfect_square(n):
    val = int(math.sqrt(n))
    return n - val ** 2 < 1e-6

# let a(n) + (sqrt(N) + x) / y
# then x' = -x, y' = ((N-x^2) / y) and a(n+1) = (sqrt(N) + x') / y'
# and remains = (sqrt(N) - x' - a(n+1) *y') / y'
def foo():
    count = 0
    for n in range(2, 10001):
        if is_perfect_square(n):
            continue
        print n
        history_table = []
        square_of_n = math.sqrt(n)
        x, y = fractions.Fraction(-int(square_of_n)), fractions.Fraction(1)
        history_table.append((x, y))
        a = [-x]
        while True:
            y = fractions.Fraction(n - x**2, y)
            next_a = int((square_of_n - x) / y)
            x =  -x - next_a * y
            a.append(next_a)
            if history_table[0] == (x, y):
                break
            else:
                history_table.append((x, y))

        if len(a) % 2 == 0:
            count += 1

    return count

def main():
    print foo()

if __name__ == '__main__':
    main()
