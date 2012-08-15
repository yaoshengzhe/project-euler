#! /usr/bin/python

from util.prime import is_prime

# phi(p_0^q0p_1^q_1...) = phi(p_0^q0) * phi(p_1^q_1) * ...
# here p_n is prime number, q_n is positive integer
# so, for given number n, factorize n and we get n = p_0^q_0 * p_1^q_1 * ..
# therefore n / phi(n) = p_0^q_0 * p_1^q_1 / (phi(p0^q0) * phi(p1^q1) * ...)
# we know phi(p^q) = p^q * (1 - 1/p)
# thus n/phi(n) = 1 / ((1-1/p0) * (1-1/p1) * ...) = p0*p1*... / ((p0-1)*(p1-1) * ...)
# notice pn is prime number. therefore, the more prime factors number n has, the larger the ratio n / phi(n)
# function f(x) = x / (x-1) is a decrease function for all positive x, which means f(x1) < f(x2) if x1 > x2.
# Here we come up an algorithm, start from prime number 2, find all continuous prime number and make sure their prod is less than upper bound. Exit util we find a next prime number but it causes prod larger than given upper bound.

# Also see on wiki: http://en.wikipedia.org/wiki/Euler%27s_totient_function
def main():
    cache = {}
    max_ratio = 1
    n_max = 1000000

    max_val = 1
    for n in ( i for i in xrange(2, n_max+1) if is_prime(i) ):
        if max_val * n <= n_max:
            max_val *= n
        else:
            break

    print max_val

if __name__ == '__main__':
    main()
