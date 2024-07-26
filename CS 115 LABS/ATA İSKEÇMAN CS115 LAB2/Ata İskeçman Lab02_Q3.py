# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 09:39:02 2023

@author: ata.iskecman-ug
"""

string=str(input("Enter a string(exit to stop): "))

while string.upper() != "EXIT":
    c_str=""
    print("adjacent duplicates removed: ",end="")
    for i in range(len(string)):
        if  i==0 or string[i] != string[i-1]:
            c_str = c_str + string[i]
    print(c_str,end="")       
    print()
    string=str(input("Enter a string(exit to stop): "))
print("Bye!")

