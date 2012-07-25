#! /usr/bin/python

def get_digit_number_count(digit):
    return 10 ** digit - 10 ** (digit-1)

def d(n):
    digit = 1
    while True:
        count = get_digit_number_count(digit)
        if n > count * digit:
            n -= (count * digit)
            digit += 1
        else:
            index, pos = (n+digit-1) / digit, (n+digit-1) % digit
            return int(str(10 ** (digit-1) + index - 1)[pos])

def foo():
    result = 1
    for i in range(6+1):
        result = result * d(10**i)
    return result
def main():
    print foo()

if __name__ == '__main__':
    main()
