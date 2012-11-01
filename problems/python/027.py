#! /usr/bin/python

import math

def is_prime(num):
    if num < 2: return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def candidate_filter(candidate_coll, start, end):
    selected_candidate = []
    for candidate in candidate_coll:
        selected = True
        for n in range(start, end):
            if not is_prime(n*n + candidate[0]*n + candidate[1]):
                selected = False
        if selected:
            selected_candidate.append(candidate)
    return selected_candidate

def foo():
    prime_less_than_1000 = [ i for i in range(1000) if is_prime(i)]
    start, end = 0, 1

    candidate_coll = [ (a, b) for a in range(-999, 1000) for b in prime_less_than_1000 if is_prime(1+a+b)]

    while len(candidate_coll) > 1:
        start = end
        end += 1
        candidate_coll = candidate_filter(candidate_coll, start, end)

    print candidate_coll[0]
    return candidate_coll[0][0]  * candidate_coll[0][1]

def main():
    print foo()

if __name__ == '__main__':
    main()
