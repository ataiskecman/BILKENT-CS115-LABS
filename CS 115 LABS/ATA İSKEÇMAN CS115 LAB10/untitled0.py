# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 08:54:35 2023

@author: ata.iskecman-ug
"""

import numpy as np
import matplotlib.pyplot as pl


time = np.array([0,2.5,5,10,15,20])
amount =np.array([5000,5600,6700,9000,12000,16000])


pl.clf()

pl.xlabel('Passed Years')
pl.ylabel('Dollars')
pl.title("Money Amount in the Bank")


coefficient = np.polyfit(time,amount,1)

new_amount = np.polyval(coefficient,time)

pl.plot(time, amount, 'bo')
pl.plot(time,new_amount,"-r")