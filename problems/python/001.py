#! /usr/bin/python

def multiple_of_three_or_five(num):
    return (num % 3 == 0) or (num % 5 == 0)

def foo(num):
    return sum([ i for i in range(num) if multiple_of_three_or_five(i)])

def main():
    print foo(1000)

if __name__ == '__main__':
    main()
