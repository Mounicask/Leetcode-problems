# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isSibling(root, a , b): 
    if root is None: 
        return 0
    if root.left is not None and root.right is not None:
        return ((root.left.val == a and root.right.val ==b) or 
            (root.left.val == b and root.right.val == a)or
            isSibling(root.left, a, b) or
            isSibling(root.right, a, b)) 
        
    if root.left is not None or root.right is  None:
        return isSibling(root.left, a, b)
    if root.right is not None or root.left is  None:
        return isSibling(root.right, a, b)
  

def level(root, ptr, lev): 
    if root is None : 
        return 0 
    if root.val == ptr:  
        return lev 
    l = level(root.left, ptr, lev+1) 
    if l != 0: 
        return l 
    return level(root.right, ptr, lev+1) 
  
 
def isCousins( root: TreeNode, x: int, y: int) -> bool:
        if ((level(root,x,1) == level(root, y, 1)) and 
            not (isSibling(root, x, y))): 
            return 1
        else: 
            return 0       
        
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
val = isCousins(root,3,4)
print("val is ",val)