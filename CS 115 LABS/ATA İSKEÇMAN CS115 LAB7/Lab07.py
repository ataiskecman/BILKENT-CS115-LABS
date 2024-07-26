# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:16:19 2023

@author: ata.iskecman-ug
"""

from Employee import Employee
from Manager import Manager



def read_employees(fileName):
    list_employee=[]
    openedfile=open(fileName,"r")
    for line in openedfile:
        n=line.split(",")
        p1=None
        if n[0]=="M":
            p1=Manager(n[1],n[2],float(n[3]),float(n[4]))
        elif n[0]=="E":
            p1=Employee(n[1],n[2],float(n[3]))
        if p1 in list_employee:
            print(f"Duplicate employee id:\n{p1}not added")
            
        else:
            list_employee.append(p1)
    return list_employee
L=read_employees("employees.txt")
L=sorted(L)
print()
print("Sorted List:")
print()
print(L)

for emp_salary in L:
    print(f"{emp_salary.get_emp_name()} salary after tax:{emp_salary.calculate_salary()}")
print()
total=0
total_salary=0
for average in L:
    if type(average)==Manager:
        total+=1
        total_salary += average.calculate_salary()
print(f"Average Salary for Managers:{total_salary/total}")