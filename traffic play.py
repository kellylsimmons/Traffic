# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 13:16:10 2015

@author: student
"""

import os
import pandas as pd
import matplotlib as plt
from datetime import datetime
 
data = pd.read_csv('C:\Users\student.BOOZ-A9OR3F5AHU\Downloads\Traffic_Violations.csv')
test = data.head(100)
#Questions
## Do Alcohol related accidents vary by time and day? 
### coding day of week

for row in data['Date Of Stop']:
    data['Weekday']=datetime.weekday(datetime.strptime(row,'%m/%d/%Y'))
#coding for day
day_map = {
0:'Monday',
1:'Tuesday',
2:'Wednesday',
3:'Thursday',
4:'Friday',
5:'Saturday',
6:'Sunday'}

data['Weekday Text'] = data['Weekday'].map(day_map)

data.pivot_table(index = ['Weekday Text','Race'])


## Are some vehicles more likely to be stopped than others?  
## Are some vehicles more likely to be involved in a fatality? 
## Are some Vehicles more likely to be involved in an alcohol related accident? 
## Are women more likely to be warnings then men? 
## Are women more likely than men to be stoped by police in MONTCO? 
## Are women more likely than men to be involved in a traffic fataility?
## What is the most likely day time to get stoped by a cop?   
## does this vary by gender? 
##where is propery damage most likely to occur
## Where are the most dangerous intersections in MONTCO? By number of accidents and fatalities?