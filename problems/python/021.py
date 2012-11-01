#! /usr/bin/python

import math

amicable_number_cache = {}

def find_all_proper_divisors(num):
    divisor_set = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisor_set.add(i)
            if i > 1:
                divisor_set.add(num / i)

    return divisor_set

def is_amicable_number(num):
    if num in amicable_number_cache:
        return amicable_number_cache[num]

    sum_of_all_divisors = sum(find_all_proper_divisors(num))
    if sum_of_all_divisors != num and sum(find_all_proper_divisors(sum_of_all_divisors)) == num:
        amicable_number_cache[num] = True
        amicable_number_cache[sum_of_all_divisors] = True
    else:
        amicable_number_cache[num] = False
    return amicable_number_cache[num]

def foo():
    return sum([i for i in range(1, 10000 + 1) if is_amicable_number(i)])

def main():
    print foo()

if __name__ == '__main__':
    main()
