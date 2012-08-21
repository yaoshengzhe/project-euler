#! /usr/bin/python

import sys

def main():
    matrix = [ [int(num) for num in line.split(',')] for line in sys.stdin.readlines() ]
    score_matrix = [ [0 for v in range(len(matrix[0]))] for i in range(len(matrix)) ]

    for n in range(0, len(matrix)):
            score_matrix[n][0] = matrix[n][0]

    # start from the second column
    for column in range(1, len(matrix[0])):
        # scan from top to bottom
        for row in range(len(matrix)):
            if row == 0:
                score_matrix[row][column] = score_matrix[row][column-1] + matrix[row][column]
            else:
                score_matrix[row][column] = min(score_matrix[row][column-1], score_matrix[row-1][column]) + matrix[row][column]
        # scan from bottom to top
        for row in reversed(range(len(matrix))):
            if row == len(matrix)-1:
                score_matrix[row][column] = min(score_matrix[row][column], score_matrix[row-1][column] + matrix[row][column])
            else:
                score_matrix[row][column] = min(score_matrix[row][column], score_matrix[row+1][column] + matrix[row][column])

    print min([score_matrix[i][-1] for i in range(len(score_matrix))])

if __name__ == '__main__':
    main()
