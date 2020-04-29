#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:57:10 2020

@author: sakethvns
"""
from functools import reduce
from statistics import mode

def func1(mat,diff):
    if diff[0] == diff[3] == 0:
        if diff[1] == diff[4] == 0:
            pass
        elif diff[1]!=diff[4]:
            mat_1 = mat[1:][1:]
    return mat_1
    




def func2():
    pass


def  get(mat):
    

    row_sum = []
    col_sum = []
    diag_sum = 0

    for i in range(3):
        row_sum.append(reduce(lambda a,b:a+b, mat[i]))
        # row_sum.append(ele)
        t_mat = list(zip(*mat))

    for i in range(3):
            col_sum.append(reduce(lambda a,b:a+b, t_mat[i]))
            # diag_sum.append(ele)
        
    for i in range(3):
        diag_sum += mat[i][i]

    new = []
    total = row_sum + col_sum
    total.append(diag_sum)
    
    most = mode(total)
    return total,most,

mat = []

for i in range(3):#input matrix
    mat.append(list(map(int, input().strip().split(' '))))

[total,most] = get(mat)

num = 0

diff = list(map(lambda n: most-n, total))

if diff[-1] == 0:
    total = func1(mat,diff)
else:
    total = func2()
    
    


# for i in range(len(total)):
#     inter = total.count(total[i])
#     new.append(inter)
    
# print(len(new)-new.count(max(new)))








