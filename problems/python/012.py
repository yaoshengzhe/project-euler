#! /usr/bin/python

import math

def find_all_divisors(num):
    divisor_set = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisor_set.add(i)
            divisor_set.add(num / i)

    return divisor_set

def find_all_divisors_for_ith_triangle_num(i):
    return find_all_divisors(i*(i+1) / 2)

def find_low_bound(bound, target):
    start = bound[0]
    end = bound[1]

    for i in range(start, end):
        print i
        if len(find_all_divisors_for_ith_triangle_num(i)) == target:
            return i

def foo():
    n = 10
    target = 500

    while True:
        val = len(find_all_divisors_for_ith_triangle_num(n))

        print n, n*(n+1)/2, val
        if val > target:
            return n
        n += 1

def main():
    print foo()

if __name__ == '__main__':
    main()
