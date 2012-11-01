#! /usr/bin/python

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

def reverse_sum(num):
    return num + int(str(num)[::-1])

def foo():
    count = 0
    for num in range(10000):
        is_lychrel_num = True
        for i in range(50):
            num = reverse_sum(num)
            if is_palindrome(num):
                is_lychrel_num = False
                break
        if is_lychrel_num:
            count += 1

    return count

def main():
    print foo()

if __name__ == '__main__':
    main()
