#! /usr/bin/python

import sys

def square_digit_sum(num):
    return sum([int(ch) ** 2 for ch in str(num)])

def main():
    lower, upper = 1, 10000000
    table_size = 567 + 1
    table = [-1 for i in range(table_size)]
    table[1] = 1
    table[89] = 89
    count = 0
    for i in range(lower, upper):
        num = i
        num = square_digit_sum(num)
        index = num
        if table[index] == -1:
            while num != 1 and num != 89:
                num = square_digit_sum(num)
                if table[num] != -1:
                    num = table[num]
                    break
            table[index] = num

        if table[index] == 89:
            count += 1
        print i

    print count

if __name__ == '__main__':
    main()
