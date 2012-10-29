#! /usr/bin/python

import sys
import copy
import itertools
import math
import operator
from termcolor import colored

def base_cmp(x, y):
    a, b = x
    c, d = y
    diff = b * math.log(a) - d * math.log(c)
    if math.fabs(diff) < 1e-6:
        return 0
    elif diff < 0:
        return -1
    else:
        return 1

def main():
    coll = [map(lambda x: int(x), line.strip().split(',')) for line in sys.stdin.readlines()]
    print coll.index(sorted(coll, base_cmp)[-1]) + 1

if __name__ == '__main__':
    main()
