#! /usr/bin/python

import sys

def main():
    lower, upper = 0, 50
    count = upper * upper

    count2 = 0
    for x in range(lower, upper+1):
        for y in range(lower, upper+1):
            if x == 0 and y == 0:
                continue
            a, b = x, y
            c = x**2 + y**2
            for z in range(lower, upper+1):
                t = c - a*z
                if t < 0:
                    break

                if b == 0 and t == 0:
                    count2 += upper
                    for j in range(0, upper+1):
                        print (x, y), (z, j)
                elif b > 0 and (t % b == 0) and t / b <= upper:
                    if (x, y) != (z, t/b):
                        count2 += 1
                        print (x, y), (z, t / b)
    print count + count2

if __name__ == '__main__':
    main()
