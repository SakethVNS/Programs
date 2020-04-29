#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:36:59 2020

@author: sakethvns
"""

from functools import reduce
#This program takes 5 integers and gives mininmum sum of four integers and maximum sum of four integers and input given is sorted

"""My min and max hacker rank code
import math
import os
import random
import re
import sys

def swap(a,b):
    c = a
    a = b
    b = c
    return(a,b)
# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    b = arr
    min1 = 0
    max1 = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                (b[i],b[j]) = swap(b[i],b[j])
#    for i in range(len(arr)):
#        print(b[i], end = ' ')
    for i in range(0,4):
        min1 += b[i]
    for i in range(4,0,-1):
        max1 += b[i]
    print(min1, max1)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)




"""


"""user_1 - HR code for min and max
a = input().strip().split(' ') #strip(char) - removes mentioned character from leading and trailing edges only. If nothing is
for i in range(0, len(a)):     #mentioned space is removed from ends.
    a[i] = int(a[i])           #split(char, maxsplit) - removes mentioned character from the string and separates before characters
                               #and after characters maxsplit number of times. If maxsplit not mentioned then all appearances are removed
s = sum(a)
print(str(s - max(a)) + " " + str(s - min(a)))
"""


"""User_2 - HR code for min and max
toy = list(map(int, input().split()))
ans=sum(toy)
toy.sort()
print(ans-toy[len(toy)-1],ans-toy[0])
"""

""" Inbuilt functions reduce, filter, map, lambda:
    filter(function, iteration):
        ->filter gives out sequence by which is a result of applying a condition on other sequence
        ->filter takes sequence and gives sequence so to get in list format use list(filter())
        ->filter takes two arguments one is function either built in or created function must return
          true or false for a specified condition
        Ex:
            def is_even(n):
                return n%2 == 0
            nums = [2, 4, 7, 9, 3, 245, 548, 976, 1, 0]
            evens = list(filter(is_even, nums))
            print(evens)
    map(function, iteration):
        ->map performs operations on all values of a sequence
        ->map also takes sequence and gives sequence, mention list(map()) to get in list format or any other
        Ex:
           nums = [2, 4, 7, 9, 3, 245, 548, 976, 1, 0]
            evens = list(filter(lambda n:n%2==0, nums)) 
            doubles = list(map(lambda n: n*n, evens))
            print(doubles)
    reduce(function, sequence):
        ->reduce takes sequence and performs some operation specified and returns a single value
        ->it is in functools library
        Ex:
            nums = [2, 4, 7, 9, 3, 245, 548, 976, 1, 0]
            evens = list(filter(lambda n:n%2==0, nums)) 
            doubles = list(map(lambda n: n*n, evens))
            print(doubles)
            sum = reduce(lambda a,b : a+b, doubles)#reduce belongs to module functools 
            print(sum)

"""



nums = [2, 4, 7, 9, 3, 245, 548, 976, 1, 0]
evens = list(filter(lambda n:n%2==0, nums))
print(evens)
doubles = list(map(lambda n: n*n, evens))
print(doubles)
sum = reduce(lambda a,b : a+b, doubles)#reduce belongs to module functools 
print(sum)


















