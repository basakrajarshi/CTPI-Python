# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:31:07 2018

@author: rajar
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs_2(graph, start, visited=None):
    if (visited is None):
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs_2(graph, next, visited)
    return visited

print(dfs_2(graph, 'C'))