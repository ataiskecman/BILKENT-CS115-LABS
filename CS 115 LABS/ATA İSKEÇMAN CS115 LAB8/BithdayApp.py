# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:02:32 2023

@author: ata.iskecman-ug
"""

from Birthday import *

def read_birthdays(file_name):
    list_birthday=[]
    opened_file = open(file_name,"r")
    for line in opened_file:
        n = line.strip().split(";")
        name=n[0]
        month=n[1]
        day=n[2]
        b1=Birthday(name,month,day)
        if b1 in list_birthday:
            print(f"{b1.getName()} is already in the list")    
        else:
            list_birthday.append(b1)
    return list_birthday

def selection_sort(list1):
    number=0
    while number != len(list1):
        for i in range(number,len(list1)):
            if list1[number] >list1[i]:
                list1[number], list1[i]=list1[i],list1[number]
        number+=1
    return list1

def linear_search(list_birthday,month,day):
    list_matching_names=[]
    for i in list_birthday:
        if month == int(i.getMonth()) and day == int(i.getDay()):
            list_matching_names.append(i.getName())
    return list_matching_names
     
def binarySearch(list1,name):
    startInd=0
    endInd=len(list1)
    if(startInd >= endInd):
        return None
    else:
        mid = (startInd + endInd)//2
        if list1[mid].getName() == name:
            return list1[mid].getDay() + "/" +list1[mid].getMonth()
        elif list1[mid].getName() > name:
            return binarySearch(list1[startInd: mid-1], name)
        elif list1[mid].getName() < name:
            return binarySearch(list1[mid+1: endInd], name)
        else:
            return None
        
read_birthdays("birthdays.txt")
a=int(input("Enter the month:"))
b=int(input("Enter the day:"))

temp1=read_birthdays("birthdays.txt")
temp2=linear_search(temp1, a, b)



print(f"People Born on the given day:{temp2}")
print("Sorted List")
print(selection_sort(temp1))
print()
c=str(input("Enter a name to search:"))
print(c,":",binarySearch(temp1,c))



