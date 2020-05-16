# -*- coding: utf-8 -*-
"""
Created on Sat May 16 21:37:55 2020

@author: Sri
"""

#Consecutive Characters

s= 'triplepillooooow'
s = "leetcode"
s= "tourist"
s = "ccbccbb"
dic = dict()
n = len(s)-1
for i in range(0,len(s)-1):
    if s[i] == s[i+1]:
        count = 1        
        while s[i] == s[i+1] and i<n:
            count = count +1
            i = i +1
            if i==n:
                break         
        if s[i] in dic:
            if dic[s[i]] < count:
                dic[s[i]] = count
        else:
            dic[s[i]] = count
if len(dic)!=0:
    print(max(dic.values()))
else:
    print("1")
