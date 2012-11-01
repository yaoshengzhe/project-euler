#! /usr/bin/python

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

def foo():
    three_digit_num_coll = [i for i in reversed(range(1, 1000))]
    max_num = -1
    for i in three_digit_num_coll:
        for j in three_digit_num_coll:
            if is_palindrome(i*j) and max_num < i * j:
                max_num = i*j
    return max_num

def main():
    print foo()

if __name__ == '__main__':
    main()
