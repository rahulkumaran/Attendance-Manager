# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 22:54:54 2017

@author: Rahul
"""

print"----------------------------------------------"
n = int(raw_input("Enter the number of students in class:\n"))
print"----------------------------------------------"
values = raw_input("Enter roll numbers of students who are present:\n")
value_list = values.split(",")
value_list_new = []             
s_list =[]

''' function for initialising the value_list_new with 500 0's '''
for i in range(0,500):
    value_list_new = value_list_new+[0]

''' function to convert the string values in value_list to integers '''   
for i in range(0,len(value_list)):
    value_list[i]=int(value_list[i])

''' function for the same purpose as above but to also take
    rollnumbers beyond the len of the initial value_list'''    
for j in range(len(value_list),max(value_list)):
    value_list=value_list+[0]
    
#print value_list
''' function to check whether or not a student with a particular 
    roll number was present or not. If absent prints 0 '''
for i in range(0,len(value_list)):
    #k=i+1 not in value_list
    #print k
    if(i+1 in value_list):
        value_list_new[i]=i+1
        
    else:
        value_list_new[i]=0
        
#print value_list_new
for i in range(0,n):
    s_list.append(value_list_new[i])

print"----------------------------------------------"
print"Number of students absent : ",s_list.count(0)
print "The roll numbers of students who are absent are:"    
for i in range(0,len(s_list)):
    if(i+1 not in s_list):
        print i+1
print"----------------------------------------------"    
#print s_list