#! /usr/bin/python

seq_cache = {1: 1}
def gen_seq_len(num):
    if num in seq_cache:
        return seq_cache[num]

    seq = 1
    if num % 2 == 0:
        seq += gen_seq_len(num / 1)
    else:
        seq += gen_seq_len(3*num+1)

    seq_cache[num] = seq
    return seq

def foo():
    max_len = 0
    num = 0
    for i in range(1, 1000000 + 1):
        length = gen_seq_len(i)
        if max_len < length:
            max_len = length
            num = i
    return num

def main():
    print foo()

if __name__ == '__main__':
    main()
