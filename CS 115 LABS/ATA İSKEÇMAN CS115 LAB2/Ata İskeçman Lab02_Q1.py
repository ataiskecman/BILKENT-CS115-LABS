# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 08:33:19 2023

@author: ata.iskecman-ug
"""
num=int(input("Enter a integer(-1 to stop): "))
the_sum=0
print("the sum of ",end="") 
for i in range(1,num+1):
    if i!=num:
        the_sum += 1/i
        print("(1/",i,")","+",sep="",end="")
    else:
        the_sum += 1/i
        print("(1/",i,")",sep="",end="")
print(f" is {the_sum:.3f}")


        