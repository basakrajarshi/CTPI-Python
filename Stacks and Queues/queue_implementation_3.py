# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 22:03:32 2018

@author: rajar
"""

class Queue2:
    
    # Constructor
    def __init__(self):
        self.queue = list()
        self.maxSize = 8
        self.head = 0
        self.tail = 0
        
    # Adding elements
    def enqueue(self, data):
        # Checking if the queue is full
        if (self.size() >= self.maxSize):
            return ("Queue Full")
        self.queue.append(data)
        self.tail += 1
        return True
    
    def dequeue(self):
        if (self.size() <= 0):
            self.resetQueue()
            return ("Queue Empty")
        data = self.queue[self.head]
        self.head += 1
        return data

    # Calculate size
    def size(self):
        return self.tail - self.head
    
    # Reset queue
    def resetQueue(self):
        self.tail = 0
        self.head = 0
        self.queue = list()
        
q = Queue2()
print(q.enqueue(1))#prints True
print(q.enqueue(2))#prints True
print(q.enqueue(3))#prints True
print(q.enqueue(4))#prints True
print(q.enqueue(5))#prints True
print(q.enqueue(6))#prints True
print(q.enqueue(7))#prints True
print(q.enqueue(8))#prints True
print(q.enqueue(9))#prints Queue Full!
print(q.size())#prints 8        
print(q.dequeue())#prints 8
print(q.dequeue())#prints 7 
print(q.dequeue())#prints 6
print(q.dequeue())#prints 5
print(q.dequeue())#prints 4
print(q.dequeue())#prints 3
print(q.dequeue())#prints 2
print(q.dequeue())#prints 1
print(q.dequeue())#prints Queue Empty
#Queue is reset here 
print(q.enqueue(1))#prints True
print(q.enqueue(2))#prints True
print(q.enqueue(3))#prints True
print(q.enqueue(4))#prints True
    