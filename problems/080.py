#! /usr/bin/python

import decimal
import math
def main():
    digit_sum = 0
    n = 100
    num_coll = [i for i in range(n+1)]

    for i in range(2, int(math.sqrt(n))+1):
        num_coll[i*i] = -1

    for i in num_coll[2:]:
        if i == -1:
            continue
        if i*i < len(num_coll):
            num_coll[i*i] = -1
        sqrt_root = decimal.Decimal(i).sqrt(decimal.Context(prec=120))
        digit_sum += sum([int(d) for d in str(sqrt_root)[:101] if d.isdigit()])

    print digit_sum

if __name__ == '__main__':
    main()
