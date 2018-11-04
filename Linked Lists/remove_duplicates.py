# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 14:19:18 2018

@author: rajar
"""

# Implement a function that removes duplicates from a LinkedList

#import LinkedList

def remove_duplicates(ll):
    
    if ll.head is None:
        return
    
    current = ll.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next
            
    return ll

ll = LinkedList()
ll.generate(100, 0 , 9)
print(ll)
remove_duplicates(ll)
print(ll)
