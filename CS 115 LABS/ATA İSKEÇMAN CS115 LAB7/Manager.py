# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 10:11:21 2023

@author: ata.iskecman-ug
"""

from Employee import Employee

class Manager(Employee):
    def __init__(self,emp_name,id_num,wage,bonus,tax_rate=0.3,extra_salary=0.1):
        super().__init__(emp_name,id_num,wage,tax_rate)
        self.bonus=float(bonus)
        
    def getBonus(self,bonus):
        return float(self.bonus)
    
    def calculate_salary(self):
        a=(self.get_wage()*1.1+self.bonus)*0.7
        return a
    
    def __repr__(self):
        return f"{super().__repr__()} Bonus:{self.bonus}\n"