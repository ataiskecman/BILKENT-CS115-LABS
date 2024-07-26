# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 09:52:45 2023

@author: ata.iskecman-ug
"""

import numpy as np
import matplotlib.pyplot as pl

file = np.loadtxt("students.txt",skiprows=1)

col0 = file[:,0]
col1 = file[:,1]
col2 = file[:,2]
col3 = file[:,3]
col4 = file[:,4]

male = np.array(file[file[:,0]==0])
female = np.array(file[file[:,0]==1])

completed = np.array(file[file[:,1]==1])

completed_reading = completed[:,3]
completed_writing = completed[:,4]


mean_male = np.mean(male[:,2])
mean_female = np.mean(female[:,2])

pl.clf()

pl.subplot(3,1,1)

bar_width = 0.25

pl.ylabel("Avg of Math Gr.")
pl.bar("Female Students",mean_female,bar_width)
pl.bar("Male Students",mean_male,-bar_width)
pl.title("Comparison of Math Grades:Female vs Male")


pl.subplot(3,1,2)

pl.plot(completed_reading,"ro--")
pl.plot(completed_writing,"ko:")

pl.legend(["Reading","Writing"])

pl.subplot(3,1,3)

label = "man", "woman"
len_male = len(male)
len_female = len(female)
sizes = [len(male),len(female)]

explode = (0,0.1)
pl.pie(sizes, explode=explode ,labels=label, autopct="%1.1f%%")
