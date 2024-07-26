# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def pair_sum(n):
    m = []
    for i in range(0,(len(n)-1),2):
        m.append(n[i]+n[i+1])
    if len(n) % 2 == 0:
        return m
    else:
        m.append(n[-1])
        return m


original_list= [2, 8, 5, 9, 4, 7, 9, 3, 6]

result = pair_sum(original_list)
print(f"original list: {original_list}\npair sum list: {result}\n")


original_list2= [2, 8, 5, 9]

result2 = pair_sum(original_list2)
print(f"original list: {original_list2}\npair sum list: {result2}")