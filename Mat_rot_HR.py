#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 09:09:23 2020

@author: sakethvns
"""

def swap1(a,b):
    # print(a, b, end = ' ')
    a,b = b,a
    # print("<------->", a, b)
    return a,b


def matrixRotation(matrix, r, m, n):
    row_end = m-1
    col_end = n-1
    row_begin = 0
    col_begin = 0
    
    
    
    # for i in range(0,1):
    while(row_begin < row_end and col_begin < col_end ):
        row = matrix[row_begin]
        row = row_inc_swap(row, col_begin, col_end)
        matrix[row_begin] = row
        # print(row_begin, row_end, col_begin, col_end)
        # col_inc_swap(col, col_end)
        for i in range(row_begin, row_end):
            
            matrix[i][col_end],matrix[i+1][col_end] = swap1(matrix[i][col_end],matrix[i+1][col_end])
        matrix[row_end].reverse()
        row = matrix[row_end]
        row = row_inc_swap(row, col_begin, col_end)
        row.reverse()
        matrix[row_end] = row
        # print(row)    
            
        for i in range(row_end, row_begin+1, -1):
            # print("i =", i, "col_end =", row_end, "col_begin", row_begin+1)
            matrix[i][col_begin],matrix[i-1][col_begin] = swap1(matrix[i][col_begin],matrix[i-1][col_begin])
            
        row_begin += 1
        row_end -= 1
        col_begin += 1
        col_end -= 1
        # print(row_begin, m, col_begin, n)
        # print(row_begin, row_end, col_begin, col_end)
    
    
    return matrix
    
    
def row_inc_swap(row, col_begin, col_end):
    for i in range(col_begin, col_end):
        # print(col_begin, col_end, row[i+1])
        (row[i], row[i+1]) = swap1(row[i], row[i+1])
    # print("row_inc wa")
    return row
    
    



def row_dec_swap(row, col_end, col_begin):
    for i in range(col_end, col_begin, -1):
        print(col_end, col_begin)
        (row[i], row[i-1]) = swap1(row[i], row[i-1])
    return row
    pass


def col_inc_swap(a,b):
    pass


def col_dec_swap(a,b):
    pass






mnr = input().rstrip().split()
m = int(mnr[0])

n = int(mnr[1])

r = int(mnr[2])

matrix = []

for i in range(max(m,n)):
    matrix.append(list(map(int, input().rstrip().split())))
    
for i in range(r):
    matrix = matrixRotation(matrix, r, m, n)

print('\n')

for i in range(m):
    for j in range(n):
        print(matrix[i][j], end = ' ')
    print('')



















