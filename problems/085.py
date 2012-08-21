#! /usr/bin/python

import math

def main():
    m = 1
    t = 2000000
    candidate = None
    min_val = t
    while True:
        c = m * (m+1) / 2
        n_float = math.sqrt(t*2.0/c) - 0.5
        if c > t:
            break

        n_ceil, n_floor = math.ceil(n_float), math.floor(n_float)
        ceil_val = math.fabs(c * n_ceil * (n_ceil+1)/2 - t)
        floor_val = math.fabs(c * n_floor * (n_floor+1)/2 - t)

        val = min(ceil_val, floor_val)
        if val < min_val:
            min_val = val
            if ceil_val < floor_val:
                candidate = (m, int(n_ceil))
            else:
                candidate = (m, int(n_floor))
        m += 1
    print candidate[0] * candidate[1], candidate, min_val

if __name__ == '__main__':
    main()
