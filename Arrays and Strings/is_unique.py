# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 17:41:28 2018

@author: rajar
"""
def is_unique(s):
    uniq = []
    for i in s:
        if i in uniq:
            return False
        else:
            uniq.append(i)
    return True

s = "qwertyuiopp"
print(is_unique(s))       
