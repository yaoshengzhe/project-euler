#! /usr/bin/python

import math

cache = {}
def find_next(n):
    if n not in cache:
        cache[n] = sum([math.factorial(int(ch)) for ch in str(n)])
    return cache[n]

def find_chain(n):
    s = set([n])
    while True:
        n = find_next(n)
        if n in s:
            return s
        s.add(n)

def main():
    count = 0
    for n in range(1, 1000000+1):
        if len(find_chain(n)) == 60:
            count += 1
        print n
    print count

if __name__ == '__main__':
    main()
