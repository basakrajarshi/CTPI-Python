# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 21:11:53 2018

@author: rajar
"""

# Queue implementation using dequeue

from collections import deque

# Creating a queue
queue = deque([1,5,8,9])

# Enqueuing elements to the queue
queue.append(7)
queue.append(0)

# Dequeuing elements from the queue
queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()

# Printing the elements of the queue
print(queue)

