# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 08:36:41 2023

@author: ata.iskecman-ug
"""

def sum_without_twenties(a,b,c):
    total=0
    if a //10==2:
        a=0
    if b //10==2:
        b=0
    if c //10==2:
        c=0
    total=total + a + b + c
    return total
    

a =int(input("Enter first integer: "))
b =int(input("Enter second integer: "))
c =int(input("Enter third integer: "))
while a>0 and b>0 and c>0:
    total=sum_without_twenties(a,b,c)
    print(f"Sum of {a} {b} {c} without twenties is {total}")
    a =int(input("Enter first integer: "))
    b =int(input("Enter second integer: "))
    c =int(input("Enter third integer: "))