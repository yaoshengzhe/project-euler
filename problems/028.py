#! /usr/bin/python

import math

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

def find_previous_num(val, n):
    return val - n + 1

def foo(n):
    if n < 1 or n % 2 == 0:
        raise Exception('Invalid number n = %d, n should be odd number (of course should be positive)' % (n))

    step = 2
    result = 1
    for num in range(3, n+1, step):
        upper_right = num ** 2

        upper_left = find_previous_num(upper_right, num)
        down_left = find_previous_num(upper_left, num)
        down_right = find_previous_num(down_left, num)
        result = result + upper_right + upper_left + down_left + down_right
    return result

def main():
    print foo(1001)

if __name__ == '__main__':
    main()
