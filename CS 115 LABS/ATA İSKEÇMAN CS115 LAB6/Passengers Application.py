# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:37:12 2023

@author: ata.iskecman-ug
"""

from Passenger import *



def load_passengers(file):
    passengerList=[]
    try:
        with open(file, encoding='utf-8') as file:
            openedfile = file.readlines()
    except UnicodeDecodeError:
        with open(file, encoding='latin-1') as file:
            openedfile = file.readlines()
    for line in openedfile:
        line=line.strip().split(";")
        passengerName=line[0]
        passengerSurname=line[1]
        fare=line[2]
        seatNo=line[3]
        p=passenger(line[0],line[1],line[3].strip(),line[2])
        passengerList.append(p)
    return passengerList

L=load_passengers("passengers.txt")

input_name=str(input("Enter name:"))
input_surname=str(input("Enter surname:"))
passengerFound= False

for i in L:
    if input_name==i.getpassengerName() and input_surname==i.getpassengerSurname():
        input_fare=str(input("Enter new price:"))
        print(i)
        print("UPDATED")
        i.setfare(input_fare)  
        passengerFound= True

if passengerFound==False:
    print("Passenger is NOT Found!")
print(L)






        
        
        




    
    
    
    