#! /usr/bin/python

import itertools

from util.prime import is_prime

def is_anagram(num_coll):

    if num_coll is None or len(num_coll) < 1:
        return True

    signiture = None
    for i in num_coll:
        sig = ''.join(sorted(str(i)))
        if signiture is None:
            signiture = sig
        elif signiture != sig:
            return False

    return True

def foo():

    candidate_coll = []
    for i in range(1000, 10000):
        num = int(i)
        if is_prime(num):
            candidate_coll.append(num)

    candidate_set = set(candidate_coll)

    for i in range(len(candidate_coll)):
        for j in range(i+1, len(candidate_coll)):
            x, y = candidate_coll[i], candidate_coll[j]
            z = y + y - x
            if z in candidate_set and is_anagram([x, y, z]) and (x, y, z) != (1487, 4817, 8147):
                print x, y, z
                return ''.join([str(x), str(y), str(z)])

def main():
    print foo()

if __name__ == '__main__':
    main()
