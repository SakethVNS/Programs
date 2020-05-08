#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" My recursion code didn't work
Created on Fri May  8 08:21:06 2020

@author: sakethvns


from math import log2, floor

def bin_search(search, arr, first, last, count):
    if count == 10:
        return
    # print(arr[first], arr[last], count, '\t', first, last, arr[(first + last)//2])    
    if first == last:
        return first+1
    if arr[(first+last)//2] == search:
        return (first+last)//2 + 1
    elif arr[first] == search:
        return first +1
    elif arr[last] == search:
        return last +1
    elif search > arr[(first+last)//2]:
        count+=1
        return bin_search(search, arr, first, (first+last)//2, count)
    elif search < arr[(first+last)//2]:
        count +=1
        return bin_search(search, arr, (first+last)//2 + 1, last, count)

    
    
    
    
    
    
    pass

scores_count = int(input())

scores = list(map(int, input().rstrip().split()))

alice_count = int(input())

alice = list(map(int, input().rstrip().split()))



scores = sorted(list(set(scores)), reverse=True)




for j in range(len(alice)):
    pos = bin_search(alice[j], scores, 0, len(scores)-1, 0)
    if alice[pos-1] < scores[len(scores)-1]:
        print(pos+1)
        break
    print(pos)
    
"""    


""" My normal code worked but for large arrays it didn't work
scores_count = int(input())

scores = list(map(int, input().rstrip().split()))

alice_count = int(input())

alice = list(map(int, input().rstrip().split()))



scores = sorted(list(set(scores)), reverse=True)

for j in range(alice_count):
    for i in range(len(scores)):
        # print(alice[j], scores[i], i)
        if alice[j] >= scores[i]:
            print(i+1)
            break
        elif i == len(scores)-1:
            print(len(scores)+1)
            break





"""


#User_1's code it worked

# n = int(input().strip())
scores = list(reversed(sorted(list(set([int(scores_temp) for scores_temp in input().strip().split(' ')])))))
# m = int(input().strip())
alice = list(sorted(set(int(alice_temp) for alice_temp in input().strip().split(' '))))

for x in alice:
    while len(scores) > 0 and scores[-1] <= x:
        print('\t', scores[-1])
        del scores[-1]
        
    
    print(len(scores) + 1)


"""
sort all lists and find element by deleting the element at end by comparing


if scores element is less than or equal to last element of alice then remove last element 

"""
    
    
