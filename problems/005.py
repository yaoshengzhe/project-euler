#! /usr/bin/python

import math

factor_cache = {}

def multiple(hash):
    result = 1
    for key, val in hash.items():
        for i in range(val):
            result = result * key
    return result

def prime_factor(num):
    if num in factor_cache:
        return factor_cache[num]

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            result = [i]
            result.extend( prime_factor(num/i) )
            factor_cache[num] = result
            return result
    factor_cache[num] = [num]
    return [num]

def foo():
    global_prime_factor_coll = {}
    for i in range(2, 21):
        prime_factor_coll = {}
        for i in prime_factor(i):
            prime_factor_coll[i] = prime_factor_coll.get(i, 0) + 1
        for key, val in prime_factor_coll.items():
            if global_prime_factor_coll.get(key, -1) < val:
                global_prime_factor_coll[key] = val

    return multiple(global_prime_factor_coll)

def main():
    print foo()

if __name__ == '__main__':
    main()
