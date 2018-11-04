# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 15:09:45 2018

@author: rajar
"""

# Find the kth last element in a linkedlist

from LinkedList import LinkedList

def kth_to_last(ll):
    runner = current = ll.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next
        
    while runner:
        current = current.next
        runner = runner.next
        
    return current