# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 14:34:13 2018

@author: rajar
"""

# sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of all nodes to be checked
    queue = [start]
    
    # keep looping until there are nodes to be checked
    while queue:
        # pop shallowest node from the queue
        node = queue.pop(0)
        if node not in explored:
            # add node to a list of checked nodes
            explored.append(node)
            neighbours = graph[node]
            
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored

print((bfs_connected_component(graph,'A')))
