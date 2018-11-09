# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:11:13 2018

@author: rajar
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if (vertex not in visited):
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    
    return visited

print(dfs(graph, 'A'))  