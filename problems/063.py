#! /usr/bin/python

from util.prime import is_prime

import itertools

# suppose x is n digit num, then 10^(n-1) <= x < 10^n
# assume x = y^n, then 10^(n-1) < y^n < 10^n
# since y is an integer, therefore 1 <= y <= 9
# also observe max number of y is 9
# therefore 9^n >= 10^(n-1), which means maximum value of right side
# should at least larger than smallest x
# which infers (10/9)^(n-1) <= 9 => n <= (log9)/log(10/9) + 1
# we get 1<= n <= 21
def foo():
    count = 0
    for n in range(1, 22):
        for y in range(1, 10):
            if len(str(y ** n)) == n:
                count += 1
    return count

def main():
    print foo()

if __name__ == '__main__':
    main()
