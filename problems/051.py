#! /usr/bin/python

import itertools

from util.prime import is_prime

def get_signiture(prime_num):

    prime_str = str(prime_num)
    signiture_coll = []
    for i in '0123456789':
        num_freq = prime_str.count(i)
        if num_freq > 0:
            idx_coll = [idx for idx in range(len(prime_str)) if prime_str[idx] == i]
            for idx_permutation in itertools.combinations(idx_coll, num_freq):
                prime_str_sig = list(prime_str)
                for j in idx_permutation:
                    prime_str_sig[j] = '*'
                signiture_coll.append(''.join(prime_str_sig))
    return signiture_coll

def foo():

    family_size = 8
    for num in (i for i in range(1000000)  if is_prime(i)):
        for sig in get_signiture(num):
            current_familiy_size = 0
            missed = 0
            first_prime_in_family = None

            for i in '0123456789':
                family_candidate = int(sig.replace('*', i))

                if len(str(family_candidate)) == len(sig) and is_prime(family_candidate):
                    current_familiy_size += 1
                    if first_prime_in_family is None:
                        first_prime_in_family = family_candidate
            if current_familiy_size == family_size:
                return first_prime_in_family

def main():
    print foo()

if __name__ == '__main__':
    main()
