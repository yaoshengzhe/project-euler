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
    candidate = (2, 5)
    target = 3.0/7
    for d in range(8, 1000001):
        start, end = int(d*float(candidate[0])/candidate[1])+1, int(math.ceil(d*target))
        for n in reversed(range(start, end)):
            if gcd(n, d) == 1:
                candidate = (n, d)
                break
    print candidate

if __name__ == '__main__':
    main()
