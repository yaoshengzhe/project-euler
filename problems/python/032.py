#! /usr/bin/python

import itertools

def tuple2num(t):
    num = 0
    for i in t:
        num = 10 * num + i
    return num

def partition_number(remained_num, k):
    for a in itertools.permutations(remained_num, k):
        possible_b = remained_num - set(a)
        for b in itertools.permutations(possible_b):
            yield tuple2num(a), tuple2num(b)

def foo():
    # from analysis, c must be a 4-digit number
    # and if we let a <= b, then a, b will in ((1, 4), (2, 3))
    num_set = set(range(1, 10))
    result = 0
    for c in itertools.permutations(num_set, 4):
        remained_num = num_set - set(c)
        c = tuple2num(c)
        for a, b in itertools.chain(partition_number(remained_num, 1), partition_number(remained_num, 2)):

            if a * b == c:
                print '%d * %d = % d' % (a, b, c)
                result += c
                break

    return result

def main():
    print foo()

if __name__ == '__main__':
    main()
