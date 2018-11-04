# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 14:37:59 2018

@author: rajar
"""

# Implement a function that removes duplicates from a LinkedList
# without using a buffer

# In this case, use two pointers: 
# (1) current, which iterates through the LinkedList
# (2) runner, which checks all subsequent nodes for duplicates

def remove_duplicates_2(ll):
    
    if ll.head is None:
        return
    
    current = ll.head
    
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next == runner.next.next
            else:
                runner == runner.next
        current == current.next
     
        return ll.head
    
ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)
remove_duplicates_2(ll)
print(ll)