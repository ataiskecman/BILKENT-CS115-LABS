# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:50:29 2023

@author: ata.iskecman-ug
"""
def getSuffix(a,b):
    return a % (10**b)

def getNoOfDigits(n):
    i=0
    while getSuffix(n,i) != getSuffix(n,i+1) :
        i += 1
    return i
      

a= int(input("Enter an integer number: "))
b= int(input("Enter  the number of digits of suffix: "))   
print(f"The suffix is: {getSuffix(a,b)}")
print(f"The number of digits of {a} is {getNoOfDigits(a)}")