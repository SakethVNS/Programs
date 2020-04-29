#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 08:52:00 2020

@author: sakethvns
"""
import time

n = int(input("enter end ="))

a = range(1,n,2)

search = int(input("enter number to find  "))

start_time = time.time()
iteration = 0

for i in range(len(a)):
    iteration+=1
    if a[i] == search:
        print("element found at ", i)
        break

print("No of iterations =", iteration)
print(time.time()-start_time, "seconds taken to execute the program")