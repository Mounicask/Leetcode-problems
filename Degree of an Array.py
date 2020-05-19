# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:47:03 2020

@author: Sri
"""

697. Degree of an Array


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_element = []
        final_val_list = []
        max_val = 0
        for i in set_nums:
            val = nums.count(i)
            if val>max_val:
                max_element = [i]
                max_val = val
            elif val == max_val:
                max_element.append(i)
        for i in max_element:
            element_list = [index for index,element in enumerate(nums) if element == i]
            final_val_list.append(max(element_list)-min(element_list)+1)
        return (min(final_val_list)) 
    
nums = [1,3,2,2,3,1]
left = {}
right = {}
count = {}
final_list = []
for i in range(0,len(nums)):
    if nums[i] not in left:
        left[nums[i]] = i
    right[nums[i]] = i
    if nums[i] not in count:
        count[nums[i]] = nums.count(nums[i])
val = max(count.values())
for i,j in count.items():
    if j == val:
        final_list.append(right[i]-left[i]+1)
print(min(final_list))