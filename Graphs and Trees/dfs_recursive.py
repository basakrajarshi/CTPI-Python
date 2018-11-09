# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 14:11:40 2018

@author: rajar
"""

adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]
    
    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)
    
    return path

print(dfs_recursive(adjacency_matrix, 1))