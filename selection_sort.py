#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:02:44 2020

@author: sakethvns
"""

def swap(a,b):
    print("swapped:", a, b)
    a,b = b,a
    return a,b





def select_sort(nums):
    for i in range(len(nums)-1):
        var = i
        for j in range(i, len(nums)-1):
            if nums[j]>nums[j+1]:#To sort in descending order change greater to lesser
                # minn = nums[j+1]
                var = j+1
        nums[i], nums[var] = swap(nums[i], nums[var])
    return nums






nums = list(map(int, input().strip().split()))



print(select_sort(nums))