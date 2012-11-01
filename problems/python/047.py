#! /usr/bin/python

from util.prime import is_prime

prime_less_than_one_thousand = [ i for i in range(1000) if is_prime(i)]

def find_prime_factor_num(num):
    count = 0

    for i in prime_less_than_one_thousand:

        if is_prime(num) or num == 1:
            count += 1
            break

        if num % i == 0:
            count += 1
            while num % i == 0:
                num = num / i

    return count

def foo():
    num = 600
    count = 0
    num_of_prime_factor = 4
    while True:

        if find_prime_factor_num(num) == num_of_prime_factor:
            count += 1
            if count == num_of_prime_factor:
                return num - count + 1
        else:
            count = 0

        num += 1

def main():
    print foo()

if __name__ == '__main__':
    main()
