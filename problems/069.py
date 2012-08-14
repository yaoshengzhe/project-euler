#! /usr/bin/python

from util.prime import is_prime

def find_prime_factor(num):
    prime_factor_table = set()
    for i in range(2, num + 1):
        while num % i == 0:
            num = num / i
            prime_factor_table.add(i)
        if num == 1:
            break
    return prime_factor_table

def main():
    cache = {}
    max_ratio = 1
    n_max = 1000000

    prime_coll = []
    max_val = 1
    for n in range(2, n_max+1):

        if not is_prime(n):
            continue

        max_val *= n
        if max_val > n_max:
            break

        prime_coll.append(n)

    a = 1
    for i in prime_coll:
        a *= i

    print a

if __name__ == '__main__':
    main()
