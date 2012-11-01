#! /usr/bin/python

import sys

def visit(graph, node, result, visited_node_set):
    if node not in visited_node_set:
        visited_node_set.add(node)
        for parent in graph[node]:
            visit(graph, parent, result, visited_node_set)
        result.append(node)

def main():
    asked_key_coll = [[int(i) for i in line.strip()] for line in sys.stdin.readlines()]
    graph = {}
    no_edge_node_coll = set()
    for a, b, c in asked_key_coll:
        graph[c] = graph.get(c, [])
        graph[b] = graph.get(b, [])
        graph[c].append(b)
        graph[b].append(a)
        graph[a] = graph.get(a, [])
        no_edge_node_coll.add(c)
        if a in no_edge_node_coll:
            no_edge_node_coll.remove(a)
        if b in no_edge_node_coll:
            no_edge_node_coll.remove(b)
    result = []
    visited_node_set = set()
    for node in no_edge_node_coll:
        visit(graph, node, result, visited_node_set)
    print ''.join([str(i) for i in result])

if __name__ == '__main__':
    main()
