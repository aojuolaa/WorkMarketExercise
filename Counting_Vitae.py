# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 18:55:08 2016

@author: DEBOLA
"""

import re
from collections import defaultdict
import matplotlib.pyplot as plt

#read in the file
f = open('ADEBOLA_OJUOLA_Resume.txt','r')
mystr=f.readlines()

#remove all none-word characters
mystr=re.sub(r"\W", "", mystr[0])
#mystr=re.sub(r"\d", "", mystr)

#split the characters into a list
l=list(mystr.lower())

#Create a dictionary to store character and values in key-value pair
def count(xyz):
    counts = defaultdict(int)
    for x in xyz:
        counts[x] += 1 
    return counts
    
 #call the function   
xl=count(l)    

#create bar chat
plt.bar(range(len(xl)), xl.values(), align='center')
plt.xticks(range(len(xl)), list(xl.keys()))

plt.show()