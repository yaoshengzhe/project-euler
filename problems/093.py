#! /usr/bin/python

import sys
import itertools
import math

def compute(seq):
    if len(seq) == 1:
        d = int(seq[0])
        if seq[0] - d < 1e-6:
            yield d

    elif len(seq) > 1:
        for s in itertools.permutations(seq, len(seq)):
            c = list(s)
            d = c[2:]
            d.insert(0, c[0] + c[1])
            for i in compute(d):
                yield i

            d = c[2:]
            d.insert(0, c[0] - c[1])
            for i in compute(d):
                yield i

            d = c[2:]
            d.insert(0, c[0] * c[1])
            for i in compute(d):
                yield i

            if c[1] != 0:
                d = c[2:]
                d.insert(0, float(c[0]) / c[1])
                for i in compute(d):
                    yield i

    else:
        yield None

def gen_target_set(a, b, c, d):
    target_set = set()
    for num in compute([a, b, c, d][:]):
        target_set.add(num)
    return target_set

def longest_n(target_set):
    i = 1
    while True:
        if i not in target_set:
            return i-1
        else:
            i += 1

def main():
    max_n = 0
    selected_num = []
    for a in range(7):
        for b in range(a+1, 8):
            for c in range(b+1, 9):
                for d in range(c+1, 10):
                    n = longest_n(gen_target_set(a, b, c, d))
                    if n > max_n:
                        selected_num = [a, b, c, d]
                        max_n = n
                        # print max_n, selected_num
    print max_n, selected_num
    print ''.join([str(i) for i in selected_num])

if __name__ == '__main__':
    main()
