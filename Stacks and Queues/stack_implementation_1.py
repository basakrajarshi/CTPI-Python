# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 13:55:33 2018

@author: rajar
"""

class Stack:
    
    # Constructor : creates a list
    def __init__(self):
        self.stack = list()
        
    # Adding elements to a stack
    def push(self, data):
        # Checking to avoid duplicate entries
        if (data not in self.stack):
            self.stack.append(data)
            return True
        return False
    
    # Removing last element from the stack
    def pop(self):
        if (len(self.stack) <= 0):
            return ("Stack Empty!")
        return self.stack.pop()
    
    # Getting the size of the stack
    def size(self):
        return len(self.stack)
    
mystack = Stack()
print(mystack.push(5))
print(mystack.push(6))
print(mystack.push(9))
print(mystack.push(5))
print(mystack.push(3))
print(mystack.size())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
