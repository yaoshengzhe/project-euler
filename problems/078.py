#! /usr/bin/python

def generalised_pentagonal(n): # 0, 1, -1, 2, -2
    pentagonal = lambda n : n*(3*n-1)/2

    if n < 0:
        return 0
    if n%2 == 0:
        return pentagonal(n/2+1)
    else:
        return pentagonal(-(n/2+1))

def main():

    pt = [1]
    for n in range (1, 100000+1):
        r = 0
        f = -1
        i = 0
        while 1:
            k = generalised_pentagonal(i)
            if k > n:
                break
            if i%2==0: f = -f
            r += f*pt[n - k]
            i += 1

        if r > 1000000 and r % 1000000 == 0:
            print n
            print r
            break
        pt.append(r)

if __name__ == '__main__':
    main()
