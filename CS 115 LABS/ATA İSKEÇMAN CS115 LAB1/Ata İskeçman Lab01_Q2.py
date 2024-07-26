# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:51:40 2023

@author: ata.iskecman-ug
"""

#Q2

Card_notation = str(input("Enter the card notation: "))
if Card_notation[0:-1] == "A" :
    Card_notation1 = "Ace"
elif Card_notation[0:-1] == "j" :
    Card_notation1 = "Jack"
elif Card_notation[0:-1] == "Q" :
    Card_notation1 = "Queen"
elif Card_notation[0:-1] == "K" :
    Card_notation1 = "King"
else :
    Card_notation1 = Card_notation[0:-1]
    
if Card_notation[-1] == "D" :
    Card_notation2 = "Diamond"
elif Card_notation[-1] == "H" :
    Card_notation2 = "Hearts"
elif Card_notation[-1] == "S" :
    Card_notation2 = "Spades"
elif Card_notation[-1] == "C" :
    Card_notation2 = "Clubs"

print(Card_notation1 , "of" , Card_notation2)