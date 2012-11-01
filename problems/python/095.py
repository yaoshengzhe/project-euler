#! /usr/bin/python

import sys
import itertools
import math
import operator

def gen_factor_table(limit):
    if limit < 1:
        raise Exception("table size has to larger than 0." % (limit))
    factor_table = [0 for i in range(limit + 1)]
    for i in range(1, limit + 1):
        for j in range(2, limit / i + 1):
            factor_table[i*j] += i

    return factor_table

def main():

    LIMIT = 1000000

    factor_table = gen_factor_table(LIMIT)

    print 'factor table generated.'

    max_chain_size = 0
    max_chain_coll = []
    for i in range(1, LIMIT + 1):
        if factor_table[i] > LIMIT:
            #print "number: %d is at index %d is larger than limit: %d" % (factor_table[i], i, LIMIT)
            continue
        chain_coll = set([i])
        num = factor_table[i]
        while num not in chain_coll:
            chain_coll.add(num)
            num = factor_table[num]
            if num > LIMIT:
                chain_coll = set()
                break

        if num != i:
            continue

        if len(chain_coll) > max_chain_size:
            max_chain_size = len(chain_coll)
            max_chain_coll = chain_coll

    print max_chain_size
    print max_chain_coll
    print sorted(list(max_chain_coll))[0]

if __name__ == '__main__':
    main()
