#! /usr/bin/python

import sys
import heapq

def is_in_matrix(matrix, i, j):
    return i > -1 and j > -1 and i < len(matrix) and j < len(matrix[0])

def add_node_if_exist(search_tree, matrix, i, j, score, used_node_set):
    if is_in_matrix(matrix, i, j) and not (i, j) in used_node_set:
        heapq.heappush(search_tree, (score+matrix[i][j], (i, j)))


def search(search_tree, matrix):
    used_node_set = set([])
    score, pos = heapq.heappop(search_tree)
    while pos != (len(matrix)-1, len(matrix[-1])-1):
        used_node_set.add(pos)
        i, j = pos
        # left
        add_node_if_exist(search_tree, matrix, i-1, j, score, used_node_set)
        # right
        add_node_if_exist(search_tree, matrix, i+1, j, score, used_node_set)
        # up
        add_node_if_exist(search_tree, matrix, i, j-1, score, used_node_set)
        # down
        add_node_if_exist(search_tree, matrix, i, j+1, score, used_node_set)
        score, pos = heapq.heappop(search_tree)

    return score

def main():
    matrix = [ [int(num) for num in line.split(',')] for line in sys.stdin.readlines() ]
    #score_matrix = [ [0 for v in range(len(matrix[0]))] for i in range(len(matrix)) ]
    search_tree = []
    heapq.heappush(search_tree, (matrix[0][0], (0, 0)))
    print search(search_tree, matrix)

if __name__ == '__main__':
    main()
