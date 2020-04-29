#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:20:28 2020

@author: sakethvns
"""

"""My code
a = input().strip().split(':')
if(a[2][2] == 'p' or a[2][2] == 'P' and int(a[0])!=12):
    a[0] = str(int(a[0]) + 12)
if int(a[0])==24 or (int(a[0]) ==12 and a[2][2] =='A'):
    a[0] = "00"
    

a[2] = a[2].replace('P','')
a[2] = a[2].replace('A','')
a[2] = a[2].replace('M','')

print(':'.join(a))

"""


"""Features solution
s = raw_input()
zn = s[-2:]
if zn == "PM" and s[:2] != "12":
    s = str(12 + int(s[:2])) + s[2:]
if zn == "AM" and s[:2] == "12":
    s = "00" + s[2:]
print s[:-2]


"""


