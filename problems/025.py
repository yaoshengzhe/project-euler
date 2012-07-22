#! /usr/bin/python

import math

def foo():
    a, b = 1, 1
    n = 3
    while True:
        c = a + b

        if math.ceil(math.log10(c)) >= 1000:
            return n
        a, b = b, c
        n += 1

def main():
    print foo()

if __name__ == '__main__':
    main()
