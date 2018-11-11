# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 20:46:17 2018

@author: rajar
"""

# Implementing a queue using a list

class Queue:
    
    # Constructor : creates a list
    def __init__(self):
        self.queue = list()
        
    # Adding elements to a queue
    def enqueue(self, data):
        # Checking to avoid duplicate entry (not mandatory)
        if (data not in self.queue):
            self.queue.insert(0,data)
            return True
        return False
    
    # Removing the last element from the queue
    def dequeue(self):
        if (len(self.queue) > 0):
            return self.queue.pop()
        return ("Queue empty!")
    
    # Getting the size of the queue
    def size(self):
        return len(self.queue)
    
    
    # Printing the elements of the queue
    def printqueue(self):
        return self.queue
    
myQueue = Queue()
print(myQueue.enqueue(5))
print(myQueue.enqueue(6))
print(myQueue.enqueue(9))
print(myQueue.enqueue(5))
print(myQueue.enqueue(3))
print(myQueue.size())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.size())
print(myQueue.dequeue())