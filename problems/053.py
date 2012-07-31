#! /usr/bin/python

def choose_k_from_n(n, k):
    ntok = 1
    for t in xrange(min(k, n-k)):
        ntok = ntok*(n-t) / (t+1)
    return ntok

def foo():
    count = 0
    for n in range(1, 101):
        for r in range(n+1):
            if choose_k_from_n(n, r) > 1000000:
                count += 1
    return count

def main():
    print foo()

if __name__ == '__main__':
    main()
