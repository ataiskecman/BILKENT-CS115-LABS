# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Employee:
    def __init__(self,emp_name,id_num,wage, tax_rate=0.3):
        self.__tax_rate=tax_rate
        self.__emp_name=self.set_emp_name(emp_name)
        self.__id_num=id_num
        self.__wage=wage
        
        self.set_id_num(id_num)
        self.set_wage(wage)
        
    def get_tax_rate(self):
        return self.__tax_rate
    
    def get_emp_name(self):
        return self.__emp_name
    
    def get_id_num(self):
        return self.__id_num
    
    def get_wage(self):
        return self.__wage
    
    def set_emp_name(self,new_name):
        str_new_name=""
        for i in new_name:
            if i.isalpha() or i==" ":
                str_new_name+=i
        self.new_name=str_new_name
        return self.new_name       
    
    def set_id_num(self,new_id_num):
        try:
            new_id_num = int(new_id_num)
            self.__id_num = new_id_num
        except:
            self.__id_num = 11111111
            
    def set_wage(self,new_wage):
        if new_wage <0:
            new_wage=0
            self.__wage = new_wage
        else:
            self.__wage = new_wage
            
    
    
    
    def calculate_salary(self):
        salary=self.__wage*(1-self.__tax_rate)
        self.new_salary=salary
        return self.new_salary
    
    def __eq__(self,other):
        if isinstance(other, Employee):    
            return self.get_id_num() == other.get_id_num()
        else:
            return False
            
    def __lt__(self,another):
        if isinstance(another, Employee):
            myName = self.__emp_name.split(" ")
            other = another.get_emp_name().split(" ")
            if myName[-1]<other[-1]:
                return True
            elif myName[-1]==other[-1]:
                if myName[0]<other[0]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __repr__(self):
        return f"Name:{self.__emp_name}\tEmployee ID:{self.__id_num}Wage:{self.__wage}\n"
    