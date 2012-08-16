#! /usr/bin/python

def main():
    n = 100
    C = range(1, n)
    T = [0 for i in range(n+1)]
    T[0] = 1

    for i in range(len(C)):
        for j in range(C[i], len(T)):
            T[j] += T[j - C[i]]
    print T[n]

if __name__ == '__main__':
    main()
