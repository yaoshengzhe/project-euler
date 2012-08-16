#! /usr/bin/python

from util.prime import is_prime

def main():
    count = 0
    upper = 1000000
    phi = range(1, upper+1)

    for d in range(2, upper+1):
        if d == phi[d-1]:
            for n in range(d, upper+1, d):
                phi[n-1] = phi[n-1] * (d-1)/d

        count += phi[d-1]

    print count
if __name__ == '__main__':
    main()
