#! /usr/bin/python

def foo(bound):
    table = range(bound)
    table[1] = 0
    for i in range(len(table)):
        if table[i] == 0: continue
        count = 2
        while count * i < len(table):
            table[count * i] = 0
            count += 1
    res = 0
    for i in table:
        res += i
    return res

def main():
    print foo(2000000)

if __name__ == '__main__':
    main()
