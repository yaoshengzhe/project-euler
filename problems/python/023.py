#! /usr/bin/python

import math

def find_all_divisors(num):
    divisor_set = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisor_set.add(i)
            if i > 1:
                divisor_set.add(num / i)

    return divisor_set

def is_abundant_number(num):
    return sum(find_all_divisors(num)) > num

def foo():
    abundant_num_coll = [ i for i in range(1, 28124) if is_abundant_number(i) ]

    abundant_num_set = set(abundant_num_coll)
    result = 0
    s = []
    for i in range(1, 28124):
        for j in abundant_num_coll:
            if i < 2 * j:
                result += i
                break
            elif i > j:
                val = i - j
                if val in abundant_num_set:
                    break
    return result

def main():
    print foo()

if __name__ == '__main__':
    main()
