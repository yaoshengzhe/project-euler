#! /usr/bin/python

import math

def sum_of_digit(num, base):
    return sum([ int(i)**base for i in str(num)])

def find_upper_bound():
    n = 1
    while True:
        if 10**n > 9**5*n:
            return 9**5*n
        n += 1

def foo():
    return sum([i for i in range(2, find_upper_bound()+1) if sum_of_digit(i, 5) == i])

def main():
    print foo()

if __name__ == '__main__':
    main()
