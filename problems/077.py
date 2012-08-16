#! /usr/bin/python

from util.prime import is_prime

def infinite_prime_list():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

def main():
    n = 1000

    T = [0 for i in range(n+1)]
    T[0] = 1

    for i in infinite_prime_list():
        if T[i] > 5000:
            print i
            break
        for j in range(i, len(T)):
            T[j] += T[j - i]

if __name__ == '__main__':
    main()
