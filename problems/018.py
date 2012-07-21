#! /usr/bin/python

import sys

def get_max(triangle, level, i):
    if len(triangle[level]) <= i:
        return -1
    else:
        return triangle[level][i]

def foo():
    triangle = [ [int(num) for num in line.split()] for line in sys.stdin.readlines() ]
    for level in range(len(triangle)-1):
        for i in range(len(triangle[level])):
            if i == 0:
                triangle[level+1][i] = get_max(triangle, level, i) + triangle[level+1][i]

            max_val = max(get_max(triangle, level, i), get_max(triangle, level, i+1))

            triangle[level+1][i+1] = max_val + triangle[level+1][i+1]

    print triangle[len(triangle)-1]
    return max(triangle[len(triangle)-1])

def main():
    print foo()

if __name__ == '__main__':
    main()
