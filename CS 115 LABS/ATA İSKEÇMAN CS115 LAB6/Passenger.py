# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 08:51:44 2023

@author: ata.iskecman-ug
"""

class passenger(object):
    def __init__(self,passengerName,passengerSurname,seatNo,fare=1000):
        self.__passengerName=passengerName
        self.__passengerSurname=passengerSurname
        self.__seatNo=seatNo
        self.__fare=fare
        
    def getpassengerName(self):
        return self.__passengerName
    
    def getpassengerSurname(self):
        return self.__passengerSurname
    
    def getpassengerseatNo(self):
        return self.__seatNo
    
    def setseatNo(self,new_seatNo):
        self.__seatNo = new_seatNo
        return self.__seatNo
    
    def setfare(self,new_fare):
        self.__fare = float(new_fare)
        return self.__fare
    
    def calculateFare(self):
        if self.__fare<1000:
            self.__fare=self.__fare*1.05
            return self.__fare
    def __str__(self):
        return f"Passenger Name:{self.__passengerSurname} {self.__passengerName} Seat:{self.__seatNo}"
    def __repr__(self):
        return f"({self.__passengerSurname} {self.__passengerName[0]}. {self.__seatNo} {self.__fare}TL)\n"