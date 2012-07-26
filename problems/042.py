#! /usr/bin/python

import sys
import math

def get_word_score(word):
    return sum([ord(ch) - ord('A') + 1 for ch in word])

def is_triangle_word(score):
    val = math.sqrt(1+8*score)
    epsilon = 1e-6
    if val - int(val) < epsilon:
        if val > 1 and int(val-1) % 2 == 0:
            return True
    return False

def foo():
    result = 0
    for word in ( word[1:-1] for line in sys.stdin.readlines() for word in line.split(',')):
        score = get_word_score(word)
        if is_triangle_word(score):
            result += 1
    return result

def main():
    print foo()

if __name__ == '__main__':
    main()
