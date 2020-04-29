#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:14:40 2020

@author: sakethvns
"""


def fibo(n):
    first = 0
    second = 1
    renew = 1
    for i in range(0,n):
        if(n==0):
            return(first)
        else:
            renew = first + second
            first = second
            second = renew
    if(n!=0):
        return(renew)