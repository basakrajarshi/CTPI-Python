# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 18:59:18 2018

@author: rajar
"""

s = "Mr John Smith"
ni = len(s)
for i in reversed(range(len(s))):
    print(i)
    '''if (s[i] == ' '):
        s[ni - 3:ni] = '%20'
        ni -= 3
    else:
        s[ni - 1] = s[i]
        ni -= 1'''
print(s)
    