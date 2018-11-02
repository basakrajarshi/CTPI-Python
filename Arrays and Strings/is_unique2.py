# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 17:49:33 2018

@author: rajar
"""
# Is unique without an additional data structure
def is_unique_2(s):    
    #s = "qwertyuiop"
    for i in range(len(s)):
        #print(s[i])
        for j in range(i+1, len(s)):
            #print(s[i],s[j])
            if s[i] == s[j]:
                return False
    return True

s = "qwertpyuiop" 
print(is_unique_2(s))       
