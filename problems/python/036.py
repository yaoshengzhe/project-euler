#! /usr/bin/python

import math

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

def foo():
    return sum([num for num in range(1000000) if is_palindrome(num) and is_palindrome(bin(num)[2:])])

def main():
    print foo()

if __name__ == '__main__':
    main()
