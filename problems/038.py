#! /usr/bin/python

import itertools

def is_pandigital(s):
    return len(s) == 9 and ''.join(sorted(s)) == '123456789'

def test_n(num, n_upper_bound):
    candidate = []
    length = 0
    n_val = 0
    for n in range(1, n_upper_bound+1):
        if length >= 9:
            break
        val = str(num * n)
        length += len(val)
        candidate.append(val)
        n_val = n
    pandigital_num = ''.join(candidate)
    if is_pandigital(pandigital_num):
        return (pandigital_num, num, n_val)
    return ()

def max_pandigital_num(a, b):
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a

    if a[0] > b[0]:
        return a
    else:
        return b

def produce_num(digit):
    for p in itertools.permutations('12345678', digit-1):
        yield int('9'+''.join(p))

def foo():

    result = ()
    # only two-digit, three-digit and four-digit numbers are possible to be candidate
    # and n should <= 9
    for num in itertools.chain(produce_num(2), produce_num(3), produce_num(4)):
        r = test_n(num, 9)
        if len(r) > 0:
            result = max_pandigital_num(result, r)
    return result

def main():
    print foo()

if __name__ == '__main__':
    main()
