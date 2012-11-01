#! /usr/bin/python

import math

def h(x):
    return x*(2*x-1)

# Suppose we have x(x+1)/2 = y(3y-1)/2 = z(2z-1)
# Then we can search solution by let z from 1 to inf
# Let C = z(2z-1)
# then x = (-1 sqrt(1+8C)) / 2
# and  y = (1 + sqrt(1+24C)) / 6
# find the solution that let x and y be positive integer
# the one after (285, 165, 143) is our solution
def foo():
    z = 1
    epsilon = 1e-6
    solution = []
    while True:
        c = h(z)
        for_x = math.sqrt(1+8*c) - 1
        for_y = math.sqrt(1+24*c) + 1
        if (for_x - int(for_x)) < epsilon and (for_y - int(for_y)) < epsilon:
            for_x, for_y = int(for_x), int(for_y)
            if for_x % 2 == 0 and for_y % 6 == 0:
                solution.append((for_x/2, for_y/6, z))
                if len(solution) > 1 and solution[-2] == (285, 165, 143):
                    return h(z)
        z += 1

def main():
    print foo()

if __name__ == '__main__':
    main()
