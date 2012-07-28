#! /usr/bin/python

from util.prime import is_prime

def foo():
    n = 2

    while True:
        odd_num = 2*n - 1
        if is_prime(odd_num):
            n += 1
            continue
        i = 1
        twice_a_square = 2 * (i**2)
        while odd_num > twice_a_square:
            if is_prime(odd_num - twice_a_square):
                break
            else:
                i += 1
                twice_a_square = 2 * (i**2)

        if odd_num <= twice_a_square:
            return odd_num
        else:
            n += 1

def main():
    print foo()

if __name__ == '__main__':
    main()
