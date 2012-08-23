#! /usr/bin/python

import math

def is_perfect_sqrt_root(n):
    return int(math.sqrt(n)) ** 2 == n

def main():
    M = 1
    count = 0

    while True:
        # c = i + j where i <= j
        for c in range(2, 2*M+1):
            shortest_path = c**2 + M**2
            if is_perfect_sqrt_root(shortest_path):
                count += c/2
                if c - M > 0:
                    count -= (c-M - 1)

        if count > 1000000:
            break
        print M, count
        M += 1
    print M, count

if __name__ == '__main__':
    main()
