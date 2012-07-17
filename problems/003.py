#! /usr/bin/python

import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0: return False
    return True

def foo(num):
    for i in reversed(range(int(math.sqrt(num)))):
        if num % i == 0 and is_prime(i):
            return i

def main():
    print foo(600851475143)

if __name__ == '__main__':
    main()
