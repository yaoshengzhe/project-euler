#! /usr/bin/python

import itertools

from util.prime import is_prime

def foo():

    for n in reversed(range(1, 10)):
        digit_coll = reversed([str(i) for i in range(1, n+1)])
        for i in itertools.permutations(digit_coll, n):
            num = int(''.join(i))
            if is_prime(num):
                return num

def main():
    print foo()

if __name__ == '__main__':
    main()
