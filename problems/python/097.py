#! /usr/bin/python

import sys
import copy
import itertools
import math
import operator
from termcolor import colored

# 28433 * 2 ** 7830457 + 1

def last_10(num):
    if len(str(num)) < 10:
        return num
    else:
        return int(str(num)[-10:])

def find_last_10digit(exp):
    if exp < 60:
        return last_10(2**exp)
    elif exp % 2 == 0:
        x = find_last_10digit(exp/2)
        return last_10(x * x)
    else:
        x = find_last_10digit(exp/2)
        return last_10(x * x * 2)

def main():
    print last_10(28433 * find_last_10digit(7830457) + 1)

if __name__ == '__main__':
    main()
