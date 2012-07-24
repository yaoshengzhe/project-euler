#! /usr/bin/python

import fractions

def get_nth_digit(num, n):
    return int(str(num)[n-1])

def get_all_possible_digit_pair(a, b):
    for i in range(2):
        for j in range(2):
            if get_nth_digit(a, i+1) == get_nth_digit(b, j+1):
                yield get_nth_digit(a, 2 - i), get_nth_digit(b, 2 - j)

def foo():
    result = fractions.Fraction(1)
    for b in range(11, 100):
        if b % 10 == 0:
            continue
        for a in range(11, b):
            for a_star, b_star in get_all_possible_digit_pair(a, b):
                if a * b_star == a_star * b:
                    result = result * fractions.Fraction(a, b)

                    return result

def main():
    print foo()

if __name__ == '__main__':
    main()
