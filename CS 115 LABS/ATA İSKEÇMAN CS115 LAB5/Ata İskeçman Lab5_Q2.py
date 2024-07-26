# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:49:06 2023

@author: ata.iskecman-ug
"""
#
def select_tuples(a):
    b = ()
    for i in a:
        if type(i)==tuple:
            b += (i,)
    return b

n =  (5, 'ab', (1, 4), 4.3, 'xyz', (2, 'a'))


print(f"input tuple: {n}\ntuples in input tuple:{select_tuples(n)}")



