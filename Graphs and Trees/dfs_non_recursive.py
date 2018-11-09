# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 14:17:46 2018

@author: rajar
"""

adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

def dfs_non_recursive(graph, start):
    stack = [start]
    path = []
    
    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
    return path

print(dfs_non_recursive(adjacency_matrix, 1))