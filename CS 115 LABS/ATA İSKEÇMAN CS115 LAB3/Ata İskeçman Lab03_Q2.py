# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:26:39 2023

@author: ata.iskecman-ug
"""

def get_substring_positions(a,b):
    total=0
    for n in range(min(len(a),len(b))):
        if a[n:n+2] == b[n:n+2]:
            total += 1
    return f"'{a}' and '{b}' have {total} positions where they contain the same substrings of length 2"
    
a=str(input("Enter first string: "))
if a=="":
    print("Enter second string: finished")
else:
    b=str(input("Enter second string: "))
while a!="" and b!="":
    result=get_substring_positions(a,b)
    print(result)
    a=str(input("Enter first string: "))
    b=str(input("Enter second string: "))
