#! /usr/bin/python

import math
from util.prime import is_prime

def gcd(x, y):
    if x == 0:
        return y

    r = y % x
    return gcd(r, x)

# initial guess to 2/5 and reduce search space for each iteration
def main():
    lower, upper = (1, 3), (1, 2)
    count = 0
    for d in range(2, 12001):
        start, end = int(d*float(lower[0])/lower[1])+1, int(math.ceil(d*float(upper[0])/upper[1]))
        for n in range(start, end):
            if gcd(n, d) == 1:
                count += 1
        print d
    print count

if __name__ == '__main__':
    main()
