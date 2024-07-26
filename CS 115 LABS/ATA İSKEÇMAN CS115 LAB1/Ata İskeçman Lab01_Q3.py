# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:52:00 2023

@author: ata.iskecman-ug
"""

#Q3

second = int(input("Enter number of seconds: "))
if second < 0:
    print("The number of seconds must be positive.")
elif  0 <= second <= 60 :
    print(second ,"secs")
elif 60 <= second <= 60 ** 2:
    print(int(second/ 60), "minutes", second % 60, "secs") 
elif 60 **2 <= second <= 60 ** 2 * 24:
    print(int(second/ 60 ** 2), "hours",int(second/ 60)%60, "minutes", (second%(60**2))%60, "secs")
elif 60 **2*24 <= second : 
    print(int(second/ (60 ** 2 * 24)), "days",int(second/(60**2)%24),"hours", int((second/60)%60),"minutes", int(((second%(60**2*24))%60**2)%60), "secs")
    