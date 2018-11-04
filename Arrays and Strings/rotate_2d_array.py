# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 01:12:54 2018

@author: rajar
"""
def rotate_2d_array(m, len_m):
    for layer in range(0, len_m//2):
        #print(layer)
        f = layer
        l = len_m - layer - 1
        for i in range(f,l):
            off = i - f
            top = m[f][i]
            m[f][i] = m[l - off][f]
            #print(f,i, "gets", l - off,f)
            m[l - off][f] = m[l][l - off]
            #print(l - off,f, "gets", l,l - off)
            m[l][l - off] = m[i][l]
            #print(l, l - off, "gets",i,l)
            m[i][l] = top
            #print(i,l,"gets",f,i)
    return m

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print(rotate_2d_array(matrix, len(matrix)))

