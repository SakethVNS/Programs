#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:45:57 2020

@author: sakethvns
"""





num = int(input().strip())

marks = []

for i in range(num):
    
    ele = input()
    
    marks.append(ele)

grades = list(map(int, marks))


for i in range(num):
    if grades[i] >38 and grades[i]%5 >= 3:
        grades[i] = grades[i] + 5 - grades[i]%5

print(grades)





