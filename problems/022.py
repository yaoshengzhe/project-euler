#! /usr/bin/python

import sys

def get_name_score(name):
    return sum([ord(ch) - ord('A') + 1 for ch in name if ch != '"'])

def foo():
    name_coll = sorted([name for line in sys.stdin.readlines() for name in line.split(',')])
    return sum([ (i+1) * get_name_score(name_coll[i]) for i in range(len(name_coll))])

def main():
    print foo()

if __name__ == '__main__':
    main()
