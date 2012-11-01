#! /usr/bin/python

def get_signiture(num):
    return ''.join(sorted(str(num)))

def check(num):
    sig = get_signiture(num)
    for i in range(2, 7):
        if sig != get_signiture(i * num):
            return False
    return True

def foo():
    for num in xrange(10, 1000000000):
        if check(num):
            return num
    return -1

def main():
    print foo()

if __name__ == '__main__':
    main()
