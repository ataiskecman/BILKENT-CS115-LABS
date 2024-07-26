# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 09:50:19 2023

@author: ata.iskecman-ug
"""
my_dict = {}



def addCustomer(my_dict,customer_id_number, account_id, branch_name, balance):
    if customer_id_number in my_dict :
        print("Customer already exists")
    else:
        my_dict[customer_id_number] = (account_id,branch_name,balance)
        print("Customer Added")
        
def addAccount(my_dict, customer_id_number, account_id, branch_name, balance):
        if customer_id_number in my_dict:
            my_dict[customer_id_number] = (my_dict[customer_id_number],)+ ((account_id,branch_name,balance),)
            print("Account Added")
        else:
            print("error")
            
def findCustomer(customer_id_number):
    if customer_id_number in my_dict:
        print(my_dict.values())
    else:
        return None


n= int(input("1)Add Customer\n2)Search Customer\n3)Add Account\n4)Quit\nEnter Choice:"))            
while True:
    if n == 1:
        customer_id_number=int(input("Enter customer number: "))
        account_id=int(input("Enter account id: "))
        branch_name=str(input("Enter branch name: "))
        balance=int(input("Enter balance: "))
        print(addCustomer(my_dict,customer_id_number, account_id, branch_name, balance))
    elif n == 2:
        customer_id_number=int(input("Enter customer number: "))
        print(findCustomer(customer_id_number))
    elif n == 3:
        customer_id_number=int(input("Enter customer number: "))
        account_id=int(input("Enter account id: "))
        branch_name=str(input("Enter branch name: "))
        balance=int(input("Enter balance: "))
        print(addAccount(my_dict,customer_id_number, account_id, branch_name, balance))
    elif n == 4:
        print("Program Ended....")
        break
    n= int(input("1)Add Customer\n2)Search Customer\n3)Add Account\n4)Quit\nEnter Choice:"))