#! /usr/bin/python

from util.prime import is_prime

import itertools


def foo():
    n = 406
    table = {}
    digit_size = len(str(n**3))

    while True:
        val = n ** 3
        if len(str(val)) > digit_size:
            for v in sorted(table.values()):
                if len(v) == 5:
                    print v
                    return v[0]

            digit_size = len(str(val))
            table = {}
        sig = ''.join(sorted(str(val)))
        table[sig] = table.get(sig, [])
        table[sig].append(val)

        n += 1

def main():
    print foo()

if __name__ == '__main__':
    main()
