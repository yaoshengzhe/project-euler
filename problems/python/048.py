#! /usr/bin/python

def foo():
    return str(sum([ i**i for i in range(1, 1001)]))[-10::]

def main():
    print foo()

if __name__ == '__main__':
    main()
