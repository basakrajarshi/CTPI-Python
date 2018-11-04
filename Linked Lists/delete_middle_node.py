# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 15:55:53 2018

@author: rajar
"""

# Delete a node in the middle (i.e. any node except first and last)
# Given only access to that node

def delete_middle_node:
    node.value = node.next.value
    node.next = node.next.next
    
ll = LinkedList()
ll.addmultiple([1,2,3,4])
middle_node = ll.add(5)
ll.addmultiple([7,8,9])

print(ll)
delete_middle_node(middle_node)
print(ll)

