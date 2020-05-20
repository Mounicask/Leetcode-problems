# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:51:53 2020

@author: Sri
"""

Right View of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        final_list = []
        queue = [root]
        while queue:
            interim_list = list(queue)
            while interim_list:
                val = interim_list.pop(0)
                queue.pop(0)
                if len(interim_list) == 0:
                    final_list.append(val.val)
                if val.left:
                    queue.append(val.left)
                if val.right:
                    queue.append(val.right)
        return   final_list      