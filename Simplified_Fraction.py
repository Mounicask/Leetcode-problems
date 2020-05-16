# -*- coding: utf-8 -*-
"""
Created on Sat May 16 21:39:17 2020

@author: Sri
"""

#Simplified Fractions
  
    

Input: n = 2
Output: ["1/2"]
Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
Example 2:

Input: n = 3
Output: ["1/2","1/3","2/3"]
Example 3:

Input: n = 4
Output: ["1/2","1/3","1/4","2/3","3/4"]
Explanation: "2/4" is not a simplified fraction because it can be simplified to "1/2".
Example 4:

Input: n = 1
Output: []
    
n = 5
if n ==1:
    print([])
actual_val = []
fraction_list = []
for i in range(1,n+1):
    for j in range(1,n+1):
        val = i/j
        if int(val) !=val and val<1:
            if val not in actual_val:
                actual_val.append(val)
                fraction_list.append(str(i)+'/'+str(j))
print(fraction_list)            

