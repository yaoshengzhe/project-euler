#! /usr/bin/python

def foo():
    return sum([ int(i) for i in str(2**1000)])

def main():
    print foo()

if __name__ == '__main__':
    main()
