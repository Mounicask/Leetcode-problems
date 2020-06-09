# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 23:07:43 2020

@author: Sri
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
            for i in s:
                try:
                    index = t.index(i)
                except:
                    return False
                t = t[index+1:]
            return True

s ="leeeeetcode"
t = "yyyyylyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" 
val = sub_sequence(s,t)


print(val)

