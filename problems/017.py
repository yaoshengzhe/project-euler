#! /usr/bin/python

single_digit_num = ['one', 'two', 'three', 'four', 'five', 'six',
                    'seven', 'eight', 'nine']
double_digit_num = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
                    'eighty', 'ninety']
ten_to_nineteen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
                   'sixteen', 'seventeen', 'eighteen', 'nineteen']

def num2english(num):
    if num == 1000:
        return 'one thousand'
    elif num > 99:
        c = num / 100
        remains = num2english(num - c * 100)
        if len(remains) > 0:
            remains = ' and ' + remains

        return ' '.join([single_digit_num[c - 1], 'hundred', remains])
    elif num > 19:
        c = num / 10
        return ' '.join([double_digit_num[c - 2], num2english(num - c * 10)])
    elif num > 9:
        return ten_to_nineteen[num - 10]
    elif num > 0:
        return single_digit_num[num-1]
    elif num == 0:
        return ''
    else:
        raise Exception('Negative number!!! ==> %d <===' % (num))

def foo():
    return sum([ len(s) for i in range(1, 1001) for s in num2english(i).split()])

def main():
    print foo()

if __name__ == '__main__':
    main()
