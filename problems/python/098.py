#! /usr/bin/python

import sys
import copy
import itertools
import math
import operator
from termcolor import colored

def square_num_cache():
    cache = {}
    for i in xrange(100000):
        num = i**2
        key = len(str(num))
        if key not in cache:
            cache[key] = set([num])
        else:
            cache[key].add(num)

    return cache

# Given a anagram list and square num cache, find the max square number
def get_largest_square_number(anagram_list, cache):

    square_candidate = cache.get(len(anagram_list[0]), None)
    # hacky way to reduce square number candidate space, only works if there is no duplicate characters in anagram
    candidate_coll = filter(lambda x: len(set(str(x))) == len(anagram_list[0]), square_candidate)
    print anagram_list, len(square_candidate), len(candidate_coll)
    max_square_num = 0
    # for each anagram pair, find all possible square number pair
    # Then find the maximum square number
    for pair in itertools.combinations(anagram_list, 2):
        a, b = pair
        for candidate in candidate_coll:
            candidate_str = str(candidate)
            word_digit_map = {a[i]: candidate_str[i] for i in xrange(len(candidate_str))}
            val = int(''.join([str(word_digit_map[ch]) for ch in b]))
            if val in candidate_coll:
                if max_square_num < val:
                    max_square_num = val
                if max_square_num < candidate:
                    max_square_num = candidate

    return max_square_num

def main():
    anagram_coll = {}
    for line in sys.stdin.readlines():
        for word_with_quotes in line.split(','):
            word = word_with_quotes[1:-1]
            key = ''.join(sorted(word))
            if key not in anagram_coll:
                anagram_coll[key] = [word]
            else:
                anagram_coll[key].append(word)

    cache = square_num_cache()
    anagram_more_than_one = filter(lambda key: len(anagram_coll[key]) > 1, anagram_coll)
    print max(map(lambda key: get_largest_square_number(anagram_coll[key], cache), anagram_more_than_one))

if __name__ == '__main__':
    main()
