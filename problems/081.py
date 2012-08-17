#! /usr/bin/python

import sys

def main():
    matrix = [ [int(num) for num in line.split(',')] for line in sys.stdin.readlines() ]
    score_matrix = [ [0 for v in range(len(matrix[0]))] for i in range(len(matrix)) ]

    score_matrix[0][0] = matrix[0][0]

    for x in range(1, len(matrix[0])):
            score_matrix[x][0] = score_matrix[x-1][0] + matrix[x][0]

    y = 1
    while y < len(matrix):
        score_matrix[0][y] = score_matrix[0][y-1] + matrix[0][y]
        for x in range(1, len(matrix[0])):
            score_matrix[x][y] = min(score_matrix[x-1][y], score_matrix[x][y-1]) + matrix[x][y]
        y += 1

    print score_matrix[-1][-1]

if __name__ == '__main__':
    main()
