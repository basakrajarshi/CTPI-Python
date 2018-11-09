# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 19:48:10 2018

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

# find the shortest path between two nodes of a graph using bfs
def shortest_path(graph, start, goal):
    # keep track of all visited nodes
    explored = []
    # keep track of all nodes to be checked
    queue = [start]
    
    # return path if start == goal : base case
    if (start == goal):
        return "Start = goal"
    
    # keeps looping untill all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        print (path, "was popped from the queue")
        # get the last node from the path
        node = path[-1]
        print ("Node is ", node)
        print ("Explored is ", explored)
        if node not in explored:
            neighbours = graph[node]
            print ("Neighbours are", neighbours)
            # go through all neighbour nodes, construct a new path
            # and push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                print ("new_path is", new_path)
                new_path.append(neighbour)
                print ("new_path is", new_path)
                queue.append(new_path)
                print ("Queue is", queue)
                
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
                
            # mark node as explored
            explored.append(node)
            
    return "No path exists between these nodes"

print(shortest_path(graph, 'A', 'F'))