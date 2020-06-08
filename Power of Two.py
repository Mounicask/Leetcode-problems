# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:48:51 2020

@author: Sri
"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false


def isPowerOfTwo(n: int) -> bool:
    if n == 1:
        return True
    if n == 0:
        return False
    while n:
        if n % 2 ==0:
            n = n //2
        else:
            break
    if n == 1:
        return True
    else:
        return False
    
val = isPowerOfTwo(2)
print(val)

