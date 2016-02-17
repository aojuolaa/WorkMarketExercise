# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:24:56 2016

@author: DEBOLA
"""

import pandas as pd

#read file

c=pd.read_csv("NYC_Jobs.csv")

#use pandas aggregation function to group by Agency

grouped = c['# Of Positions'].groupby(c['Agency'])

#sum the result and sort in descending order

u=grouped.sum().sort_values(ascending=False)
print '\n'
#print the highest value
print 'Most Openings: '  + u.keys()[0] + ' -' +" " + str(u[0])


#the "Posting Updated column provides the status of job

#convert the  column to date format. 
c['Posting_Updated']=pd.to_datetime(c['Posting Updated'])

#change the index of the dataframe to  a date format for easy slicing
c.index=c.Posting_Updated

#for recent job openings we use February 2016 and the status with 
d=c['2016-02']


print '\n'
print  "Highest and Lowest paying positions "
print  "current job openings: February 2016"
print '\n'
print  "FOR ANNUAL RATE: "
#print '\n'

# we extract both annual and hour rate
annual=d[d['Salary Frequency']=='Annual']
hourly=d[d['Salary Frequency']=='Hourly']

#find the highest annual salary
high = max(annual['Salary Range To'])

highest_salary = annual[annual['Salary Range To']==high]


x= highest_salary['Agency'].unique()
print 'Highest:'
for i in x:
    print  i + ' ' + "pays " +str(high)+'/Annum'


print '\n'
#find the lowest annual salary
low = min(annual['Salary Range To'])

#compute all rows equivalent to the highest salary
lowest_salary = annual[annual['Salary Range To']==low]

#return just unique values of Agency
y=lowest_salary['Agency'].unique()

print 'Lowest:'
for i in y:
    print  i + ' ' + "pays   " +str(low)+'/Annum'


print'\n'

#calculate highest and lowest hourly rate
print 'FOR HOURLY RATE:'

high = max(hourly['Salary Range To'])

highest_salary = hourly[hourly['Salary Range To']==high]

x= highest_salary['Agency'].unique()

print "Highest:"
for i in x:
    print i + ' ' + "pays   " +str(high)+'/Hour'



print '\n'

low = min(hourly['Salary Range To'])

lowest_salary = hourly[hourly['Salary Range To']==low]

y=lowest_salary['Agency'].unique()

print 'Lowest:'
for i in y:
    print i + '  ' + "pays   " +str(low)+'/Hour'



