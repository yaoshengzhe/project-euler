#! /usr/bin/python

from util.prime import is_prime

import itertools

def is_prime_set(prime_set):
    for prime_pair in itertools.permutations(prime_set, 2):
        if not is_prime(int(str(prime_pair[0]) + str(prime_pair[1]))):
            return False
    return True

def look_set(exist_set, num, prime_table):
    if prime_table.get(num, None) is None:
        return set()

    return set(prime_table[num]).intersection(exist_set)

def find_group(current_candidate_set, n, prime_table):

    if n == 1:
        for i in current_candidate_set:
            yield (i,)

    for num in current_candidate_set:
        if num not in prime_table:
            continue
        result = set(prime_table[num]).intersection(current_candidate_set)
        if len(result) >= (n-1):
            for i in find_group(result, n-1, prime_table):
                yield (num,) + i

def foo():
    prime_less_than_thousand = [i for i in range(10000) if str(i)[-1] in '1379' and is_prime(i)]
    prime_table = {}
    print 'loaded'
    for i in prime_less_than_thousand:
        for j in prime_less_than_thousand:
            if i >= j:
                continue
            if is_prime_set((i, j)):
                prime_table[i] = prime_table.get(i, [])
                prime_table[i].append(j)

    min_val = -1
    print 'start'
    n = 5
    for key, val in prime_table.items():
        if len(val) >= n-1:
            for g in find_group(set(val), n-1, prime_table):
                print (key,) + g, key + sum(g)
                if min_val == -1 or min_val > key + sum(g):
                    min_val = key + sum(g)
    return min_val

def main():
    print foo()

if __name__ == '__main__':
    main()
