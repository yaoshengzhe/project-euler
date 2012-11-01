#! /usr/bin/python

import sys

def next_roman_char(roman_num, i):
    if i+1 < len(roman_num):
        return roman_num[i+1]
    return None

def roman2num(roman_num):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    i = 0

    while i < len(roman_num):
        if roman_num[i] == 'I':
            next_char = next_roman_char(roman_num, i)
            if next_char == 'V' or next_char == 'X':
                num += roman_dict[next_char] - roman_dict[roman_num[i]]
                i += 1
            else:
                num += roman_dict[roman_num[i]]

        elif roman_num[i] == 'X':
            next_char = next_roman_char(roman_num, i)
            if next_char == 'L' or next_char == 'C':
                num += roman_dict[next_char] - roman_dict[roman_num[i]]
                i += 1
            else:
                num += roman_dict[roman_num[i]]

        elif roman_num[i] == 'C':
            next_char = next_roman_char(roman_num, i)
            if next_char == 'D' or next_char == 'M':
                num += roman_dict[next_char] - roman_dict[roman_num[i]]
                i += 1
            else:
                num += roman_dict[roman_num[i]]
        else:
            num += roman_dict[roman_num[i]]
        i += 1
    return num

def num2roman(num):
    if num >= 1000:
        return 'M' + num2roman(num - 1000)
    elif num >= 900:
        return 'CM' + num2roman(num - 900)
    elif num >= 500:
        return 'D' + num2roman(num - 500)
    elif num >= 400:
        return 'CD' + num2roman(num - 400)
    elif num >= 100:
        return 'C' + num2roman(num - 100)
    elif num >= 90:
        return 'XC' + num2roman(num - 90)
    elif num >= 50:
        return 'L' + num2roman(num - 50)
    elif num >= 40:
        return 'XL' + num2roman(num - 40)
    elif num >= 10:
        return 'X' + num2roman(num - 10)
    elif num >= 9:
        return 'IX' + num2roman(num - 9)
    elif num >= 5:
        return 'V' + num2roman(num - 5)
    elif num >= 4:
        return 'IV' + num2roman(num - 4)
    elif num >= 1:
        return 'I' + num2roman(num - 1)
    elif num == 0:
        return ''
    else:
        raise Exception('Unable to encode number to roman number. Num = ' + str(num))

def main():
    roman_num_coll = [line.strip() for line in sys.stdin.readlines()]
    offset = 0

    for  roman_num in roman_num_coll:
        print roman2num(roman_num), roman2num(num2roman(roman2num(roman_num))), roman_num, num2roman(roman2num(roman_num))
        offset += len(roman_num) - len(num2roman(roman2num(roman_num)))
    print offset

if __name__ == '__main__':
    main()
