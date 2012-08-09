#! /usr/bin/python

import sys

import itertools

def is_valid_char(val):
    return (val >= ord('A') and val <= ord('z')) or (val >= ord('0') and val <= ord('9')) or val in set([ord('"'), ord('.'), ord(' '), ord("\n"), ord(';'), ord(','), ord("'"), ord('('), ord(')'), ord('!')])

def find_key(encoded_num_coll, idx):
    candidate = []
    for key in range(ord('a'), ord('z')+1):
        is_candidate = True
        for n in encoded_num_coll[idx::3]:
            a = n ^ key
            if  not is_valid_char(a):
                is_candidate = False
                break
        if is_candidate:
            candidate.append(key)
    if len(candidate) != 1:
        raise Exception('ERROR: ' + ', '.join(candidate))
    return candidate[0]

def foo():
    count = 0
    encoded_num_coll = [ int(num) for line in sys.stdin.readlines() for num in line.split(',')]

    a, b, c = find_key(encoded_num_coll, 0), find_key(encoded_num_coll, 1), find_key(encoded_num_coll, 2)

    count = 0
    for i in range(len(encoded_num_coll)):
        if i % 3 == 0:
            count += encoded_num_coll[i] ^ a
        elif i % 3 == 1:
            count += encoded_num_coll[i] ^ b
        else:
            count += encoded_num_coll[i] ^ c

    return count

def main():
    print foo()

if __name__ == '__main__':
    main()
