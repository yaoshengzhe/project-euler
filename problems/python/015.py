#! /usr/bin/python

import math
def foo():
    a = math.factorial(20)
    return math.factorial(40) / a / a
def main():
    print foo()

if __name__ == '__main__':
    main()
