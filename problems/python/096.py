#! /usr/bin/python

import sys
import copy
import itertools
import math
import operator
from termcolor import colored

def print_puzzle(puzzle, color='green'):
    print
    for row in puzzle:
        print colored(row, color)
    print

def print_puzzle_with_highlight(puzzle, i, j, highlight='red', color='green'):
    print
    for row in range(9):
        buf = []
        for col in range(9):
            if row == i and col == j:
                buf.append(colored(puzzle[row][col], highlight))
            else:
                buf.append(colored(puzzle[row][col], color))
        print ' '.join(buf)
    print

def validate_solution(puzzle, verbose=False):
    if puzzle is None:
        if verbose:
            print colored('Validation failed, puzzle is None', 'red')
        return False

    for i in range(9):
        row = puzzle[i]
        for j in range(9):
            val = puzzle[i][j]
            if val == 0:
                if verbose:
                    print colored('Validation failed, there are unfilled fields at (%d, %d)' % (i, j), 'red')
                return False

    for i in range(9):
        row = puzzle[i]
        if sum(row) != 45:
            if verbose:
                print colored('Validation failed, Row: %d\'s sum not equals to 45' % (i+1), 'red')
            return False

    for col in range(9):
        if sum([row[col] for row in puzzle]) != 45:
            if verbose:
                print colored('Validation failed, there are columns sum not equals to 45', 'red')
            return False

    for i in range(3):
        for j in range(3):
            if sum(flat_square(puzzle, (i, j))) != 45:
                if verbose:
                    print colored('Validation failed, there are squares sum not equals to 45', 'red')
                return False
    return True

def find_unknown_pos(puzzle):
    unknown_coll = []
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                unknown_coll.append((i, j, set(range(1, 10))))
    return unknown_coll

def find_square(puzzle, i, j):
    return (i/3, j/3)

def flat_square(puzzle, square):
    result = []
    i, j = square
    for row in range(i*3, i*3+3):
        for col in range(j*3, j*3+3):
            result.append(puzzle[row][col])
    return result

def reduce_possible_choice(unknown, puzzle):
    i, j, possible_choice = unknown
    possible_choice = possible_choice - set(filter(lambda x: x > 0, puzzle[i]))
    possible_choice = possible_choice - set(filter(lambda x: x > 0, [row[j] for row in puzzle]))
    flatted_square = flat_square(puzzle, find_square(puzzle, i, j))
    possible_choice = possible_choice - set(filter(lambda x: x > 0, flatted_square))

    return (i, j, possible_choice)


def solve(puzzle):

    while True:
        unknown_coll = find_unknown_pos(puzzle)
        if len(unknown_coll) == 0:
            break
        reduced = False
        new_unknown_coll = []
        for unknown in unknown_coll:
            i, j, possible_choice = reduce_possible_choice(unknown, puzzle)
            if len(possible_choice) == 0:
                return None
            if len(possible_choice) == 1:
                puzzle[i][j] = possible_choice.pop()
                reduced = True
            else:
                new_unknown_coll.append((i, j, possible_choice))

        if not reduced:
            new_unknown = sorted(new_unknown_coll[:], lambda x, y: len(x[2]) - len(y[2]))[0]
            i, j, possible_choice = new_unknown
            for choice in possible_choice:
                new_puzzle = copy.deepcopy(puzzle)
                new_puzzle[i][j] = choice
                candidate = solve(new_puzzle)
                if validate_solution(candidate):
                    return candidate
            break

    if validate_solution(puzzle):
        return puzzle
    else:
        return None

def top_left_corner(puzzle):
    return int(''.join([str(i) for i in puzzle[0][:3]]))

def next_puzzle(stream):
    while stream.readline():
        puzzle = []
        for i in range(9):
            puzzle.append([int(ch) for ch in stream.readline().strip()])
        yield puzzle

def main():
    print sum([top_left_corner(solve(puzzle)) for puzzle in next_puzzle(sys.stdin)])

if __name__ == '__main__':
    main()
