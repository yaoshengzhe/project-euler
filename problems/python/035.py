#! /usr/bin/python

import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: return False
    return True

def is_circular_prime(num, cache):
    n = len(str(num))
    for i in range(1, n):
        q, r = num / 10, num % 10
        num = r * 10 **(n-1) + q
        if num not in cache:
            return False
    return True

def foo():
    prime_less_than_one_million = set([i for i in range(2, 1000000) if is_prime(i)])
    result = [i for i in prime_less_than_one_million if is_circular_prime(i, prime_less_than_one_million)]

    print result
    return len(result)

def main():
    print foo()

if __name__ == '__main__':
    main()
