#! /usr/bin/python

import math
def foo():
    return sum([int(ch) for ch in str(math.factorial(100))])

def main():
    print foo()

if __name__ == '__main__':
    main()
