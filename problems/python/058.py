#! /usr/bin/python

from util.prime import is_prime

def foo():
    n = 3
    total_num = 5
    prime_num = 0

    while True:

        bottom_left = n**2 - n + 1
        upper_left = bottom_left - n + 1
        upper_right = upper_left - n + 1

        if is_prime(bottom_left):
            prime_num += 1

        if is_prime(upper_left):
            prime_num += 1

        if is_prime(upper_right):
            prime_num += 1

        if (prime_num * 1.0) / total_num < 0.1:
            break
        n += 2
        total_num += 4
    return n

def main():
    print foo()

if __name__ == '__main__':
    main()
