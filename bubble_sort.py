#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:52:24 2020

@author: sakethvns
"""


def swap(a,b):
    a,b = b,a
    return a,b

def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = swap(nums[j], nums[j+1])
    return nums



nums = list(map(int, input().strip().split()))
print(sort(nums))