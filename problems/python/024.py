#! /usr/bin/python

import math

def find_nth_permutation(arr, k, n):
    if n == 0 or len(arr) == k:
        return

    idx = (n-1) / math.factorial(len(arr) - k - 1)

    arr[k], arr[idx+k] = arr[idx+k], arr[k]
    arr[(k+1):] = sorted(arr[(k+1):])
    find_nth_permutation(arr, k+1, n - idx*math.factorial(len(arr) - k - 1))

def foo():
    arr = [ str(i) for i in range(10)]
    find_nth_permutation(arr, 0, 1000000)

    return ''.join(arr)

def main():
    print foo()

if __name__ == '__main__':
    main()
