#! /usr/bin/python

import fractions

def foo():

    count = 0
    x = fractions.Fraction(1, 1)
    for i in range(1000):
        x = 1/(2 + x - 1) + 1
        if len(str(x.numerator)) > len(str(x.denominator)):
            count += 1
    return count

def main():
    print foo()

if __name__ == '__main__':
    main()
