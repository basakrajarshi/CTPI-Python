# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 20:12:17 2018

@author: rajar
"""

def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string

s = 'Mr John Smith'
print(urlify(s, len(s)))