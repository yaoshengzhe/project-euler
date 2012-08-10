#! /usr/bin/python

import math

def is_perfect_square(n):
    val = int(math.sqrt(n))
    return n - val ** 2 < 1e-6

# triangle area = sqrt(b^2c^2 + b^2 + c^2) / 2

S = set([])
for i in range(0, 100):
    S.add((i*i) % 256)
print S
def get_integer_area(b_square, c_square):
    v = b_square * c_square + b_square + c_square
    if not (v % 256) in S:
        return 0
    if (is_perfect_square(v) and v % 2 == 0):
        return int(math.sqrt(v)) / 2
    return 0

def main():
    b = 1
    s = 0
    n = 10**6
    while True:
        b_square = b**2
        upper_bound = math.sqrt((4 * n**2 - b_square) / (1.0 + b_square))
        if b > int(upper_bound):
            break
        for c in range(b, int(upper_bound)+1):
            c_square = c**2
            v = get_integer_area(b_square, c_square)
            if v > n:
                break
            s += v
        b += 1
        print s
    print s

if __name__ == '__main__':
    main()
