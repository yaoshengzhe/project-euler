#! /usr/bin/python

import math

from util.prime import is_prime

def main():
    prime_less_than_ten_thousand = [i for i in range(2, 10000) if is_prime(i)]
    upper_bound = 50000000
    solution_coll = set()
    for x in prime_less_than_ten_thousand:
        x_square = x*x
        if x_square > upper_bound:
            break
        for y in prime_less_than_ten_thousand:
            y_cubic = y*y*y
            if y_cubic > upper_bound:
                break
            for z in prime_less_than_ten_thousand:
                z_fourth = (z*z)**2
                if z_fourth > upper_bound:
                    break
                val = x_square + y_cubic + z_fourth
                if val > upper_bound:
                    break
                solution_coll.add(x_square + y_cubic + z_fourth)

    print len(solution_coll)
if __name__ == '__main__':
    main()
