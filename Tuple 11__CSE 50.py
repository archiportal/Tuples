# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 10:04:26 2020

@author: ARCHISMAN ROY
"""

tup = (12,26,32,62,14)
print(tup)
x = input("Enter the key you want to search for :" )
y = int(x)
a=input("Enter :\n1.Linear search\n2.Binary search\n")
b=int(a)
if b==1:
    for i in range(len(tup)):
        if tup[i]==y:
            print("Key element found.")
            break;
        if i==len(tup)-1:
            print("Key element not found.")
elif b==2:
    l=0
    h=len(tup)-1
    while l<=h:
        mid=(l+h)//2
        if y<tup[mid]:
            h=mid-1
        elif y==tup[mid]:
            print("Key element is found.")
            break;
        else:
            l=mid+1
    if l>h:
        print("Key element is not found.")
else:
    print("Wrong input.")          
            

    
    