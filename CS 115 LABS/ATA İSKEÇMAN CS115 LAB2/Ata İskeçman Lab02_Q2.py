# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:08:18 2023

@author: ata.iskecman-ug
"""

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
print("[",end="")
if b>=a:
    for i in range(a,(b+1)):
        if i != b:
            print(i,",",end="")
        else:
            print(i,end="")
    print("]")
else:
    for i in range(a,(b-1),-1):
        if i != b:
            print(i,",",end="")
        else:
            print(i,end="")
    print("]")