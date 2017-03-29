# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:31:53 2015

@author: Naman
"""
import re




def monthvalue(date):
    return{
        'Jan' : 1,
        'Feb' : 2,
        'Mar' : 3,
        'Apr' : 4,
        'May' : 5,
        'Jun' : 6,
        'Jul' : 7,
        'Aug' : 8,
        'Sep' : 9, 
        'Oct' : 10,
        'Nov' : 11,
        'Dec' : 12}[date]
        
def compute_time_diff(month,time):
    #Considering Sep as base month (Value=9)
    #Code is written considering only months Sep and Oct since considering only 30 days
    value=(month-9)*30*24*60*60+(float(time[0])-1)*24*60*60+float(time[1])*60*60+float(time[2])*60+float(time[3])
    return value   

def timevalue(dates):
    #test=dates[0:5]
    pattern='\d{1,2}\:\d{2}\:\d{2}\:\d{2}\.\d{6}'
    for index,date in enumerate(dates):
        month=monthvalue(re.search('^([^\s]+)',date).group(0))
        time=re.search(pattern,date).group(0).split(':')
        #takes into consideration base date as Sep 1:00:00:00:000000
        value=compute_time_diff(month,time)
        dates[index]=value
    return dates
        
 
#print monthvalue('Sep')      