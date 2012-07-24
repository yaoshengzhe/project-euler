#! /usr/bin/python

import math

def find_prime_factor(num):
    prime_factor_table = {}
    for i in range(2, num + 1):
        while num % i == 0:
            num = num / i
            prime_factor_table[i] = prime_factor_table.get(i, 0) + 1
        if num == 1:
            break
    return prime_factor_table

def foo():
    result = set()
    # represent a^b to (b * log a)
    upper_bound = 100
    prime_factor_cache = {}

    for a in range(2, upper_bound+1):
        for b in range(2, upper_bound+1):
            if a not in prime_factor_cache:
                prime_factor_cache[a] = find_prime_factor(a)

            prime_factor_for_a = prime_factor_cache[a]

            sig_list = [0 for i in range(upper_bound)]

            for key, freq in prime_factor_for_a.items():
                sig_list[key] = b * freq

            result.add(tuple(sig_list))

    return len(result)

def main():
    print foo()

if __name__ == '__main__':
    main()
