# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 14:30:15 2018

@author: rajar
"""

# Stack implementation using an array

class Stack2:
    
    # Constructor
    def __init__(self):
        self.stack = list()
        self.maxSize = 8
        self.top = 0
        
    # Adds element to the stack
    def push(self, data):
        if (self.top >= self.maxSize):
            return ("Stack Full!")
        self.stack.append(data)
        self.top += 1
        return True
    
    # Removes element from the stack
    def pop(self):
        if (self.top <= 0):
            return ("Stack Empty!")
        item = self.stack.pop()
        self.top -= 1
        return item
    
    # Size of the stack
    def size(self):
        return self.top
    
s = Stack2()
print(s.push(1))

print(s.push(2))
print(s.push(3))
print(s.push(4))
print(s.push(5))
print(s.push(6))
print(s.push(7))
print(s.push(8))
print(s.push(9))
print(s.size())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

    