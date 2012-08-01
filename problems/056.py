#! /usr/bin/python

def foo():
    max_digit_sum = 0

    for a in range(1, 100):
        for b in range(1, 100):
             s = sum([ int(ch) for ch in str(a ** b)])
             if max_digit_sum < s:
                 max_digit_sum = s
    return max_digit_sum

def main():
    print foo()

if __name__ == '__main__':
    main()
