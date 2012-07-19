#! /usr/bin/python

import math

def is_prime(num):
    if num < 2: return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def foo(num):
    if num < 1: return -1

    i = 2
    while True:
        if is_prime(i):
            num = num - 1
            if num == 0:
                return i
        i += 1

def main():
    print foo(10001)

if __name__ == '__main__':
    main()
