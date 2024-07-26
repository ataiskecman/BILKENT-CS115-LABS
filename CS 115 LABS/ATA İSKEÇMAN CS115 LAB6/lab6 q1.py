# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 08:34:38 2023

@author: ata.iskecman-ug
"""

def formMatrix(n):
    for row in range(n):
        for col in range(n):
            if row-col>=0:
                print(row-col,end=" ")
            else:
                print((row+col),end=" ")
        print()

n=int(input("Enter a number which will determine the size of the matrix:"))
formMatrix(n)
                