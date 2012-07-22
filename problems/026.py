#! /usr/bin/python

def find_recurring_cycle(num):
    scale = 10 ** len(str(num))
    result_coll = []
    result_set = set()
    r = 1
    while True:
        q, r = (r * scale)  / num, (r * scale) % num

        if r == 0:
            return 0

        if (q, r) in result_set:
            return [ i for i in reversed(result_coll)].index((q, r)) + 1
        else:
            result_coll.append((q, r))
            result_set.add((q, r))

def foo():
    max_val = 0
    max_num = 1
    for i in range(1, 1000):
        val = find_recurring_cycle(i)
        if val > max_val:
            max_val = val
            max_num = i
    return max_num

def main():
    print foo()

if __name__ == '__main__':
    main()
