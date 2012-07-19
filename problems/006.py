#! /usr/bin/python

def foo():
    return sum([i for i in range(1, 101)])**2 - sum([i*i for i in range(1, 101)])

def main():
    print foo()

if __name__ == '__main__':
    main()
