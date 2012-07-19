#! /usr/bin/python

def is_pythagorean(a, b, c):
    arr = sorted([a, b, c])
    return arr[0]**2 + arr[1] **2 == arr[2]**2

def foo():

    for a in range(1, int(1000/3)):
        for b in range(a, int(1000-a)/2):
            c = 1000 - a -b
            if is_pythagorean(a, b, c):
                return a * b * c

def main():
    print foo()

if __name__ == '__main__':
    main()
