#! /usr/bin/python


four_million = 4000000

def foo():
    sum = 0
    a = 1
    b = 1
    while True:
        c = a + b
        a = b
        b = c
        if c >= four_million: break
        if c % 2 == 0:
            sum += c
    return sum

def main():
    print foo()

if __name__ == '__main__':
    main()
